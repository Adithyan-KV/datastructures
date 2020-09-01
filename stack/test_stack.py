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

    def test_pop_empty(self):
        s = stack.Stack()
        self.assertRaises(IndexError, s.pop)

    def test_pop_single_item_to_empty(self):
        s = stack.Stack()
        s.push(5)
        s.pop()
        self.assertEqual(len(s), 0)

    def test_push_2_pop_1(self):
        s = stack.Stack()
        s.push(3)
        s.push(4)
        self.assertEqual(s.pop(), 4)
        self.assertEqual(len(s), 1)

    def test_pop_value(self):
        s = stack.Stack()
        s.push(5)
        self.assertEqual(s.pop(), 5)
        self.assertEqual(len(s), 0)

    def test_peek_empty(self):
        s = stack.Stack()
        self.assertRaises(IndexError, s.peek)

    def test_peek_single_item_stack(self):
        s = stack.Stack()
        s.push(5)
        self.assertEqual(s.peek(), 5)

    def test_str_empty(self):
        s = stack.Stack()
        self.assertEqual(str(s), "[]")

    def test_str_non_empty(self):
        s = stack.Stack()
        s.push(6)
        s.push(3)
        s.push(8)
        self.assertEqual(str(s), "[6, 3, 8]")

    def test_is_empty_function(self):
        s = stack.Stack()
        self.assertEqual(s.is_empty(), True)
        s.push(8)
        self.assertEqual(s.is_empty(), False)


if __name__ == "__main__":
    unittest.main()
