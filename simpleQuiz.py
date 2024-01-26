points = 0 

teamName = input("What is your team name? ")
print(f"welcome to the quiz {teamName} good luck and have fun")

#Question 1
print("Question 1: What is the capital of the United States?")
answerOne = input("Answer: ")
if answerOne == "Washington D.C.":
    points += 1

#Question 2
print("Question 2: From what direction does the sun rise?")
answerTwo = input("Answer: ")
if answerTwo == "East":
    points += 1 

#End of Quiz
print(f"congratulation {teamName} you completed the quiz, you scored a total of {points} in total")