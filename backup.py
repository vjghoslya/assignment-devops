import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, destination_dir):
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: The source directory {source_dir} does not exist.")
        return

    # Check if the destination directory exists, if not, create it
    if not os.path.exists(destination_dir):
        print(f"Warning: The destination directory {destination_dir} does not exist. Creating it.")
        os.makedirs(destination_dir)

    # Loop through each file in the source directory
    for file_name in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file_name)

        # Skip if it’s a folder (we only want files)
        if os.path.isdir(source_file):
            continue

        destination_file = os.path.join(destination_dir, file_name)

        # If the file already exists in the destination, add a timestamp to make it unique
        if os.path.exists(destination_file):
            base_name, extension = os.path.splitext(file_name)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            destination_file = os.path.join(destination_dir, f"{base_name}_{timestamp}{extension}")

        try:
            # Copy the file to the destination
            shutil.copy2(source_file, destination_file)
            print(f"Copied: {file_name} to {destination_file}")
        except Exception as e:
            print(f"Error copying {file_name}: {e}")

# Main part of the script
if __name__ == "__main__":
    # Make sure the user provides both source and destination directories
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
    else:
        source_directory = sys.argv[1]
        destination_directory = sys.argv[2]
        backup_files(source_directory, destination_directory)