import unittest
import linked_list


class TestLinkedList(unittest.TestCase):

    def test_empty_list(self):
        l = linked_list.LinkedList()
        self.assertEqual(l.head, None)
        self.assertEqual(len(l), 0)

    def test_length_of_one_item_list(self):
        l = linked_list.LinkedList()
        n1 = linked_list.Node(1)
        l.insert_beginning(n1)
        self.assertEqual(len(l), 1)


if __name__ == "__main__":
    unittest.main()
