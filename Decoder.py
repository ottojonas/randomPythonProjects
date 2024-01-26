string = input("Enter the message: ")

stringEncoded = string.encode('utf_16', errors = 'strict')

print("The encoded string is: ", stringEncoded) 

stringDecoded = stringEncoded.decode('utf_16', errors = 'strict')

print("The decoded string is: ", stringDecoded)
