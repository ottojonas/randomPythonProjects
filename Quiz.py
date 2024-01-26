teamName = input("What is your team name? ")
print("Welcome to the game, " + teamName + "You will get points for each question that you get right! Good Luck and have fun!")

score = points = 0 

#Question 1
print("Question 1: What is the capital of the United States?")
answerOne = input("Answer: ")
if answerOne == "Washington D.C.":
    print("Correct! You got a point!")
    points = points + 1

else:
    print("Sorry, that answer is wrong. The answer was Washington D.C.")
    points = points + 0 

pointsTotal = points
#Question 2
print("Question 2: From what direction does the sun rise?")
answerTwo = input("Answer: ")

if answerTwo == "East":
    print("Correct! You got a point!")
    points = points + 1 

else:
    print("Sorry, that answer is wrong. The answer was East")
    points = points + 0 

pointsTotal = points

#End of Quiz
print("Congratlations", teamName,"! You completed the quiz")
finalPoints = pointsTotal 
print("You managed to get", finalPoints, "points in total!")