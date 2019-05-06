def div(a, b):
    try:
        d = a/b
    except ZeroDivisionError:
        d = 0
    finally:
        return d


print(div(5, "4"))