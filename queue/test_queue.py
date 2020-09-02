import queue
import unittest


class TestQueue(unittest.TestCase):

    def test_enqueue_to_empty(self):
        q = queue.Queue()
        q.enqueue(5)
        self.assertEqual(len(q), 1)

    def test_dequeue_from_empty(self):
        q = queue.Queue()
        self.assertRaises(IndexError, q.dequeue)

    def test_dequeue_from_single_item(self):
        q = queue.Queue()
        q.enqueue(5)
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(len(q), 0)


if __name__ == "__main__":
    unittest.main()
