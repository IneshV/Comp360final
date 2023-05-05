# Set the file path to your PE file
path = 'something.exe'

# Initialize the byte count and line list
byte_count = 0
line = []

# Open the file for reading in binary mode
with open(path, 'rb') as file:
    # Read the contents of the file and store them in file_content
    file_content = file.read()

# Iterate through each byte in file_content
for bit in file_content:
    # Increment the byte count by 1
    byte_count +=1
    # Add the byte to the line list
    line.append(bit)
    # Print the byte in hexadecimal format
    print("{0:0{1}x}".format(bit,2),end = " ")
    # If the byte count is a multiple of 16, print a "#" symbol
    if byte_count % 16 == 0:
        print("#", end = "" )
        # Iterate through each byte in the line list
        for b2 in line:
            # If the byte represents a printable character, print the corresponding ASCII character
            if (b2 >= 32) and (b2<=256):
                print(chr(b2),end = "")
        # Reset the line list to an empty list and print a new line character
        line = []
        print()
