#!/bin/python3
import shutil
import os

def delete_directory():
    path = input("Enter the path of the directory to delete: ").strip()

    if os.path.exists(path) and os.path.isdir(path):
        confirm = input(f"Are you sure you want to delete '{path}' and all its contents? (yes/no): ").strip().lower()
        if confirm == 'yes':
            try:
                shutil.rmtree(path)
                print(f"Directory '{path}' deleted successfully.")
            except Exception as e:
                print(f"Error deleting directory '{path}': {e}")
        else:
            print("Deletion cancelled.")
    else:
        print(f"Directory '{path}' does not exist or is not a valid directory.")

# Run the function
delete_directory()