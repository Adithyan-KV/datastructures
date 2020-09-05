class Node():

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def __len__(self):
        current_node = self.head
        length = 0
        while current_node:
            length += 1
            current_node = current_node.next
        return length

    def __str__(self):
        current_node = self.head
        data_list = []
        string = ""
        while current_node is not None:
            data_list.append(f'({current_node.data})->')
            current_node = current_node.next
        data_list.append('None')
        return string.join(data_list)

    def insert_beginning(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insert_end(self, node):
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
        if self.is_node_in_list(prev_node):
            node.next = prev_node.next
            prev_node.next = node
        else:
            raise ItemNotInListError()

    def delete_beginning(self):
        if self.head is None:
            raise EmptyListError
        else:
            new_head = self.head.next
            self.head = new_head

    def delete_node(self, node):
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
        current_node = self.head
        while current_node is not None:
            if current_node is node:
                return True
            else:
                current_node = current_node.next
        return False

    def get_node_by_key(self, key):
        current_node = self.head
        while current_node is not None:
            if current_node.data == key:
                return current_node
            current_node = current_node.next
        return None


class EmptyListError(Exception):

    def __init__(self, message="cannot perform this operation on empty list"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ItemNotInListError(Exception):

    def __init__(self, message="node is not in list"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message
