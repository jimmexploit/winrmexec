import runpy
import sys
import os

def main():
    # Find winrmexec.py in the package directory
    pkg_dir = os.path.dirname(__file__)
    script = os.path.join(pkg_dir, "winrmexec.py")
    sys.argv[0] = "winrmexec"
    runpy.run_path(script, run_name="__main__")

if __name__ == "__main__":
    main()
