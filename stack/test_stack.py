import stack
import unittest


class TestStack(unittest.TestCase):

    def test_is_empty_on_creation(self):
        s = stack.Stack()
        self.assertEqual(len(s), 0)

    def test_push_to_empty(self):
        s = stack.Stack()
        s.push(5)
        self.assertEqual(len(s), 1)

    def test_pop_single_item_to_empty(self):
        s = stack.Stack()
        s.push(5)
        s.pop()
        self.assertEqual(len(s), 0)

    def test_pop_value(self):
        s = stack.Stack()
        s.push(5)
        self.assertEqual(s.pop(), 5)


if __name__ == "__main__":
    unittest.main()
