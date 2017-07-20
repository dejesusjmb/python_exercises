def sort(*args):
    return sorted(args)

def find_largest_value(*args):
    return sorted([int(x) for x in args])[-1]

def only_positives(*args):
    return [i for i in args if i > 0]
