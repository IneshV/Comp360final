# Import the necessary modules
import os
import pandas as pd

# Set the root directory and create an empty DataFrame with the desired column names
root_directory = "theZoo/malware"
df = pd.DataFrame(columns=["foldername", "md5", "sha"])

# Iterate through each folder in the root directory
for folder_name in os.listdir(root_directory):
    # Get the full folder path
    folder_path = os.path.join(root_directory, folder_name)
    # Check if the folder is actually a directory
    if os.path.isdir(folder_path):
        # Initialize variables to store the MD5 and SHA hashes
        md5_hash = None
        sha_hash = None

        # Iterate through each file in the folder
        for file_name in os.listdir(folder_path):
            # Get the full file path
            file_path = os.path.join(folder_path, file_name)
            # Check if the file starts with "md5" and is a regular file
            if file_name.startswith("md5") and os.path.isfile(file_path):
                # Open the file and extract the MD5 hash
                with open(file_path, "r") as f:
                    md5_hash = f.read().split()[0]
            # Check if the file starts with "sha" and is a regular file
            elif file_name.startswith("sha") and os.path.isfile(file_path):
                # Open the file and extract the SHA hash
                with open(file_path, "r") as f:
                    sha_hash = f.read().split()[0]
        
        # Create a new DataFrame with the folder name, MD5 hash, and SHA hash
        df2 = pd.DataFrame([[folder_name,md5_hash,sha_hash]],columns=["foldername", "md5", "sha"])
        # Concatenate the new DataFrame with the existing DataFrame
        df = pd.concat([df, df2])

# Save the DataFrame as a CSV file called "viruses.csv" in the root directory
df.to_csv("viruses.csv", index=False)
