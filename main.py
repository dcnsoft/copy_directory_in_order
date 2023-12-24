import os
import shutil
import sys
from time import sleep

def copy_directory_in_order(source, destination):
  # Create the destination directory if it doesn't exist
    if not os.path.exists(destination):
        os.makedirs(destination)

    # Get all entries in the directory sorted alphabetically
    entries = sorted(os.listdir(source))

    for entry in entries:
        full_path = os.path.join(source, entry)
        dest_path = os.path.join(destination, entry)

        if os.path.isdir(full_path):
            # If entry is a directory, recursively copy its contents
            copy_directory_in_order(full_path, dest_path)
        else:
            relativePath = dest_path.replace(destination_directory + "/", "")
            print(f"Copying: {relativePath}")
            # If entry is a file, copy it
            shutil.copy2(full_path, dest_path)
            # sleep(1)


# Check if the correct number of arguments are provided
if len(sys.argv) != 3:
    print("Usage: python main.py <source_directory> <destination_directory>")
    sys.exit(1)

source_directory = sys.argv[1]
destination_directory = sys.argv[2]

# Call the copy function
copy_directory_in_order(source_directory, destination_directory)
