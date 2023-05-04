#first install 7zip by typing: brew install p7zip
# into your terminal

import subprocess
import csv
import os


disk_path = 'AdobeConnect2019.5.1.dmg'

# Run the command and capture the output


result = str(subprocess.run(['7z', 'l',disk_path], capture_output=True, text=True))

'''
def get_table_data(text):
    table_data = text.split('-------------------')
    return table_data[2][7:]



result = get_table_data(result)

lines = result.split("\n")

# Create a CSV writer object
csv_writer = csv.writer(open("output.csv", "w"))

# Write the header row to the CSV file
csv_writer.writerow(["Date", "Time", "Attr", "Size", "Compressed", "Name"])

# Write each line of the text to the CSV file
for line in lines:
    print(line)
    parts = line.split()
    csv_writer.writerow(parts)
'''


with open(file_full_path, "w") as f:
    f.write(result)

# Print the output
