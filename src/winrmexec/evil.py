import runpy
import sys
import os

def main():
    pkg_dir = os.path.dirname(__file__)
    script = os.path.join(pkg_dir, "evil_winrmexec.py")
    sys.argv[0] = "evil-winrmexec"
    runpy.run_path(script, run_name="__main__")

if __name__ == "__main__":
    main()
