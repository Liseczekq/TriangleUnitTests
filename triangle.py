def czy_utworzy_trojkat(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False