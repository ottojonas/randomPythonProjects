import random 

if __name__ == "__main__": 
    score = int('0')
    for i in range(10): 

        userChoice = input('Enter your choice') 
        
        num = random.randint(1,2) 

        if num == 1: 
            result= 'heads'
        
        else: 
            result = 'tails'

        if result == 'heads': 
            if userChoice == result: 
                print('Congrats you got it right') 
                score = score + 1
            else: 
                print('It was heads you were wrong') 

        if result == 'tails': 
            if userChoice == result: 
                print('Congrats you got it right') 
                score = score + 1 
            else: 
                print('It was tails you were wrong') 

    print('Thank you for playing, you got', str(score), 'correct guesses') 