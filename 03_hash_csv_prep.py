# Import the os module
import os

# Set the root directory
root_directory = "/path/to/theZoo"

# Iterate through each folder in the root directory
for folder_name in os.listdir(root_directory):
    # Get the full folder path
    folder_path = os.path.join(root_directory, folder_name)
    # Check if the folder is actually a directory
    if os.path.isdir(folder_path):
        # Iterate through each file in the folder
        for file_name in os.listdir(folder_path):
            # Get the full file path
            file_path = os.path.join(folder_path, file_name)
            # Check if the file does not end with ".zip"
            if not file_name.endswith(".zip"):
                # Create a new file name by appending ".txt" to the end of the file name
                new_file_name = file_name + ".txt"
                # Create the full path for the new file
                new_file_path = os.path.join(folder_path, new_file_name)
                # Rename the old file to the new file name
                os.rename(file_path, new_file_path)
