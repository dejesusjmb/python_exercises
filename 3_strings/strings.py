def length(x):
    return len(x)

def without(string, toberemoved):
    return ''.join(char for char in string if char not in toberemoved)

def count_distinct(string):
    return len(set(string))

def tokens(string):
    return [entry for entry in string.split('.') if entry != '']
