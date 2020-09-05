class Node():
    """A single node in a linked list
    """

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList():
    """
    A singly linked linked list object.
    """

    def __init__(self):
        self.head = None

    def __len__(self):
        """Get the number of nodes in the linked list

        Returns:
            int: the number of nodes in the list
        """
        current_node = self.head
        length = 0
        while current_node:
            length += 1
            current_node = current_node.next
        return length

    def __str__(self):
        """generates a readable string representation of the linked list

        Returns:
            string: a string representation of the list
        """
        current_node = self.head
        data_list = []
        string = ""
        while current_node is not None:
            data_list.append(f'({current_node.data})->')
            current_node = current_node.next
        data_list.append('None')
        return string.join(data_list)

    def insert_beginning(self, node):
        """Insert a node to the beginning of the linked list

        Args:
            node (Node object): the node to be inserted
        """
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insert_end(self, node):
        """Insert a node at the end of the linked list

        Args:
            node (Node object): the node to be inserted
        """
        if self.head is None:
            self.head = node
            node.next = None
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.next is None:
                    current_node.next = node
                    break
                current_node = current_node.next

    def insert_after(self, prev_node, node):
        """Insert a node after a specified node in the list. Raises an error if
        node is not in the list

        Args:
            prev_node (Node object): The node after which to insert the node
            node (Node object): The node to be inserted

        Raises:
            ItemNotInListError: Raised when the specified node after which the 
            node is to be inserted is not present in the list
        """
        if self.is_node_in_list(prev_node):
            node.next = prev_node.next
            prev_node.next = node
        else:
            raise ItemNotInListError()

    def delete_beginning(self):
        """Delete node at the beginning of the list

        Raises:
            EmptyListError: Raised when trying to delete from an already empty
            list
        """
        if self.head is None:
            raise EmptyListError
        else:
            new_head = self.head.next
            self.head = new_head

    def delete_node(self, node):
        """Delete a specified node from the linked list

        Args:
            node (Node object): The node to be deleted

        Raises:
            EmptyListError: Raised when trying to delete from an empty list
            ItemNotInListError: Raised when the node to be deleted is not in 
            the list

        Returns:
            Bool: Returns true on succesful deletion of node
        """
        if self.head is None:
            raise EmptyListError
        elif self.head is node:
            self.head = None
            return True
        else:
            current_node = self.head
            previous_node = None
            while current_node is not None:
                previous_node = current_node
                current_node = current_node.next
                if current_node is node:
                    previous_node.next = current_node.next
                    current_node.next = None
                    return True
            raise ItemNotInListError

    def is_node_in_list(self, node):
        """Checks if the specified node is in the list

        Args:
            node (Node object): The node to check for in the list

        Returns:
            Bool: Returns True if node is in the list and False otherwise
        """
        current_node = self.head
        while current_node is not None:
            if current_node is node:
                return True
            else:
                current_node = current_node.next
        return False

    def get_node_by_key(self, key):
        """Get a node by the key value. If multiple nodes with the same key
        value exist, only the first is returned

        Args:
            key (key): The key of the node

        Returns:
            Node Object: The node with the specified key
        """
        current_node = self.head
        while current_node is not None:
            if current_node.data == key:
                return current_node
            current_node = current_node.next
        return None


class EmptyListError(Exception):
    """Error raised when trying to do an operation that is not valid on an 
    empty list.
    """

    def __init__(self, message="cannot perform this operation on empty list"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ItemNotInListError(Exception):
    """Raised when an operation involves an item that is not in the list"""

    def __init__(self, message="node is not in list"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message
