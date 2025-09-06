#!/bin/python3
import os
import socket
print("Python Scritping Starts...")
print(os.getlogin(),"@",socket.gethostname(),"you are using",socket.getfqdn())
print()