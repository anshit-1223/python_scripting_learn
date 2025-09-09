#!/bin/python3
import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, check=True)
        print(f"✅ Successfully ran: {' '.join(command)}")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to run: {' '.join(command)}")
        sys.exit(1)

def update_and_upgrade():
    print("🔄 Updating package lists...")
    run_command(["sudo", "apt", "update"])

    print("\n⬆️ Upgrading packages...")
    run_command(["sudo", "apt", "upgrade", "-y"])

    print("\n🎉 System is up to date!")

if __name__ == "__main__":
    update_and_upgrade()
