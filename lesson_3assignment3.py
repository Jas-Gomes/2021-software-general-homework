from typing import cast

x = 1
translation = {}

while x == 1:
    ring = input("Please enter a word, or press enter to end: ")
    if ring == "" :
        print("bye, bye")
        break
    if " " in ring:
        print("You cannot enter spaces")
        print("bye, bye")
        break
    if ring in translation.keys():
        print("Key already esists")
        print("bye, bye")
        break
    cat = input("Please enter the word's translation: ")
    translation[ring] = cat
    
print(translation)

