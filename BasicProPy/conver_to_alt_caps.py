def convert_to_alt_caps(sentance):
    list=[]
    count=1
    for i in range(0, len(sentance)):
        if(sentance[i] != ' '):
            if(count%2 != 0):
                list.insert(i, sentance[i].lower())
                count += 1
            else:
                list.insert(i, sentance[i].upper())
                count += 1
        else:
            list.insert(i, ' ')
    list = ''.join(list)
    return list



# def string_spiter_lower(word):
#     list=word.split()
#     lower_list = [item.lower() for item in list]
#     return lower_list


def main():
    word = input("Input string: ")
    

# main()
convert_to_alt_caps("hello")
convert_to_alt_caps("section is AWESOME")

# list = []
# for i in range(0, len(word)):
#         if(i%2!=0):
#             list.insert(i, word[i].upper())
#         else:
#             list.insert(i, word[i])
#     word = ''.join(list)
#     print(word)

# def convert_to_alt_caps(sentance):
#     list = string_spiter_lower(sentance)
    
#     for i in range(0, len(list)):
#         word = list[i]
#         print(word)
#         wordList = []
#         for j in range(0, len(word)):
#             if(j%2!=0):
#                 wordList.insert(j, word[j].upper())
#             else:
#                 wordList.insert(j, word[j])
#         word = ''.join(wordList)
#         print(word)