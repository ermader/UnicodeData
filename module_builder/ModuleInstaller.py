"""/
ModuleInstaller. Install generated files

Created on June 1, 2021

@author Eric Mader
"""

from sys import argv, exit, stderr
import shutil
from pathlib import Path

def install():
    sourcePath = Path(argv[1])  # Might want an actuall argument scanner?
    destPath = Path("UnicodeData")

    for pythonFile in sourcePath.glob("*.py"):
        shutil.copy2(pythonFile, destPath)

    shutil.copy2(sourcePath / "icudata.dat", destPath / "Data")

if __name__ == "__main__":
    install()
