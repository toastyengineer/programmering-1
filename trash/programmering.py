
age = input("What is your age? ")
print("You are "+age+" years old.")

def print_age():
    if int(float(age)) <= 0:
        print("You can not exist.")
    elif int(float(age)) >= 19:
        print("You are also an adult.")
    elif int(float(age)) < 13:
        print("You are also a child.")
    elif int(float(age)) >= 13 < 19:
        print("You are also a teenager.")
    else:
        print("age error")

print_age()