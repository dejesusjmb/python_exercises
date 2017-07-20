import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from my_time import MyTime


class TestMyTime(unittest.TestCase):

    def test_time_stores_its_value(self):
        # Implement a class called MyTime to which you can pass a string
        # representation of time when creating the object. Also three access
        # methods will be needed.
        time = MyTime('08:56:12')
        self.assertEqual(time.get_hours(), 8)
        self.assertEqual(time.get_minutes(), 56)
        self.assertEqual(time.get_seconds(), 12)

    def test_time_knows_how_to_advance(self):
        # MyTime class needs to have a method called 'advance'.
        time = MyTime('23:30:50')
        time.advance(hours=3, minutes=4, seconds=6)
        self.assertEqual(time.get_hours(), 2)
        self.assertEqual(time.get_minutes(), 34)
        self.assertEqual(time.get_seconds(), 56)

    def test_time_instances_can_be_compared(self):
        # Implement 'is_less_than' method to be able to compare different
        # instances of MyTime class.
        time_small = MyTime('08:20:02')
        time_large = MyTime('08:22:02')
        self.assertTrue(time_small.is_less_than(time_large))

    def test_time_knows_how_to_string(self):
        # Now we need to get a string representation of MyTime content.
        time = MyTime('12:23:34')
        self.assertEqual(time.to_string(), "12:23:34")


if __name__ == '__main__':
    unittest.main()
