
def main():

    fileName = input("Input file? ")
    content = fileIO(fileName)
    
    cnd1 = 0
    cnd2 = 0

    for line in content:
        if not line.strip():
            continue

        elect = line.split()

        if(len(elect)<4):
            continue
        
        elect1 = int(elect[1])
        elect2 = int(elect[2])

        if (elect1 > elect2):
            cnd1+=int(elect[3])
        elif (elect1 < elect2):
            cnd2+=int(elect[3])
        else:
            continue
        
    print(f'Candidate 1: {cnd1} votes')
    print(f'Candidate 2: {cnd2} votes')

def fileIO(fileName):
    if not fileName.strip():
            return "polls.txt"
    f = open(fileName)
    content = f.read()
    tokens = content.split('\n')
    return tokens



main()