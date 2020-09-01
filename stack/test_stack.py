import stack
import unittest


class TestStack(unittest.TestCase):

    def test_is_empty(self):
        s = stack.Stack()
        self.assertEqual(len(s), 0)


if __name__ == "__main__":
    unittest.main()
