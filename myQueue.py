class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []
    
    def enqueue(self, data):
        if len(self.queue) < self.size:
            self.queue.append(data)
        else:
            raise Exception("Queue Overflow")
        
    def dequeue(self):
        if self.queue:
            front = self.queue[0]
            if len(self.queue) > 1:
                for i in range(1, len(self.queue)):
                    self.queue[i-1] = self.queue[i]
            self.queue.pop()
            return front
        else:
            raise Exception("Queue Underflow")
        
    def peek(self):
        if self.queue:
            return self.queue[0]
        else:
            raise Exception("Queue Underflow")

q1 = Queue(5)
q1.enqueue('apple')
q1.enqueue('banana')
q1.enqueue('orange')
q1.enqueue('cherry')
q1.enqueue('strawberry')
# q1.enqueue('cactus')
print(q1.queue)
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.queue)
print(q1.peek())

class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * self.size
        self.head = 0
        self.tail = 0

    def enqueue(self, data):
        if self.head == self.tail:
            self.buffer.append(data)
            self.tail = (self.tail + 1) % self.size
        else:
            self.buffer[self.tail] = data
            self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        if self.head != self.tail:
            result = self.buffer[self.head]
            self.head = (self.head + 1) % self.size
            return result
        else:
            raise Exception("Buffer Underflow")
        
    def fullCheck(self):
        if (self.tail + 1) % self.size == self.head:
            return True
        else: 
            return False