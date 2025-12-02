def main():
    fullName = input("Enter your name: ")
    nameBorder(fullName)

def nameBorder(fullName):
    # print the name border pattern with the fullName
    if (fullName.find(" ") == True):
        index = fullName.find(" ")
        
        s1 = fullName[0:index] 
        s2 = fullName[index:]

        for letter in range(0, len(s1)):
            print(s1[letter:])
        for letter in range(0, len(s1)):
            print(s1[:letter+1])

        for letter in range(0, len(s2)):
            print(s2[letter:])
        for letter in range(0, len(s2)):
            print(s2[:letter+1])

    else:
        for letter in range(0, len(fullName)):
            print(fullName[letter:])
        for letter in range(0, len(fullName)):
            print(fullName[:letter+1])

main()