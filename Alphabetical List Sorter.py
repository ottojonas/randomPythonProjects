shopping = int(input("How many words do you want to sort? "))

words = []

for i in range(shopping): 
    numList = i + 1
    colonList = ":"


    list = input(str(numList) + colonList)
    words = words + [list]
    
words.sort()

print("Your items are: ", "\n", *words, sep = "\n")

#Works as intended 

