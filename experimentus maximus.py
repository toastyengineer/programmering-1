
def bill(people, meals, drinks):
    meals = people * meals * 70
    drinks = people * drinks * 30
    total = meals + drinks
    print(total)


def split_bill(total, people):
    split = total / people
    print(round(split*1.1, 2))


def concatenate_strings(string1, string2):
    print(string1 + string2)







#bill(5, 2, 3)
#split_bill(777, 5)
#concatenate_strings("jätte","kul")
