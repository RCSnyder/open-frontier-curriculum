import subprocess
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class ObeliskValidationTest(unittest.TestCase):
    def test_structural_validator(self):
        proc=subprocess.run([sys.executable,str(ROOT/"scripts"/"validate_obelisk.py")],cwd=ROOT,text=True,capture_output=True,check=False)
        self.assertEqual(proc.returncode,0,proc.stdout+"\n"+proc.stderr)

if __name__=="__main__":
    unittest.main()
