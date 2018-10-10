#line spacing
print("\n\n")

def multiplicator(n, m):
    for numbers in range(1, 11):
        if numbers < 10:
            print(int(n) * numbers, end=", ")
        else:
            print(int(n) * numbers, end="\n")
    for numbers in range(1, 11):
        if numbers < 10:
            print(int(m) * numbers, end=", ")
        else:
            print(int(m) * numbers, end=" ")


user_inputn = input("Enter first number: ")
print()

user_inputm = input("Enter second number: ")
print("\n")

multiplicator(user_inputn, user_inputm)

#line spacing
print("\n\n")