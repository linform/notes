"""Run the dependency-free browser lifecycle checks in the regular test suite."""
from pathlib import Path
import shutil
import subprocess
import unittest


NODE = shutil.which('node')
ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(NODE, 'Node.js is unavailable; run tests/test_mathjax_lifecycle.js in the build job')
class MathJaxLifecycleTests(unittest.TestCase):
    def test_initial_load_and_instant_navigation(self):
        result = subprocess.run(
            [NODE, '--test', str(ROOT / 'tests/test_mathjax_lifecycle.js')],
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding='utf-8',
            timeout=20,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
