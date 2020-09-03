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

    def test_insert_to_beginning_of_empty_list(self):
        l = linked_list.LinkedList()
        n1 = linked_list.Node(1)
        l.insert_beginning(n1)
        self.assertNotEqual(l.head, None)
        self.assertEqual(l.head, n1)

    def test_insert_to_beginning_of_non_empty_list(self):
        l = linked_list.LinkedList()
        n1 = linked_list.Node(1)
        n2 = linked_list.Node(2)
        l.insert_beginning(n1)
        l.insert_beginning(n2)
        self.assertEqual(len(l), 2)
        self.assertEqual(l.head, n2)


if __name__ == "__main__":
    unittest.main()
