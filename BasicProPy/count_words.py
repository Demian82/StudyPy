def count_words(sentence):
    list = sentence.split()
    word = len(list)
    return word

def main():
    sentence = input()
    print(count_words(sentence))

main()


# def count_words(sentence):
#     if(len(sentence) != 0):
#         if (sentence.find(' ')):
#             word = sentence.count(' ')+1
#         else:
#             word = 1
#     else :
#         word = 0
    
#     return word