class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Queue:
    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self, value):
        node = Node(value)
        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.rear = node
            self.front = node

    def dequeue(self):
        if not self.front:
            raise Exception("Queue is empty")
        value = self.front.value
        self.front = self.front.next
        return value

queue = Queue()
array = [1,2,3,4,5]

for a in array:
    queue.enqueue(a)

for _ in range(len(array)):
    print(queue.dequeue())