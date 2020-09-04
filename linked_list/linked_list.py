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

    def delete_beginning(self):
        if self.head is None:
            raise EmptyListError
        else:
            new_head = self.head.next
            self.head = new_head


class EmptyListError(Exception):

    def __init__(self, message="cannot perform this operation on empty list"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message
