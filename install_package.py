#!/bin/python3
import subprocess
import sys

def install_package(package_name):
    try:
        # Update package lists
        subprocess.run(["sudo", "apt", "update"], check=True)
        
        # Install the package
        subprocess.run(["sudo", "apt", "install", package_name ,"-y" ], check=True)
        
        print(f"\n✅ Successfully installed '{package_name}'.")
    except subprocess.CalledProcessError:
        print(f"\n❌ Failed to install '{package_name}'. Please check the package name or your internet connection.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 install_package.py <package-name>")
        sys.exit(1)

    package = sys.argv[1]
    install_package(package)
