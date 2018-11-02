def repeat(item, times):
    output = []
    while times > 0:
        output.append(item)
        times -= 1
    return output


print(repeat("5", 3))