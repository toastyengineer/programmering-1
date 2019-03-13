array = [5, 2, 1, 3, 24, 15, 1565, 36, 23, 76, 23, 74, -2, -5.12]

for outer in range(len(array)-1, 0, -1):
    for inner in range(outer):
        if array[inner] > array[inner + 1]:
            temp = array[inner]
            array[inner] = array[inner + 1]
            array[inner + 1] = temp

print(array)
