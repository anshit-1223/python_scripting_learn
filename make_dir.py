#Python script to make directory

#!/bin/python3
import os

directory_name = input("Enter Directory Name : ")

if not os.path.exists(directory_name):
    os.makedirs(directory_name)
    print(f"Directory '{directory_name}' created.")
else:
    print(f"Directory '{directory_name}' Already Exists.")





