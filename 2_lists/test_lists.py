import unittest
import lst


class TestLists(unittest.TestCase):

    def test_sort_list(self):
        self.assertEquals(lst.sort(2, 1, 3, 7), [1, 2, 3, 7])
        self.assertEquals(lst.sort(2, -7), [-7, 2])

    def test_find_largest_value(self):
        self.assertEquals(lst.find_largest_value(2, 1, 3, 7), 7)
        self.assertEquals(lst.find_largest_value('2', '1', '3', '7'), 7)
        self.assertEquals(lst.find_largest_value(2, '1', '3', 7), 7)

    def test_only_positives(self):
        self.assertEquals(lst.only_positives(2, -1, 3, -7), [2, 3])
        self.assertEquals(lst.only_positives(20, 1, -63, -7), [20, 1])
        self.assertEquals(lst.only_positives(-12, 4, -3, 5), [4, 5])


if __name__ == "__main__":
    unittest.main()
