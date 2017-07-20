def read(filename):
    with open(filename) as f:
        return f.read()

def contains(word, filename):
    return word in read(filename)

def file_rows_startingwith(word, filename):
    return ''.join([line+'\n' for line in read(filename).splitlines() if word in line])
