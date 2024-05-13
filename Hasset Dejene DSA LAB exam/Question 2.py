class Stack:
    def init(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print ("Stack After Pushing Elemnts:", stack.stack)

print("Popped item from Stack;", stack.pop())

print ("Stack after popping element", stack.stack)


