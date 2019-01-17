""" ish
This is a translator for any language,
translates into the ISH language
"""

USER_INPUT = input("Universal Ish Translator\nEnterish yourish wordish hereish: ")
WORD_LIST = USER_INPUT.split()

for word in WORD_LIST:

    if word[-1] == "I" or word[-1] == "i":
        print(word, end=" ")

    elif word[-3:] == "igt":
        new = word.replace("igt", "ish")
        print(new, end=" ")

    elif word[-1] == "?":
        word = word.replace("?", "")
        print(word+"ish?", end=" ")

    elif word[-1] == "!":
        word = word.replace("!", "")
        print(word+"ish!", end=" ")

    elif word[-1] == ",":
        word = word.replace(",", "")
        print(word+"ish,", end=" ")

    elif word[-1] == ".":
        word = word.replace(".", "")
        print(word+"ish.", end=" ")

    else:
        print(word+"ish", end=" ")
