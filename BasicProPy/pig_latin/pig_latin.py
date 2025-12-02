VOWELS = 'aeiou'

def fileIO(fileName):
    f = open(fileName)
    content = f.read()
    
    return content

def pig_latin(fileName):
    content = fileIO(fileName)
    content = content.splitlines()
    
    newLine = []

    for line in content:
        changeLine = []
        word = line.split()
        for w in word:
            f_letter = w[0]
            if f_letter in VOWELS:
                changeWord = w + 'yay'
            else:
                changeWord = w[1:] + f_letter + 'ay'
            changeLine.append(changeWord)
        newLine.append(' '.join(changeLine))
        print(' '.join(changeLine))




pig_latin("pig_latin/lincoln.txt")
