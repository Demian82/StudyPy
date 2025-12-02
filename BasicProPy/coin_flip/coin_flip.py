def fileIO(fileName):
    with open(fileName, 'r') as f:
        content = f.read()
    
    return content
    

def coin_flip(fileName):
    content = fileIO(fileName)
    word = content.split()
    word = list(map(str.lower, word))
    total = len(word)
    hd = 0
    tl = 0
    for w in word:
        if(w == 'h' or w == 'heads'):
            hd += 1
        else:
            tl += 1
    
    percent = (hd/total)*100

    print(f'{hd} heads ({percent:.0f}%)')
    if (percent >= 50):
        print("You win!")
    else:
        print("You lose!")

coin_flip("coin_flip/HandT.txt")
