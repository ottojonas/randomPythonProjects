import secrets
import string 

def createPW(pwlength = 12): 
    letters = string.ascii_letters 
    digits = string.digits 
    special = string.punctuation 

    alphabet = letters + digits + special
    pwd = ""
    pwStrong = False

    while not pwStrong: 
        pwd = ""
        for i in range(pwlength):
            pwd += "".join(secrets.choice(alphabet))

        if (any(char in special for char in pwd) and sum(char in digits for char in pwd) >= 2):
            pwStrong = True

    return pwd 

if __name__ == "__main__": 
    print(createPW())
