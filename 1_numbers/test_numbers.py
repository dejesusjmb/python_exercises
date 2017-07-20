import unittest
import number


class TestArithmetics(unittest.TestCase):

    def test_add_two_number(self):
        self.assertEqual(number.add(1, 2), 3)
        self.assertEqual(number.add(22, 13), 35)

    def test_multiply(self):
        self.assertEqual(number.multiply(1, 2), 2)
        self.assertEqual(number.multiply(4, 2), 8)

    def test_safe_division(self):
        self.assertEqual(number.safe_division(12, 2), 6)
        self.assertEqual(number.safe_division(4, 0), None)

    def test_add_many(self):
        self.assertEqual(number.add(2, 4, 6, 8), 20)
        self.assertEqual(number.add(1, 2, 3, 4), 10)

    def test_multiply_should_handle_strings(self):
        self.assertEqual(number.multiply('1', '2'), 2)
        self.assertEqual(number.multiply('4', '2'), 8)

    def test_add_two_largest(self):
        self.assertEqual(number.add_two_largest(6, 4, 2, 8), 14)
        self.assertEqual(number.add_two_largest(4, 2, 1, 3), 7)


if __name__ == "__main__":
    unittest.main()
