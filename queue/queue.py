from collections import deque


class Queue():

    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft()

    def __len__(self):
        return len(self.queue)
