

ingredients = int(input("How many ingredients do you want to sort? "))

words = []

for i in range(ingredients):
    numList = i + 1
    colonList = ":"

    list = input(str(numList) + colonList)
    words = words + [list]
    
words.sort()

print(words)
