def __init__(self):
        self.stack1 = []
        self.stack2 = []

def enqueue(self, item):
        self.stack1.append(item)

def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                raise IndexError("Queue is empty")
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

def peek(self):
        if not self.stack2:
            if not self.stack1:
                raise IndexError("Queue is empty")
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
