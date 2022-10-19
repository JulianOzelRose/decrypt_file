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

    for i in range(len(line)):
        char = line[i]
        if char.isupper():
            plainTxt += chr((ord(char) - distance - 65) % 26 + 65)
        else:
            plainTxt += chr((ord(char) - distance - 97) % 26 + 97)

inputFile.close()
print(plainTxt)