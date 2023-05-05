# Set the file path
path = "C:\Program Files (x86)\Steam\steam.exe"

# Initialize the byte count and line list
byte_count = 0
line = []

# Initialize the executable flag to False
executable = False

# Open the file for reading in binary mode
with open(path, 'rb') as file:
    # Read the contents of the file and store them in file_content
    file_content = file.read()

# Get the first two bytes of the file in hexadecimal format
bit_one = "{0:0{1}x}".format(file_content[0],2)
bit_two = "{0:0{1}x}".format(file_content[1],2)

# If the first two bytes are "4d" and "5a" respectively, set the executable flag to True
if bit_one=='4d' and bit_two =='5a':
    executable = True
    print('this is an executable file')
