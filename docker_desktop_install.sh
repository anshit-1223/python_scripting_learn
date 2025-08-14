#!/bin/bash
#set -e
check_root=$(echo $EUID)
if [ $check_root -ne 0 ]; then
    echo "Run with sudo!!"
    exit 1
fi

echo "Download Docker Desktop"
wget -O docker-desktop-amd64.deb "https://desktop.docker.com/linux/main/amd64/docker-desktop-amd64.deb?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-linux-amd64&_gl=1*mega3h*_ga*NDg0OTU2MDU0LjE3NTk2NzIyMjU.*_ga_XJWPQMJYHQ*czE3NjkyNjc5MjgkbzUkZzEkdDE3NjkyNjc5NDQkajQ0JGwwJGgw"; 
echo "Installing required dependencies"
sudo apt update
sudo apt install -y qemu-system-x86 pass uidmap
echo "Installing Docker Desktop"
sudo dpkg -i docker-desktop-amd64.deb;
sudo dpkg --configure -a
if [ $? -eq 0 ]; then
        echo "Installed Docker Desktop Successfully"
else
    echo "Failed !!"
fi
