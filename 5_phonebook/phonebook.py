import re
book = {}

class InvalidInputException(Exception):
    pass

class NameAlreadyInPhonebookError(Exception):
    pass

class NameNotExistError(Exception):
    pass

def add(name, number):
    if name in book.keys():
        raise NameAlreadyInPhonebookError("Name already in phonebook")
    _check_valid_number(number)
    _check_valid_name(name)
    book[name] = number
    return True


def _check_valid_number(number):
    if number.isdigit() and len(number) == 11:
        return True
    else:
        raise InvalidInputException("Invalid number")
    # return re.match(r"\+?[\d ]+$", number)


def _check_valid_name(name):
    if name.isalpha():
        return True
    else:
        raise InvalidInputException("Invalid name")
    # return re.match(r"[\w ]+$", name)


def get(name):
    if name in book:
        return book[name]
    else:
        raise NameNotExistError


def clear():
    book.clear()


def serialize():
    result = ""
    for name in sorted(book.keys()):
        result += "{}={}\n".format(name, book[name])
    return result


def deserialize(content):
    for line in content.splitlines():
        name, number = line.split("=")
        add(name, number.strip())


def save(filename):
    with open(filename, "w") as outfile:
        outfile.write(serialize())


def load(filename):
    with open(filename, "r") as infile:
        deserialize(infile.read())
