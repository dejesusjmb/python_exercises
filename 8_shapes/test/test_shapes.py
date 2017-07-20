import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from shapes import Circle, Rectangle, Triangle, sum_area_of_shapes


class TestShapes(unittest.TestCase):

    def test_circle_object_returns_its_area(self):
        circle = Circle(2)
        self.assertAlmostEqual(circle.get_area(), 12.57, 2)

    def test_rectangle_area(self):
        rectangle = Rectangle(2, 4)
        self.assertEqual(rectangle.get_area(), 8)

    def test_triangle_area(self):
        triangle = Triangle(5, 5)
        self.assertAlmostEqual(triangle.get_area(), 12.5)

    def test_sum_area_of_shapes(self):
        shapes = [Circle(2), Rectangle(2, 4), Triangle(5, 5)]
        self.assertAlmostEqual(sum_area_of_shapes(shapes), 33.07, 2)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
