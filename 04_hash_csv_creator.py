import os
import pandas as pd

root_directory = "theZoo/malware"
df = pd.DataFrame(columns=["foldername", "md5", "sha"])

for folder_name in os.listdir(root_directory):
    folder_path = os.path.join(root_directory, folder_name)
    if os.path.isdir(folder_path):
        md5_hash = None
        sha_hash = None

        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if file_name.startswith("md5") and os.path.isfile(file_path):
                with open(file_path, "r") as f:
                    md5_hash = f.read().split()[0]
            elif file_name.startswith("sha") and os.path.isfile(file_path):
                with open(file_path, "r") as f:
                    sha_hash = f.read().split()[0]
        df2 = pd.DataFrame([[folder_name,md5_hash,sha_hash]],columns=["foldername", "md5", "sha"])
        df =pd.concat([df, df2])
df.to_csv("viruses.csv", index=False)
