
import os
root_directory = "/path/to/theZoo"

for folder_name in os.listdir(root_directory):
    folder_path = os.path.join(root_directory, folder_name)
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if not file_name.endswith(".zip"):
                new_file_name = file_name + ".txt"
                new_file_path = os.path.join(folder_path, new_file_name)
                os.rename(file_path, new_file_path)
