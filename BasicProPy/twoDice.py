import random
SENTIAL = 7

def combineToDice():
    count = 0
    while(1):
        first = random.randrange(1, 6, 1)
        sec = random.randrange(1, 6, 1)
        sum = first + sec
        count += 1
        print(f"{first} + {sec} = {sum}")
        if (sum == SENTIAL):
            print(f"You won after {count} tries!")
            break

# combineToDice()

def play():
    score = 0
    incorrect = 0
    
    while(1):
        correct = 0
        times = random.randrange(2, 5)
        for i in range(1, times+1):
            num = random.randint(1, 10)
            correct += num
            print(num, end='')
            if (i == times):
                print(" = ", end='')
            else:
                print(" + ", end='')
                continue
        answer = int(input())
        if (answer == correct):
            score += 1
        else:
            incorrect += 1
            print(f"Wrong! The andswer was {correct}")
            if (incorrect >= 3):
                break
    print(f"You earned {score} total points")

play()
            

