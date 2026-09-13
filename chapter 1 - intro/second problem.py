import os

# Specify the directory path
path = input("new folder ")

# Check if the directory exists
if os.path.isdir(path):
    print("Contents of the directory:")
    for item in os.listdir(path):
        print(item)
else:
    print("new folder")