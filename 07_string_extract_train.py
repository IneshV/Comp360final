# import necessary modules
import subprocess
import os

# define the file paths for the folders containing malicious and safe strings
malicious_folder_path = 'malicious_string_folder'
safe_folder_path =  'safe_strings_folder'

# prompt the user to input the path for the PE file
pe_file_path = str(input('please type in your folder path'))

# set up variables for the while loop
x = True
important_info = []

# list of flags that might indicate malicious activity in the strings
flag_list = ['https','HTTP','uninstall','numer','Post','%s','Software']

# while loop to determine if the file is malicious or not
while x:
    boolian = str(input('Is this a virus or not? Answer y if it is a virus or n if not'))
    if boolian == 'y':
        x = False
        folder_path = malicious_folder_path
    if boolian == 'n':
        x = False
        folder_path = safe_folder_path

# run the 'strings' command on the specified file path and capture the output
result = subprocess.run(['strings', '-a', '-n', '-6', '-noverify', pe_file_path], capture_output=True)

# check if there was an error with the 'strings' command and print an error message if so
if result.returncode != 0:
    print(f"Error: Failed to extract from pe file {pe_file_path}")
else:
    # iterate through the output of the 'strings' command and add any lines containing a flag from the flag_list to the important_info list
    for line in result:
        if any(flag in line for flag in flag_list):
            important_info.append(line)

    # create a file path for the new sample file based on the folder path and the current number of files in the folder
    path = folder_path + str(len(os.listdir(folder_path)))+'_sample'

    # write the contents of the important_info list to the new sample file
    with open(path, 'w') as file:
        for item in important_info:
            file.write(item)
