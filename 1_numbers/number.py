def add(*args):
    return sum(args)

def multiply(x, y):
    return int(x)*int(y)

def safe_division(x, y):
    return x/y if y != 0 else None

def add_two_largest(*args):
    return sum(sorted(args)[-2:])
