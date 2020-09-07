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

    def test_insert_to_end_of_empty_list(self):
        l = linked_list.LinkedList()
        n1 = linked_list.Node(1)
        l.insert_end(n1)
        self.assertEqual(len(l), 1)
        self.assertEqual(l.head, n1)

    def test_insert_to_end_of_non_empty_list(self):
        l = linked_list.LinkedList()
        n1 = linked_list.Node(1)
        n2 = linked_list.Node(2)
        l.insert_beginning(n1)
        l.insert_end(n2)
        self.assertEqual(len(l), 2)

    def test_insert_after_item_in_list(self):
        l = linked_list.LinkedList()
        n1 = linked_list.Node(1)
        n2 = linked_list.Node(2)
        n3 = linked_list.Node(3)
        l.insert_beginning(n1)
        l.insert_end(n2)
        l.insert_after(n1, n3)
        self.assertEqual(len(l), 3)
        self.assertEqual(l.head.next, n3)

    def test_insert_after_item_not_in_list(self):
        l = linked_list.LinkedList()
        n1 = linked_list.Node(1)
        n2 = linked_list.Node(2)
        n3 = linked_list.Node(3)
        l.insert_beginning(n1)
        self.assertRaises(linked_list.ItemNotInListError,
                          l.insert_after, n2, n3)

    def test_str_empty_list(self):
        l = linked_list.LinkedList()
        self.assertEqual(str(l), "None")

    def test_str_non_empty_list(self):
        l = linked_list.LinkedList()
        n1 = linked_list.Node(1)
        n2 = linked_list.Node(2)
        l.insert_beginning(n1)
        l.insert_end(n2)
        self.assertEqual(str(l), "(1)->(2)->None")

    def test_delete_beginning_from_empty_list(self):
        l = linked_list.LinkedList()
        self.assertRaises(linked_list.EmptyListError, l.delete_beginning)

    def test_delete_beginning_from_single_item_list(self):
        l = linked_list.LinkedList()
        n1 = linked_list.Node(1)
        l.insert_beginning(n1)
        l.delete_beginning()
        self.assertEqual(len(l), 0)

    def test_delete_beginning_from_multiple_item_list(self):
        l = linked_list.LinkedList()
        n1 = linked_list.Node(1)
        n2 = linked_list.Node(2)
        n3 = linked_list.Node(3)
        l.insert_beginning(n1)
        l.insert_end(n2)
        l.insert_end(n3)
        l.delete_beginning()
        self.assertEqual(len(l), 2)
        self.assertEqual(l.head, n2)
        l.delete_beginning()
        self.assertEqual(len(l), 1)
        self.assertEqual(l.head, n3)

    def test_delete_node_from_empty_list(self):
        l = linked_list.LinkedList()
        n1 = linked_list.Node(1)
        self.assertRaises(linked_list.EmptyListError, l.delete_node, n1)

    def test_delete_node_from_single_item_list(self):
        l = linked_list.LinkedList()
        n1 = linked_list.Node(1)
        l.insert_beginning(n1)
        l.delete_node(n1)
        self.assertEqual(l.head, None)

    def test_delete_node_not_in_list(self):
        l = linked_list.LinkedList()
        n1 = linked_list.Node(1)
        n2 = linked_list.Node(2)
        l.insert_beginning(n1)
        self.assertRaises(linked_list.ItemNotInListError, l.delete_node, n2)

    def test_delete_node_in_list(self):
        l = linked_list.LinkedList()
        n1 = linked_list.Node(1)
        n2 = linked_list.Node(2)
        n3 = linked_list.Node(3)
        n4 = linked_list.Node(4)
        l.insert_beginning(n1)
        l.insert_end(n2)
        l.insert_end(n3)
        l.insert_end(n4)
        # node at the end
        l.delete_node(n4)
        self.assertEqual(l.is_node_in_list(n4), False)
        self.assertEqual(len(l), 3)
        # node in the middle
        l.delete_node(n2)
        self.assertEqual(l.is_node_in_list(n2), False)
        self.assertEqual(len(l), 2)
        self.assertEqual(l.head.next, n3)

    def test_is_node_in_list(self):
        l = linked_list.LinkedList()
        n1 = linked_list.Node(1)
        n2 = linked_list.Node(2)
        n3 = linked_list.Node(3)
        l.insert_beginning(n1)
        l.insert_beginning(n2)
        self.assertEqual(l.is_node_in_list(n1), True)
        self.assertEqual(l.is_node_in_list(n3), False)

    def test_get_node_by_key_for_key_in_list(self):
        l = linked_list.LinkedList()
        n1 = linked_list.Node(1)
        n2 = linked_list.Node(2)
        l.insert_beginning(n1)
        l.insert_end(n2)
        self.assertEqual(l.get_node_by_key(2), n2)

    def test_get_node_by_key_for_key_not_in_list(self):
        l = linked_list.LinkedList()
        n1 = linked_list.Node(1)
        n2 = linked_list.Node(2)
        l.insert_beginning(n1)
        l.insert_end(n2)
        self.assertEqual(l.get_node_by_key(3), None)

    def test_reverse_empty_list(self):
        l = linked_list.LinkedList()
        self.assertRaises(linked_list.EmptyListError, l.reverse_list)

    def test_reverse_single_item_list(self):
        l = linked_list.LinkedList()
        n1 = linked_list.Node(1)
        l.insert_beginning(n1)
        l.reverse_list()
        self.assertEqual(l.head, n1)

    def test_reverse_multiple_item_list(self):
        l = linked_list.LinkedList()
        n1 = linked_list.Node(1)
        n2 = linked_list.Node(2)
        n3 = linked_list.Node(3)
        l.insert_beginning(n1)
        l.insert_end(n2)
        l.insert_end(n3)
        l.reverse_list()
        self.assertEqual(l.head, n3)
        self.assertEqual(l.head.next, n2)
        self.assertEqual(l.head.next.next, n1)


if __name__ == "__main__":
    unittest.main()
