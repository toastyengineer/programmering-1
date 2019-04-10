from decimal import getcontext, Decimal

precision = int(input("Enter Precision: "))
getcontext().prec = precision+1

MAX = 5000


def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + a
    return a


f = [Decimal(0), Decimal(1), Decimal(1), Decimal(2)]
for x in range(2, MAX):
    f.append(Decimal(fibonacci(x)))
    if f[-1]/f[-2] == f[-2]/f[-3]:
        print(f[-1] / f[-2])
        print(f"""Required {len(f)} numbers from the fibonacci series to achieve approximation
accurate to {precision} decimal places""")
        break

