
user_input = input("Enterish yourish wordish hereish: ")
word_list = user_input.split()

for word in word_list:

    if word[-1] == "I" or word[-1] == "i":
        print(word, end=" ")

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