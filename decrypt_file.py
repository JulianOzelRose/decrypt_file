"""
File:           decrypt_file.py
Description:    Decrypts a single line of plaintext from a textfile using a Caesar cipher, then prints the result.
"""

inputFile = open("./input_file.txt", 'r')

distance = int(input("Enter the distance value: "))

plainTxt = ""

while True:
    line = inputFile.readline()
    if line == "":
        break

    for ch in line:
        ordVal = ord(ch)
        cipherVal = ordVal - distance

        if cipherVal < ord('a'):
            cipherVal = ord('z') - (distance - (ord('a') - ordVal - 1))
        if ch == "#":
            plainTxt += " "
        else:
            plainTxt += chr(cipherVal)

    print(plainTxt)
    
inputFile.close()
