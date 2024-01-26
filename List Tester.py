shopping = int(input("How many items do you have? ")) 

words = []

for i in range(shopping): 
    list = input(str("Items: "))

    words = words + [list]

words.sort()

print("Your items are: ", "\n", *words, sep = "\n")
