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

    def insert_beginning(self, node):
        if not self.head:
            self.head = node
            node.next = None
