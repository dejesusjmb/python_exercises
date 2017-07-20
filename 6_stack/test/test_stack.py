import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from stack import Stack

class TestStack(unittest.TestCase):

    def test_size_0_after_create(self):
        stack = Stack()
        self.assertEqual(stack.get_size(), 0)

    def test_push_increases_stack_size(self):
        ''' implement push method that takes one elemet as argument
        and increases stack size'''
        stack = Stack()
        stack.push('1')
        self.assertEqual(stack.get_size(), 1)
        stack.push('2')
        self.assertEqual(stack.get_size(), 2)

    ''' Do you have any duplication in your tests? How to remove it? '''

    def test_pop_decreases_stack_size(self):
        ''' implement pop that decreases stack size '''
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.get_size(), 2)
        stack.pop()
        self.assertEqual(stack.get_size(), 1)
        stack.pop()
        self.assertEqual(stack.get_size(), 0)

    def test_popping_empty_stack_returns_None(self):
        ''' special case of popping an empty stack should return None '''
        stack = Stack()
        self.assertEqual(stack.pop(), None)

    def test_when_1_pushed_pop_returns_1(self):
        ''' test pushing and popping 1 to stack '''
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.pop(), 1)

    def test_stack_works_as_lifo(self):
        ''' test pushing several items, they should pop in last in first out order '''
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.get_size(), 3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), None)

    ''' Do you think you can refactor your stack? '''


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
