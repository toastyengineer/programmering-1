m = int(input("enter nm 1: "))
n = int(input("enter nm 2: "))


for inputs in range(m, n+1):
    for factor in range(1, 11):
        if inputs*factor < 10:
            print(end=" ")
        if factor < 10:
            print(inputs*factor, end=", ")
        else:
            print(inputs*factor, end="\n")

print()
