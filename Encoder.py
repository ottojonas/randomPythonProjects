import base64

string = input("Enter the message: ")

string = base64.b64encode(string.encode('utf-8', errors = 'strict'))

print(string)
