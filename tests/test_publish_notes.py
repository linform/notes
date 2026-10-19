"""Regression coverage for completion-time publishing from real Git worktrees.

All remotes are disposable local repositories. A tiny command stub represents
the build result; CI's independent build job checks the actual MkDocs project.
"""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time
import unittest


ROOT = Path(__file__).resolve().parents[1]
POWERSHELL = shutil.which('powershell.exe')


@unittest.skipUnless(POWERSHELL and shutil.which('git'), 'Requires Windows PowerShell and Git')
class PublishNotesTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='notes-publish-test-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.main = self.root / 'main notes'
        self.remote = self.root / 'remote.git'
        self.env = dict(os.environ, GIT_TERMINAL_PROMPT='0')
        self.git(self.root, 'init', '--bare', '--initial-branch=main', str(self.remote))
        self.git(self.root, 'init', '--initial-branch=main', str(self.main))
        for key, value in [('user.name', 'Notes Test'), ('user.email', 'test@example.invalid'),
                           ('commit.gpgsign', 'false'), ('core.hooksPath', str(self.root / 'no-hooks'))]:
            self.git(self.main, 'config', key, value)
        (self.main / 'docs').mkdir()
        (self.main / 'docs/index.md').write_text('# Original\n', encoding='utf-8')
        (self.main / 'mkdocs.yml').write_text('site_name: Fixture\n', encoding='utf-8')
        (self.main / '.gitignore').write_text('site/\n', encoding='utf-8')
        for name in ('publish-notes.ps1', 'auto-sync.ps1'):
            shutil.copyfile(ROOT / name, self.main / name)
        self.git(self.main, 'add', '.')
        self.git(self.main, 'commit', '-m', 'Initial fixture')
        self.git(self.main, 'remote', 'add', 'origin', str(self.remote))
        self.git(self.main, 'push', '-u', 'origin', 'main')
        self.initial = self.git(self.main, 'rev-parse', 'HEAD')
        self.source = self.root / 'draft notes'
        self.git(self.main, 'worktree', 'add', '--detach', str(self.source), self.initial)
        self.builder = self.root / 'build-gate.cmd'
        self.builder.write_text('@echo off\r\nexit /b 0\r\n', encoding='ascii')

    def git(self, directory, *args):
        result = subprocess.run(['git', '-C', str(directory), *args], env=self.env,
                                capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=20)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result.stdout.strip()

    def publish(self, directory=None, *args):
        directory = directory or self.source
        return subprocess.run([POWERSHELL, '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File',
                               str(directory / 'publish-notes.ps1'), '-PythonPath', str(self.builder), *args],
                              cwd=self.root, env=self.env, capture_output=True, text=True,
                              encoding='utf-8', errors='replace', timeout=45)

    def edit(self, directory=None):
        directory = directory or self.source
        (directory / 'docs/index.md').write_text('# Completed notes\n', encoding='utf-8')
        (directory / 'docs/new.md').write_text('# New article\n', encoding='utf-8')

    def remote_head(self):
        return self.git(self.remote, 'rev-parse', 'main')

    def assert_success(self, result):
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('Pushed and verified main', result.stdout)
        self.assertNotIn('NativeCommandError', result.stdout + result.stderr)
        self.assertEqual(self.remote_head(), self.git(self.main, 'rev-parse', 'HEAD'))

    def assert_blocked(self, expected):
        before = self.git(self.source, 'status', '--porcelain')
        result = self.publish()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(expected, result.stdout)
        self.assertNotIn('Pushed and verified main', result.stdout)
        self.assertEqual(self.remote_head(), self.initial)
        self.assertEqual(self.git(self.source, 'rev-parse', 'HEAD'), self.initial)
        self.assertEqual(self.git(self.source, 'status', '--porcelain'), before)

    def test_detached_worktree_updates_main_and_remote_without_publishing_ref(self):
        self.edit()
        (self.source / 'ref').mkdir()
        (self.source / 'ref/private.pptx').write_bytes(b'fixture must stay local')
        self.assert_success(self.publish())
        self.assertEqual(self.remote_head(), self.git(self.source, 'rev-parse', 'HEAD'))
        self.assertEqual((self.main / 'docs/new.md').read_text(), '# New article\n')
        self.assertNotIn('ref/', self.git(self.remote, 'ls-tree', '-r', '--name-only', 'main'))
        self.assertEqual(self.git(self.source, 'diff', '--name-only'), '')

    def test_feature_branch_and_retry_do_not_create_duplicate_commits(self):
        self.git(self.source, 'switch', '-c', 'codex/draft')
        self.edit()
        self.assert_success(self.publish())
        target = self.remote_head()
        self.assert_success(self.publish())
        self.assertEqual(self.remote_head(), target)

    def test_main_can_publish_directly(self):
        self.edit(self.main)
        self.assert_success(self.publish(self.main))

    def test_dirty_main_is_preserved(self):
        self.edit()
        self.edit(self.main)
        self.git(self.main, 'add', 'docs/index.md')
        status = self.git(self.main, 'status', '--porcelain')
        self.assert_blocked('Main working directory has uncommitted changes')
        self.assertEqual(self.git(self.main, 'status', '--porcelain'), status)

    def test_main_operation_in_progress_is_preserved(self):
        self.edit()
        marker = Path(self.git(self.main, 'rev-parse', '--path-format=absolute', '--git-path', 'MERGE_HEAD'))
        marker.write_text(self.initial + '\n', encoding='ascii')
        self.assert_blocked('Git operation is in progress')
        self.assertTrue(marker.exists())

    def test_strict_build_failure_does_not_commit_merge_or_push(self):
        self.edit()
        self.builder.write_text('@echo off\r\nexit /b 7\r\n', encoding='ascii')
        self.assert_blocked('Strict documentation build failed')
        self.assertEqual(self.git(self.main, 'rev-parse', 'HEAD'), self.initial)

    def test_course_preparation_runs_before_validation_and_publishes_generated_notes(self):
        (self.source / 'scripts').mkdir()
        (self.source / 'scripts/course_content.py').write_text('# preparation fixture\n')
        self.builder.write_text(
            f'@echo off\r\nif "%~1"=="-X" echo generated course> "{self.source / "docs/complete.md"}"\r\nexit /b 0\r\n',
            encoding='ascii',
        )
        self.assert_success(self.publish())
        self.assertIn('generated course', (self.main / 'docs/complete.md').read_text())

    def test_course_preparation_failure_does_not_commit_or_push(self):
        self.edit()
        (self.source / 'scripts').mkdir()
        (self.source / 'scripts/course_content.py').write_text('# preparation fixture\n')
        self.builder.write_text('@echo off\r\nif "%~1"=="-X" exit /b 8\r\nexit /b 0\r\n', encoding='ascii')
        self.assert_blocked('Course content preparation failed')

    def test_main_switching_branches_during_build_does_not_publish(self):
        self.edit()
        self.builder.write_text(
            f'@echo off\r\ngit -C "{self.main}" switch -c other-task\r\nexit /b 0\r\n',
            encoding='ascii',
        )
        result = self.publish()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('changed branches during validation', result.stdout)
        self.assertEqual(self.remote_head(), self.initial)
        self.assertEqual(self.git(self.main, 'rev-parse', 'HEAD'), self.initial)
        self.assertEqual(self.git(self.main, 'branch', '--show-current'), 'other-task')
        self.assertNotEqual(self.git(self.source, 'rev-parse', 'HEAD'), self.initial)

    def test_notes_changing_during_build_are_preserved_without_publishing(self):
        self.edit()
        for operation in ('modify', 'add', 'delete', 'config'):
            with self.subTest(operation=operation):
                if operation == 'modify':
                    command = f'echo edited during build> "{self.source / "docs/index.md"}"'
                elif operation == 'add':
                    command = f'echo new attachment> "{self.source / "docs/attachment.pdf"}"'
                elif operation == 'delete':
                    command = f'del "{self.source / "docs/new.md"}"'
                else:
                    command = f'echo site_name: Changed> "{self.source / "mkdocs.yml"}"'
                self.builder.write_text(f'@echo off\r\n{command}\r\nexit /b 0\r\n', encoding='ascii')
                result = self.publish()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn('Notes changed during validation', result.stdout)
                self.assertEqual(self.remote_head(), self.initial)
                self.assertEqual(self.git(self.source, 'rev-parse', 'HEAD'), self.initial)
                self.assertEqual(self.git(self.main, 'rev-parse', 'HEAD'), self.initial)
        self.assertIn('edited during build', (self.source / 'docs/index.md').read_text())
        self.assertTrue((self.source / 'docs/attachment.pdf').exists())
        self.assertFalse((self.source / 'docs/new.md').exists())
        self.assertIn('Changed', (self.source / 'mkdocs.yml').read_text())

    def test_remote_ahead_cannot_be_overwritten(self):
        other = self.root / 'other'
        self.git(self.root, 'clone', str(self.remote), str(other))
        self.git(other, 'config', 'user.name', 'Notes Test')
        self.git(other, 'config', 'user.email', 'test@example.invalid')
        self.git(other, 'config', 'commit.gpgsign', 'false')
        (other / 'docs/index.md').write_text('# Remote advance\n', encoding='utf-8')
        self.git(other, 'add', 'docs/index.md')
        self.git(other, 'commit', '-m', 'Remote advance')
        self.git(other, 'push', 'origin', 'main')
        target = self.remote_head()
        self.edit()
        before = self.git(self.source, 'status', '--porcelain')
        result = self.publish()
        self.assertEqual(result.returncode, 1)
        self.assertIn('Remote main has changes', result.stdout)
        self.assertEqual(self.remote_head(), target)
        self.assertEqual(self.git(self.source, 'status', '--porcelain'), before)

    def test_main_ahead_requires_reconciliation(self):
        self.edit(self.main)
        self.git(self.main, 'add', 'docs')
        self.git(self.main, 'commit', '-m', 'Other task completed')
        target = self.git(self.main, 'rev-parse', 'HEAD')
        self.edit()
        self.assert_blocked('Main has changes not included')
        self.assertEqual(self.git(self.main, 'rev-parse', 'HEAD'), target)

    def test_uncommitted_project_changes_are_not_published(self):
        self.edit()
        (self.source / 'auto-sync.ps1').write_text('# unfinished\n', encoding='utf-8')
        self.assert_blocked('Unreviewed project changes')

    def test_committed_project_changes_require_explicit_option(self):
        (self.source / 'README.md').write_text('# Reviewed project change\n', encoding='utf-8')
        self.git(self.source, 'add', 'README.md')
        self.git(self.source, 'commit', '-m', 'Reviewed project change')
        self.edit()
        result = self.publish()
        self.assertEqual(result.returncode, 1)
        self.assertIn('Unreviewed project changes', result.stdout)
        self.assertEqual(self.remote_head(), self.initial)
        self.assert_success(self.publish(None, '-IncludeCommittedProjectChanges'))

    def test_push_rejection_retains_commit_and_retry_publishes_it(self):
        # Disable the fixture's no-hooks setting only for this bare remote.
        self.git(self.remote, 'config', 'core.hooksPath', str(self.remote / 'hooks'))
        hook = self.remote / 'hooks/pre-receive'
        hook.write_text('#!/bin/sh\nexit 1\n', encoding='ascii')
        self.edit()
        failed = self.publish()
        self.assertEqual(failed.returncode, 1, failed.stdout + failed.stderr)
        self.assertIn('Incomplete', failed.stdout)
        target = self.git(self.source, 'rev-parse', 'HEAD')
        self.assertNotEqual(target, self.initial)
        self.assertEqual(self.git(self.main, 'rev-parse', 'HEAD'), target)
        self.assertEqual(self.remote_head(), self.initial)
        hook.unlink()
        self.assert_success(self.publish())
        self.assertEqual(self.remote_head(), target)

    def test_idle_background_worker_does_not_block_worktree_publishing(self):
        with (self.root / 'worker.log').open('w+', encoding='utf-8') as log:
            worker = subprocess.Popen([POWERSHELL, '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File',
                                       str(self.main / 'auto-sync.ps1'), '-IntervalSeconds', '86400'],
                                      cwd=self.main, env=self.env, stdout=log, stderr=subprocess.STDOUT)
            try:
                deadline = time.monotonic() + 15
                while time.monotonic() < deadline:
                    log.seek(0)
                    output = log.read()
                    if 'Checking docs/' in output:
                        break
                    self.assertIsNone(worker.poll(), output)
                    time.sleep(.1)
                else:
                    self.fail('Worker did not start: ' + output)
                self.edit()
                self.assert_success(self.publish())
            finally:
                worker.terminate()
                worker.wait(timeout=10)

    def test_shared_operation_lock_serializes_publish_and_auto_sync(self):
        self.edit()
        marker = self.root / 'build-started'
        self.builder.write_text(
            f'@echo off\r\necho ready> "{marker}"\r\n'
            'powershell.exe -NoProfile -Command "Start-Sleep -Seconds 3"\r\nexit /b 0\r\n',
            encoding='ascii',
        )
        publisher = subprocess.Popen(
            [POWERSHELL, '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File',
             str(self.source / 'publish-notes.ps1'), '-PythonPath', str(self.builder)],
            cwd=self.root, env=self.env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, encoding='utf-8', errors='replace',
        )
        try:
            deadline = time.monotonic() + 15
            while not marker.exists() and time.monotonic() < deadline:
                self.assertIsNone(publisher.poll())
                time.sleep(.05)
            self.assertTrue(marker.exists(), 'Publisher did not reach the build gate')
            started = time.monotonic()
            sync = subprocess.run(
                [POWERSHELL, '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File',
                 str(self.main / 'auto-sync.ps1'), '-Once'],
                cwd=self.main, env=self.env, capture_output=True, text=True,
                encoding='utf-8', errors='replace', timeout=40,
            )
            elapsed = time.monotonic() - started
            stdout, stderr = publisher.communicate(timeout=15)
            self.assertEqual(publisher.returncode, 0, stdout + stderr)
            self.assertEqual(sync.returncode, 0, sync.stdout + sync.stderr)
            self.assertGreater(elapsed, 2, 'Background sync failed to wait for publishing')
            self.assertEqual(self.remote_head(), self.git(self.source, 'rev-parse', 'HEAD'))
        finally:
            if publisher.poll() is None:
                publisher.terminate()
                publisher.communicate(timeout=10)


if __name__ == '__main__':
    unittest.main()
