import subprocess
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
class RepoTest(unittest.TestCase):
    def test_shebang_scripts_have_executable_git_modes(self):
        records = subprocess.check_output(
            ["git", "ls-files", "--stage", "-z", "scripts"], cwd=ROOT, text=True)
        for record in records.split("\0"):
            if not record:
                continue
            metadata, relative = record.split("\t", 1)
            if (ROOT / relative).read_bytes().startswith(b"#!"):
                self.assertEqual(metadata.split()[0], "100755", relative)

    def test_repo(self):
        p=subprocess.run([sys.executable,str(ROOT/'scripts'/'validate_repo.py')],cwd=ROOT,text=True,capture_output=True,check=False)
        self.assertEqual(p.returncode,0,p.stdout+'\n'+p.stderr)
if __name__=='__main__': unittest.main()
