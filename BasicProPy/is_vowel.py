def is_vowel(letter):
    vowels = [ 'a', 'e', 'i', 'o', 'u']
    count = 0
    if (len(letter) > 1):
        return False
    else:
        letter = letter.lower()
        for j in range(0, len(vowels)):
            if (letter == vowels[j]):
                count+=1
    if (count != 0):
        return True
    else:
        return False
        

is_vowel("e")

