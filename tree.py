from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

apple = Node("apple")
orange = Node("orange")
apple.leftChild = orange
print(apple.leftChild.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            currentNode = self.root

            while data != currentNode.data:
                if data < currentNode.data:
                    if currentNode.leftChild is None:
                        currentNode.leftChild = Node(data)
                        return
                    else:
                        currentNode = currentNode.leftChild
                else:
                    if currentNode.rightChild is None:
                        currentNode.rightChild = Node(data)
                        return
                    else:
                        currentNode = currentNode.rightChild

    def inOrderTraversal(self):
        result = []

        if not self.root:
            return result
        
        stack = deque()
        currentNode = self.root
        stack.append(currentNode)
        while currentNode.leftChild:
            currentNode = currentNode.leftChild
            stack.append(currentNode)
        
        while stack:
            currentNode = stack.pop()
            result.append(currentNode.data)
            if currentNode.rightChild:
                stack.append(currentNode.rightChild)
                rightNode = currentNode.rightChild
                while rightNode.leftChild:
                    rightNode = rightNode.leftChild
                    stack.append(rightNode)
        
        return result

    def preOrderTraversal(self):
        result = []

        if not self.root:
            return result
        
        stack = deque()
        stack.append(self.root)
        
        while stack:
            currentNode = stack.popleft()
            result.append(currentNode.data)
            if currentNode.leftChild:
                stack.append(currentNode.leftChild)
            if currentNode.rightChild:
                stack.append(currentNode.rightChild)

        return result

    def postOrderTraversal(self):
        result = []

        if not self.root:
            return result
        
        stack = deque()
        stackReverse = deque()
        stack.append(self.root)
        
        while stack:
            currentNode = stack.popleft()
            stackReverse.append(currentNode)
            if currentNode.rightChild:
                stack.append(currentNode.rightChild)
            if currentNode.leftChild:
                stack.append(currentNode.leftChild)

        while stackReverse:
            result.append(stackReverse.pop().data)

        return result
    
    def print(self, traversal=""):
        if traversal == "in":
            print(self.inOrderTraversal())
        elif traversal == "pre":
            print(self.preOrderTraversal())
        elif traversal == "post":
            print(self.postOrderTraversal())
        else:
            print("Printing In Order By Default: ", self.inOrderTraversal())

    def search(self, data):
        if data in self.inOrderTraversal():
            return True
        else:
            return False


bst = BinarySearchTree()
bst.insert(6)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(9)
bst.insert(5)
bst.insert(4)

# print(bst.root.data)
# print(bst.root.rightChild.rightChild.data)

bst.print("post")
bst.print()

print(bst.search(10))
