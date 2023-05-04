path = 'AdobeConnect2019.5.1.dmg'
byte_count = 0
line = []

with open(path, 'rb') as file:
    # Read the contents of the file and convert it to hexadecimal
    file_content = file.read()


for bit in file_content:
    byte_count +=1
    line.append(bit)
    print("{0:0{1}x}".format(bit,2),end = " ")
    if byte_count % 16 == 0:
        print("#", end = "" )
        for b2 in line:
            if (b2 >= 32) and (b2<=256):
                print(chr(b2),end = "")
        line = []
        print()