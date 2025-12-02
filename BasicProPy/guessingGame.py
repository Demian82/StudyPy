import random

def main():
    playCount = 0
    totalGuess = 0
    bestGame = []
    guess = 0
    print("This program allows you to guess random numbers.")
    print("I will think of a number between 1 and 100")
    print("and you will try to guess it.")
    print("After each guess, I will give you a clue about")
    print("whether the correct number is higher or lower.")

    while(1):
        answerPoint = makePoint()
        guess = play(answerPoint)
        bestGame.append(guess)
        totalGuess+=guess
        again = playAgain()

        if (again == True):
            playCount += 1
        else:
            playCount += 1
            break
    
    print("\nOverall results:")
    print(f'Total games   = {playCount}')
    print(f'Total guesses = {totalGuess}')
    print(f"Guesses/game  = {totalGuess/playCount:.1f}")
    print(f"Best game     = {min(bestGame)}")


def makePoint():
    point = random.randint(1, 100)
    return point

def play(answer):
    guessCount = 1
    aPoint = answer

    print("\nI'm thinking of a number between 1 and 100...")
    while(1):
        gPoint=int(input("Your guess? "))

        if (aPoint == gPoint):
            if (guessCount == 1):
                print(f"You got it right in {guessCount} guess!")
            else:
                print(f"You got it right in {guessCount} guesses!")
            break
        elif (aPoint < gPoint):
            print("It's lower.")
        else:
            print("It's higher.")
                
        guessCount += 1
    
    return guessCount

def playAgain():
    playAgainAnswer = str.lower(input("Do you want to play again? "))
    if (playAgainAnswer[0] == 'y'):
        return True
    else:
        return False



main()