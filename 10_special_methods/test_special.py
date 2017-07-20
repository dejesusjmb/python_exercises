import unittest
from special import ClassParser


class ParserTest(unittest.TestCase):

    def setUp(self):
        self.input_str = '''
class Class1(object):
    def __init__(self):
        self.name = "Class1"

    def printer(self, args):
        print args
'''
        self.other_str = '''
class Class2(object):
    def __init__(self):
        self.name = "Class2"

    def printer(self, args):
        print args

    def outputter(self, args):
        print args
'''
        self.klass = ClassParser(self.input_str)
        self.other_class = ClassParser(self.other_str)

    def test_class_get_attrib_name(self):
        self.assertEqual(self.klass.name, "Class1")
        self.assertEqual(self.other_class.name, "Class2")

    def test_class_get_attrib_method(self):
        self.assertListEqual(self.klass.methods, ['__init__', 'printer'])
        self.assertListEqual(self.other_class.methods, ['__init__', 'printer', 'outputter'])

    def test_nonexistent_attrib(self):
        self.assertEqual(self.klass.init, "Property does not exist")

    def test_class_get_item(self):
        self.assertEqual(self.klass['__init__'], "self.name = \"Class1\"")
        self.assertEqual(self.klass['printer'], "print args")
        self.assertEqual(self.other_class['__init__'], "self.name = \"Class2\"")
        self.assertEqual(self.other_class['printer'], "print args")
        self.assertEqual(self.other_class['outputter'], "print args")

    def test_klass_should_be_lesser(self):
        self.assertTrue(self.klass < self.other_class)
        self.assertFalse(self.other_class < self.klass)

    def test_other_should_be_greater(self):
        self.assertTrue(self.other_class > self.klass)
        self.assertFalse(self.klass > self.other_class)

    def test_klass_should_be_equal_to_klass(self):
        self.assertTrue(self.klass == self.klass)
        self.assertFalse(self.klass == self.other_class)

    def test_count_property(self):
        self.assertEqual(self.klass.method_count, 2)
        self.assertEqual(self.other_class.method_count, 3)

    def test_string(self):
        self.assertEqual(str(self.klass), "class Class1 with methods __init__, printer")
        self.assertEqual(str(self.other_class), "class Class2 with methods __init__, outputter, printer")

    def test_repr(self):
        self.assertEqual(str([self.klass, self.other_class]),
                         "[{Class1 : [__init__, printer]}, {Class2 : [__init__, outputter, printer]}]")

    def test_add_method_using_key(self):
        self.klass['hello'] = "print \"Hello, world!\""
        self.assertEqual(str(self.klass), "class Class1 with methods __init__, hello, printer")

if __name__ == "__main__":
    unittest.main()
