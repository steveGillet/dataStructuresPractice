class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []
    
    def push(self, data):
        if len(self.stack) < self.size:
            self.stack.append(data)
        else:
            raise StackOverflowException
        
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None    

class StackOverflowException(Exception):
    def __init__(self, message="Stack overflow occurred"):
        self.message = message
        super().__init__(self.message)


def parenthesesEven(s):
    counterStack = Stack(100)

    for c in s:
        if c == '(':
            counterStack.push(c)
        elif c == ')':
            if counterStack.peek() == '(':
                counterStack.pop()
            else:
                return False

    if counterStack.stack:
        return False
    else:
        return True
    

stack = Stack(11)
print(stack.stack)
stack.push('banana')
stack.push('apple')
print(stack.peek())

stringStack = Stack(13)
s = 'cool cat'
for c in s:
    stringStack.push(c)

reversedString = ""
while stringStack.stack:
    reversedString += stringStack.pop()

print(reversedString)

print(parenthesesEven("hello mr frog (dummy), I hope you have a good day (not)."))
print(parenthesesEven("hello mr frog (dummy), I hope you have a good day not)."))

class StackQueue:
    def __init__(self, size):
        self.size = size
        self.stack1 = Stack(size)
        self.stack2 = Stack(size)

    def enqueue(self, data):
        if len(self.stack1.stack) + len(self.stack2.stack) < self.size:
            self.stack1.push(data)
        else:
            raise Exception("Queue Overflow")
        
    def dequeue(self):
        if self.stack1.stack or self.stack2.stack:
            while self.stack1.stack:
                self.stack2.push(self.stack1.pop())
            return self.stack2.pop()
        else:
            raise Exception("Queue Underflow")

    def peek(self):
        if self.stack1.stack or self.stack2.stack:
            while self.stack1.stack:
                self.stack2.push(self.stack1.pop())
            return self.stack2.peek()
        else:
            raise Exception("Queue Underflow")

sq = StackQueue(5)
sq.enqueue("apple")
sq.enqueue("grape")
sq.enqueue("cherry")
print(sq.stack1.stack)

print(sq.dequeue())
print(sq.stack2.stack)
print(sq.peek())