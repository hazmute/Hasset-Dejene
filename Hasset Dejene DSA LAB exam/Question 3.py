class LinearQueueUsingTwoStacks:
    def init(self, capacity):
        self.stack1 = []
        self.stack2 = []
        self.capacity = capacity

    def enqueue(self, item):
        if len(self.stack1) == self.capacity:
            print("Queue is full")
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.stack2.append(item)
            while self.stack2:
                self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if not self.stack1:
            raise IndexError("Queue is empty")
        return self.stack1.pop()

    def peek(self):
        if not self.stack1:
            raise IndexError("Queue is empty")
        return self.stack1[-1]

queue = LinearQueueUsingTwoStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Front of the queue:", queue.peek())

print("Dequeued item:", queue.dequeue())
print("Dequeued item:", queue.dequeue())
print("Dequeued item:", queue.dequeue())
print("Dequeued item:", queue.dequeue())
