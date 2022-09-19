class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.stack_size = 0
        self.minimum = None

    def push(self, value):
        self.stack_size += 1
        node = Node(value)
        node.next = self.top #set next to previous top
        self.top = node #set new top

        if not self.minimum:
            self.minimum = self.top.value
        elif self.top.value < self.minimum:
            self.minimum = self.top.value


    def pop(self):
        if self.top:
            self.stack_size -= 1
            value = self.top.value
            self.top = self.top.next #set new top one back

            if  self.top  and self.top.value < self.minimum:
                self.minimum = self.top.value

            return value
        else:
            raise Exception("Stack is empty.")

    def peek(self):
        if self.top:
            return self.top.value
        raise Exception("Stack is empty.")

    def min(self):
        return self.minimum

    def size(self):
        return self.stack_size

stack = Stack()
array = [1,2,3,4,5,6,7,8,9,10]

for a in array:
    stack.push(a)
    print(stack.min())

print("Stack top is {0}".format(stack.peek()))
print("Stack size is {0}".format(stack.size()))

for _ in range(len(array)):
    print(stack.pop())
    print(stack.min())

print(stack.stack_size)

