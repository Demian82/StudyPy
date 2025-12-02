import random
import math

def main():
    playCount = 0
    totalGuess = 0
    print("This program is a 2-D guessing game.")
    print("I will think of a point somewhere")
    print("between (1, 1) and (100, 100)")
    print("and give hints until you guess it.")

    while(1):
        answerPoint = makePoint()
        totalGuess+=play(answerPoint)
        again = playAgain()
        if (again == True):
            playCount += 1
        else:
            playCount += 1
            break
    
    print("\nOverall results:")
    print(f'Games played  = {playCount}')
    print(f'Total guesses = {totalGuess}')
    print(f"Guesses/game  = {totalGuess/playCount:.1f}")



def distance(x1, x2, y1, y2):
    dtnc = round(math.sqrt((x1-x2)**2 + (y1-y2)**2), 2)
    return dtnc

def directionX(x1, x2):
    if (x2 < x1):
        return "east"
    elif (x2 > x1):
        return "west"
    else:
        return None

def directionY(y1, y2):
    if (y2 < y1):
        return "north"
    elif (y2 > y1):
        return "south"
    else:
        return None

def makePoint():
    x1 = random.randint(1, 100)
    y1 = random.randint(1, 100)
    point = [x1, y1]
    return point

def play(answer):
    guessCount = 1
    aX = answer[0]
    aY = answer[1]

    print("")
    while(1):
        gX, gY= map(int, input("Guess x and y: ").split())

        dist = distance(aX, gX, aY, gY)
        if (aX == gX and aY == gY):
            if (guessCount == 1):
                print(f"You got it right in {guessCount} guess!")
            else:
                print(f"You got it right in {guessCount} guesses!")
            break
        else:
            drX = directionX(aX, gX)
            drY = directionY(aY, gY)
            if(aX == gX):
                if (dist <= 1.5):
                    print(f"You're hot! Go {drY}")
                elif (dist <= 5.0):
                    print(f"You're warm. Go {drY}")
                else:
                    print(f"You're cold. Go {drY}")
            elif(aY == gY):
                if (dist <= 1.5):
                    print(f"You're hot! Go {drX}")
                elif (dist <= 5.0):
                    print(f"You're warm. Go {drX}")
                else:
                    print(f"You're cold. Go {drX}")
            else:
                if (dist <= 1.5):
                    print(f"You're hot! Go {drY} {drX}")
                elif (dist <= 5.0):
                    print(f"You're warm. Go {drY} {drX}")
                else:
                    print(f"You're cold. Go {drY} {drX}")
            guessCount += 1
    
    return guessCount

def playAgain():
    playAgainAnswer = str.lower(input("Play again? "))
    if (playAgainAnswer[0] == 'y'):
        return True
    else:
        return False





main()