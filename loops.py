
for n in range(20, 5, -2):
    print(n, end=", ")
print("\n")

for chars in "Hej du glade!":
    print(chars, end=" ")
print("\n")

def find_coordinate(inx, iny, inz):
    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):
                if x == inx and y == iny and z == inz:
                    print("Found coordinate ", inx,":", iny,":", inz)
                else:
                    exit("coordinate out of bounds")

x = int(input("Enter coordinates X-Axis: "))
y = int(input("Enter coordinates Y-Axis: "))
z = int(input("Enter coordinates Z-Axis: "))
find_coordinate(x, y, z)