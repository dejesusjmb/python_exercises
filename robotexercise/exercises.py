def log_name(firstname=None, lastname=None):
    pass


def multiply(multiplicand, multiplier):
    return str(int(multiplicand) * int(multiplier))


def should_be_positive(num):
    if int(num) <= 0:
        raise Exception('{} is not positive'.format(num))


def all_should_be_positive(*args):
    negatives = [x for x in args if '-' in x]
    if len(negatives):
        raise Exception('Not positive values: {}'.format(''.join(negatives)))


def open_temporary_file(filename):
    return open(filename, 'w')


def write_from_a_to_z(file_descriptor):
    file_descriptor.write('abcdefghijklmnopqrstuvwxyz')


def close_file(file_descriptor):
    file_descriptor.close()


def file_should_have_letters_from_a_to_z(filename):
    file_descriptor = open(filename, 'r')
    content = file_descriptor.readlines()
    file_descriptor.close()
    if 'abcdefghijklmnopqrstuvwxyz' not in content:
        raise Exception('string not found!')

