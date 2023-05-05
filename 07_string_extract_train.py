import subprocess
import os

malicious_folder_path = 'malicious_string_folder'
safe_folder_path =  'safe_strings_folder'

pe_file_path = str(input('please type in your folder path'))

x = True
important_info = []

#%s is for info being sent to virus person
flag_list = ['https','HTTP','uninstall','numer','Post','%s','Software']

while x:
    boolian = str(input('Is this a virus or not? Answer y if it is a virus or n if not'))
    if boolian == 'y':
        x = False
        folder_path = malicious_folder_path
    if boolian == 'n':
        x = False
        folder_path = safe_folder_path



result = subprocess.run(['strings', '-a', '-n', '-6', '-noverify', pe_file_path], capture_output=True)

if result.returncode != 0:
    print(f"Error: Failed to extract from pe file {pe_file_path}")
else:
    for line in result:
        if any(flag in line for flag in flag_list):
            important_info.append(line)


    path = folder_path + str(len(os.listdir(folder_path)))+'_sample'

    with open(path, 'w') as file:
        for item in important_info:
            file.write(item)
