path = "C:\Program Files (x86)\Steam\steam.exe"
byte_count = 0
line = []

executable = False

with open(path, 'rb') as file:
    # Read the contents of the file and convert it to hexadecimal
    file_content = file.read()

i =0

bit_one = "{0:0{1}x}".format(file_content[0],2)
bit_two = "{0:0{1}x}".format(file_content[1],2)


if bit_one=='4d' and bit_two =='5a':
    print('this is an executable file')

