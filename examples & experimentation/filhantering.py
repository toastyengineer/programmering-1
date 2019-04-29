import os

if os.path.exists('./test.txt'):
    f = open('./test.txt', "a")
else:
    f = open('./test.txt', "w")

row = input('Write a line (empty line exits): ')
if "cleanthisbitchassfile" in row:
    f.close()
    f = open('./test.txt', "w")
    row = input("New document created, write line:")
while row:
    f.write(row+'\n')
    row = input('Write a line (empty line exits): ')
f.close()

f = open('./test.txt', "r")
for row in f:
    print(row, end="")
f.close()
