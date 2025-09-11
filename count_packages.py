#!/bin/python3
import subprocess
import shutil
import sys

def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        return output.strip()
    except subprocess.CalledProcessError:
        return None

def get_installed_package_count():
    if shutil.which("dpkg"):
        # Debian/Ubuntu
        output = run_command("dpkg -l | grep '^ii' | wc -l")
        return int(output), "dpkg (Debian/Ubuntu)"
    
    elif shutil.which("rpm"):
        # Red Hat/Fedora
        output = run_command("rpm -qa | wc -l")
        return int(output), "rpm (Red Hat/Fedora/CentOS)"
    
    elif shutil.which("pacman"):
        # Arch Linux
        output = run_command("pacman -Q | wc -l")
        return int(output), "pacman (Arch Linux)"
    
    else:
        return None, "Unsupported or unknown package manager"

def main():
    count, manager = get_installed_package_count()
    if count is not None:
        print(f"Number of installed packages: {count} (using {manager})")
    else:
        print("Could not detect supported package manager.", file=sys.stderr)

if __name__ == "__main__":
    main()
