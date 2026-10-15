"""Inspect real Windows task definitions without registering system tasks."""
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
POWERSHELL = shutil.which('powershell.exe')


@unittest.skipUnless(POWERSHELL and shutil.which('git'), 'Requires Windows PowerShell and Git')
class InstallAutoSyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='notes-startup-test-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.main = self.root / 'main notes'
        self.draft = self.root / 'draft notes'
        self.env = dict(os.environ, GIT_TERMINAL_PROMPT='0')
        self.git(self.root, 'init', '--initial-branch=main', str(self.main))
        for key, value in [('user.name', 'Notes Test'), ('user.email', 'test@example.invalid'),
                           ('commit.gpgsign', 'false'), ('core.hooksPath', str(self.root / 'no-hooks'))]:
            self.git(self.main, 'config', key, value)
        for name in ('auto-sync.ps1', 'install-auto-sync.ps1'):
            shutil.copyfile(ROOT / name, self.main / name)
        self.git(self.main, 'add', '.')
        self.git(self.main, 'commit', '-m', 'Fixture')
        self.git(self.main, 'worktree', 'add', '--detach', str(self.draft), 'HEAD')

    def git(self, directory, *args):
        result = subprocess.run(['git', '-C', str(directory), *args], env=self.env,
                                capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=20)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result.stdout.strip()

    def describe(self, directory):
        return subprocess.run([POWERSHELL, '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File',
                               str(directory / 'install-auto-sync.ps1'), '-Describe'],
                              cwd=self.root, env=self.env, capture_output=True, text=True,
                              encoding='utf-8', errors='replace', timeout=20)

    def test_worktree_configuration_targets_main_with_stable_task_identity(self):
        plans = []
        for directory in (self.main, self.draft):
            before = self.git(directory, 'status', '--porcelain')
            result = self.describe(directory)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            plans.append(json.loads(result.stdout))
            self.assertEqual(self.git(directory, 'status', '--porcelain'), before)
        self.assertEqual(plans[0]['TaskName'], plans[1]['TaskName'])
        self.assertRegex(plans[0]['TaskName'], r'^NotesAutoSync-[0-9a-f]{12}$')
        plan = plans[1]
        self.assertEqual(Path(plan['MainDirectory']).resolve(), self.main.resolve())
        self.assertEqual(Path(plan['Action']['WorkingDirectory']).resolve(), self.main.resolve())
        # Git expands Windows 8.3 aliases (RUNNER~1) on hosted runners.
        # Check file identity rather than spelling or case of the path.
        worker_argument = re.search(r'-File "([^"]+)"', plan['Action']['Arguments'])
        self.assertIsNotNone(worker_argument)
        self.assertTrue(Path(worker_argument.group(1)).samefile(self.main / 'auto-sync.ps1'))
        self.assertNotEqual(Path(worker_argument.group(1)).parent.resolve(), self.draft.resolve())
        self.assertIn('-WindowStyle Hidden', plan['Action']['Arguments'])
        self.assertIn('-Unattended', plan['Action']['Arguments'])
        self.assertIn('auto-sync-task.log', plan['Action']['Arguments'])

    def test_task_has_unlimited_runtime_recovery_and_non_admin_identity(self):
        result = self.describe(self.draft)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        plan = json.loads(result.stdout)
        self.assertEqual(plan['Settings']['MultipleInstances'], 2)  # IgnoreNew
        self.assertEqual(plan['Settings']['ExecutionTimeLimit'], 'PT0S')
        self.assertEqual(plan['Settings']['RestartCount'], 3)
        self.assertEqual(plan['Settings']['RestartInterval'], 'PT1M')
        self.assertTrue(plan['Settings']['StartWhenAvailable'])
        self.assertFalse(plan['Settings']['DisallowStartIfOnBatteries'])
        self.assertFalse(plan['Settings']['StopIfGoingOnBatteries'])
        self.assertEqual(plan['Principal']['LogonType'], 3)  # InteractiveToken
        self.assertEqual(plan['Principal']['RunLevel'], 0)  # LeastPrivilege
        triggers = {x['Kind']: x for x in plan['Triggers']}
        self.assertTrue(triggers['MSFT_TaskLogonTrigger']['UserId'].startswith('S-1-'))
        self.assertEqual(triggers['MSFT_TaskTimeTrigger']['Interval'], 'PT5M')
        self.assertFalse(triggers['MSFT_TaskTimeTrigger']['Duration'])

    def test_no_main_worktree_is_reported_without_changes(self):
        self.git(self.main, 'switch', '-c', 'feature/other')
        before = self.git(self.draft, 'status', '--porcelain')
        result = self.describe(self.draft)
        self.assertEqual(result.returncode, 1)
        self.assertIn('No working directory on main', result.stdout)
        self.assertEqual(self.git(self.draft, 'status', '--porcelain'), before)


if __name__ == '__main__':
    unittest.main()
