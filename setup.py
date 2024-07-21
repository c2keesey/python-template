import os
import subprocess
import venv

"""
Run this script to setup the project. It will create a virtual environment, add the project path, and install the requirements if present.
"""


def run_command(command):
    subprocess.run(command, shell=True, check=True)


def setup_project():
    if not os.path.exists("venv"):
        print("Creating virtual environment...")
        venv.create("venv", with_pip=True)
    else:
        print("Virtual environment already exists.")

    pth_file = "venv/lib/python3.12/site-packages/root.pth"
    if not os.path.exists(pth_file) or open(pth_file).read().strip() != os.getcwd():
        print("Updating .pth file...")
        with open(pth_file, "w") as f:
            f.write(os.getcwd())
    else:
        print(".pth file already up to date.")

    if os.path.exists("core/requirements.txt"):
        print("Installing requirements...")
        run_command("venv/bin/pip install -r core/requirements.txt")
    else:
        print("No requirements.txt found in core directory")


if __name__ == "__main__":
    setup_project()
