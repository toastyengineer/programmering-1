
def rectangle_area(langd, bredd):
    return abs(langd) * abs(bredd)


def rectangle_omkrets(langd, bredd):
    return 2 * (abs(langd) + abs(bredd))

def rectangle_ratio(langd, bredd):
    if bredd != 0:
        return abs(langd) / abs(bredd)
    else:
        return 0