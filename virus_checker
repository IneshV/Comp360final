import hashlib
import csv
import os

# Define the zip file path and name
zip_path = "path/to/zip"

# Calculate the MD5 hash of the file
md5_hash = hashlib.md5()
sha256_hash = hashlib.sha256()

with open(zip_full_path, "rb") as f:
    while chunk := f.read(8192):
        md5_hash.update(chunk)
        sha256_hash.update(chunk)

# Convert the hash values to hexadecimal strings
md5_hex = md5_hash.hexdigest()
sha256_hex = sha256_hash.hexdigest()

virus = 0
# Read the data from the CSV file
with open("data.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["md5"] == md5_hex or row["sha"]==sha256_hex:
            virus = 1

if virus = 1:
    print('WARNING: This is a virus')
else:
    print('This is NOT a virus')
