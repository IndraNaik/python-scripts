#!/usr/bin/env python3

import subprocess
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: ./install.py <package_name>")
        sys.exit(1)

    package = sys.argv[1]

    print(f"*************** INSTALLING {package} ******************")

    try:
        subprocess.run(["sudo", "apt-get", "update"], check=True)
        subprocess.run(["sudo", "apt-get", "install", package, "-y"], check=True)
        subprocess.run(["sudo", "systemctl", "start", package], check=True)
        subprocess.run(["sudo", "systemctl", "enable", package], check=True)

        print(f"*************** INSTALLED {package} ******************")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing {package}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
