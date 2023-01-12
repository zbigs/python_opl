def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def mul(x, y):
    return x*y


def div(x, y):
    return x/y

def isnum(x):
    if x.strip().isdigit():
        return float(x)
    else:
        print("Nieprawidlowa liczba")
        return None
