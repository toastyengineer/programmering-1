m = int(input("enter nm 1: "))
n = int(input("enter nm 2: "))

user_input = range(m, n+1)

for numbers in usr_input:
    if numbers < usr_input[-1]:
        print(numbers, end=", ")
    else:
        print(numbers, end=" ")

print()

while m is < n:
