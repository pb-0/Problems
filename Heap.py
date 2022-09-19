class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Heap:
    def __init__(self):
        self.left = None
        self.right = None

    def push(self, value):
        node = Node(value)
        node.next =
        if not self.left and not self.right:
            self.right = self.left = node
        else:
            if value
            self.right = Node(value)

    def pop(self):

