# Write a python code print os modele and list all files in dorectory
import os

# Specify the directory you want to list
directory_path = '/'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Prints each file and direcctory name
for item in contents:
    print(item)