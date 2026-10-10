"""Exercise the real PowerShell script against disposable local Git remotes."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / 'auto-sync.ps1'
POWERSHELL = shutil.which('powershell.exe')


@unittest.skipUnless(POWERSHELL and shutil.which('git'), 'Requires Windows PowerShell and Git')
class AutoSyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='notes-sync-test-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.remote = self.root / 'remote.git'
        self.work = self.root / 'work'
        self.env = dict(os.environ, GIT_TERMINAL_PROMPT='0')
        self.run_git(self.root, 'init', '--bare', '--initial-branch=main', str(self.remote))
        self.run_git(self.root, 'init', '--initial-branch=main', str(self.work))
        self.configure(self.work)
        (self.work / 'docs').mkdir()
        (self.work / 'docs/index.md').write_text('# Original\n', encoding='utf-8')
        (self.work / 'docs/delete.md').write_text('# Delete fixture\n', encoding='utf-8')
        (self.work / 'mkdocs.yml').write_text('site_name: Fixture\n', encoding='utf-8')
        (self.work / 'requirements.txt').write_text('original\n', encoding='utf-8')
        shutil.copyfile(SCRIPT, self.work / 'auto-sync.ps1')
        self.git('add', '.')
        self.git('commit', '-m', 'Initial fixture')
        self.git('remote', 'add', 'origin', str(self.remote))
        self.git('push', '-u', 'origin', 'main')
        self.initial = self.git('rev-parse', 'HEAD')

    def run_git(self, directory, *args):
        result = subprocess.run(
            ['git', '-C', str(directory), *args], env=self.env,
            capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=20,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result.stdout.strip()

    def git(self, *args):
        return self.run_git(self.work, *args)

    def configure(self, directory):
        for key, value in [('user.name', 'Notes Test'), ('user.email', 'test@example.invalid'),
                           ('commit.gpgsign', 'false'), ('core.hooksPath', str(self.root / 'no-hooks'))]:
            self.run_git(directory, 'config', key, value)

    def sync(self, cwd=None):
        return subprocess.run(
            [POWERSHELL, '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File',
             str(self.work / 'auto-sync.ps1'), '-Once'], cwd=cwd or self.work, env=self.env,
            capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=40,
        )

    def change_notes(self):
        (self.work / 'docs/index.md').write_text('# Changed\n', encoding='utf-8')
        (self.work / 'docs/new.md').write_text('# New\n', encoding='utf-8')
        (self.work / 'docs/delete.md').unlink()
        (self.work / 'mkdocs.yml').write_text('site_name: Updated fixture\n', encoding='utf-8')

    def remote_head(self):
        return self.run_git(self.remote, 'rev-parse', 'main')

    def test_main_syncs_add_modify_delete_and_preserves_unrelated_staging(self):
        self.change_notes()
        (self.work / 'requirements.txt').write_text('unrelated change\n', encoding='utf-8')
        self.git('add', 'requirements.txt')
        result = self.sync()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('Pushed and verified main', result.stdout)
        self.assertNotIn('NativeCommandError', result.stdout + result.stderr)
        self.assertEqual(self.remote_head(), self.git('rev-parse', 'HEAD'))
        self.assertNotEqual(self.remote_head(), self.initial)
        self.assertEqual(self.git('diff', '--cached', '--name-only'), 'requirements.txt')
        self.assertEqual(set(self.git('show', '--format=', '--name-status', 'HEAD').splitlines()), {
            'D\tdocs/delete.md', 'M\tdocs/index.md', 'A\tdocs/new.md', 'M\tmkdocs.yml',
        })

    def assert_branch_skipped(self):
        self.change_notes()
        before = self.git('status', '--porcelain')
        result = self.sync()
        self.assertEqual(result.returncode, 1)
        self.assertIn('requires the main branch', result.stdout)
        self.assertNotIn('Pushed and verified', result.stdout)
        self.assertEqual(self.git('status', '--porcelain'), before)
        self.assertEqual(self.git('rev-parse', 'HEAD'), self.initial)
        self.assertEqual(self.remote_head(), self.initial)

    def test_detached_head_has_no_mutations(self):
        self.git('checkout', '--detach')
        self.assert_branch_skipped()

    def test_feature_branch_has_no_mutations(self):
        self.git('checkout', '-b', 'feature/test')
        self.assert_branch_skipped()

    def test_no_changes_does_not_create_commit(self):
        result = self.sync()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('No pending commits', result.stdout)
        self.assertEqual(self.git('rev-parse', 'HEAD'), self.initial)

    def test_duplicate_worker_is_blocked_and_recovers_after_exit(self):
        # Keep one real worker idle while a second process attempts to sync.
        with (self.root / 'worker.log').open('w+', encoding='utf-8') as log:
            worker = subprocess.Popen(
                [POWERSHELL, '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File',
                 str(self.work / 'auto-sync.ps1'), '-IntervalSeconds', '86400'],
                cwd=self.work, env=self.env, stdout=log, stderr=subprocess.STDOUT,
            )
            try:
                deadline = time.monotonic() + 15
                while time.monotonic() < deadline:
                    log.seek(0)
                    output = log.read()
                    if 'Checking docs/' in output:
                        break
                    self.assertIsNone(worker.poll(), output)
                    time.sleep(0.1)
                else:
                    self.fail('Worker did not start: ' + output)
                self.change_notes()
                before = self.git('status', '--porcelain')
                duplicate = self.sync(cwd=self.root)
                self.assertEqual(duplicate.returncode, 1, duplicate.stdout + duplicate.stderr)
                self.assertIn('already running', duplicate.stdout)
                self.assertEqual(self.git('status', '--porcelain'), before)
                self.assertEqual(self.remote_head(), self.initial)
            finally:
                worker.terminate()
                worker.wait(timeout=10)

        recovered = self.sync()
        self.assertEqual(recovered.returncode, 0, recovered.stdout + recovered.stderr)
        self.assertEqual(self.remote_head(), self.git('rev-parse', 'HEAD'))

    def test_unwatched_changes_stay_uncommitted(self):
        (self.work / 'requirements.txt').write_text('changed\n', encoding='utf-8')
        result = self.sync()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.git('rev-parse', 'HEAD'), self.initial)
        self.assertIn('requirements.txt', self.git('status', '--porcelain'))

    def advance_remote(self):
        other = self.root / 'other'
        self.run_git(self.root, 'clone', str(self.remote), str(other))
        self.configure(other)
        (other / 'docs/index.md').write_text('# Remote change\n', encoding='utf-8')
        self.run_git(other, 'add', '.')
        self.run_git(other, 'commit', '-m', 'Remote fixture change')
        self.run_git(other, 'push', 'origin', 'main')
        return self.remote_head()

    def test_remote_ahead_is_reported_even_without_local_changes(self):
        remote = self.advance_remote()
        result = self.sync()
        self.assertEqual(result.returncode, 1)
        self.assertIn('Remote main has changes', result.stdout)
        self.assertEqual(self.git('rev-parse', 'HEAD'), self.initial)
        self.assertEqual(self.remote_head(), remote)

    def test_divergence_does_not_overwrite_remote(self):
        remote = self.advance_remote()
        self.change_notes()
        result = self.sync()
        self.assertEqual(result.returncode, 1)
        self.assertIn('Remote main has changes', result.stdout)
        self.assertNotEqual(self.git('rev-parse', 'HEAD'), self.initial)
        self.assertEqual(self.remote_head(), remote)

    def test_remote_unavailable_retains_commit_and_retries(self):
        self.change_notes()
        self.git('remote', 'set-url', 'origin', str(self.root / 'unavailable.git'))
        first = self.sync()
        self.assertEqual(first.returncode, 1)
        self.assertIn('Local commits are retained', first.stdout)
        local = self.git('rev-parse', 'HEAD')
        self.assertNotEqual(local, self.initial)
        self.assertEqual(self.remote_head(), self.initial)
        self.git('remote', 'set-url', 'origin', str(self.remote))
        second = self.sync()
        self.assertEqual(second.returncode, 0, second.stdout + second.stderr)
        self.assertEqual(self.remote_head(), local)
        self.assertEqual(self.git('rev-parse', 'HEAD'), local)

    def test_merge_in_progress_preserves_working_tree_and_index(self):
        self.change_notes()
        marker = self.work / self.git('rev-parse', '--git-path', 'MERGE_HEAD')
        marker.write_text(self.initial + '\n', encoding='ascii')
        before = self.git('status', '--porcelain')
        result = self.sync()
        self.assertEqual(result.returncode, 1)
        self.assertIn('Git operation is in progress', result.stdout)
        self.assertEqual(self.git('status', '--porcelain'), before)
        self.assertEqual(self.git('rev-parse', 'HEAD'), self.initial)


if __name__ == '__main__':
    unittest.main()
