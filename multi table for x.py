#line spacing
print("\n\n")

def multiplicator(n):
    for numbers in range(1, 11):
        if numbers < 10:
            print(int(n) * numbers, end=", ")
        else:
            print(int(n) * numbers, end=" ")


user_input = input("Enter number to preview its multiplication table: ")
multiplicator(user_input)

#line spacing
print("\n\n")