class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    firstNode = None
    lastNode = None

    def insertAtBeginning(self, data):
        insertedNode = None
        if self.lastNode is None:
            insertedNode = Node(data, None)
            self.lastNode = insertedNode
        else:
            insertedNode = Node(data, self.firstNode)
        self.firstNode = insertedNode

    def insertAtEnd(self, data):
        insertedNode = Node(data, None)
        if self.firstNode is None:
            self.firstNode = insertedNode
        else:
            self.lastNode.next = insertedNode
        self.lastNode = insertedNode

    def deleteNode(self, data):
        if self.firstNode is not None:
            nodeToDelete = self.firstNode

            while nodeToDelete.data != data and nodeToDelete.next.data != data and nodeToDelete.next is not None:
                nodeToDelete = nodeToDelete.next

            if nodeToDelete.data is data:
                self.firstNode = self.firstNode.next

            elif nodeToDelete.next.data is data:
                nodeToDelete.next = nodeToDelete.next.next
    
    def search(self, data):
        if self.firstNode is not None:
            searchNode = self.firstNode
            while searchNode.data is not data and searchNode.next is not None:
                searchNode = searchNode.next
            if searchNode.data is data:
                return True
            else:
                return False
        else:
            return False
        
    def print(self):
        if self.firstNode is not None:
            printNode = self.firstNode
            while printNode is not None:
                print(printNode.data)
                printNode = printNode.next
        else:
            print("Linked List is empty")

    def reverseList(self):
        if self.firstNode is not None:
            oldLastNode = self.lastNode

            while self.lastNode is not self.firstNode:
                currentNode = self.firstNode
                while currentNode.next is not self.lastNode:
                    currentNode = currentNode.next
                currentNode.next.next = currentNode
                self.lastNode = currentNode
            
            self.firstNode.next = None
            self.firstNode = oldLastNode

    def removeDuplicates(self):
        if self.firstNode is not None:
            checkNode = self.firstNode
            while checkNode is not self.lastNode:
                currentNode = self.firstNode
                currentData = checkNode.data

                while currentNode is not self.lastNode:
                    if currentNode.next.data == currentData and currentNode.next is not checkNode:
                        if currentNode.next.next is not None:
                            currentNode.next = currentNode.next.next
                        else:
                            currentNode.next = None
                            self.lastNode = currentNode
                            break
                    currentNode = currentNode.next
                
                checkNode = checkNode.next





ll1 = LinkedList()
# print(ll1.search("cherry"))
ll1.insertAtBeginning("banana")
ll1.insertAtBeginning("apple")
ll1.insertAtBeginning("banana")
ll1.insertAtEnd("cranberry")
ll1.insertAtEnd("cherry")
ll1.insertAtEnd("cranberry")
ll1.insertAtEnd("orange")
# ll1.deleteNode("banana")


# print(lastNode.data)
# print(ll1.search("apple"))
print("List")
ll1.print()
ll1.reverseList()
# # lastNode = ll1.firstNode
# # while lastNode.next is not None:
# #     print("Current Node Data")
# #     print(lastNode.data)
# #     print("Next Node Data")
# #     print(lastNode.next.data)
# #     lastNode = lastNode.next
print("Reversed List")
ll1.print()

# print("Last Node")
# print(ll1.firstNode.next.next.data)
# print("First Node")
# print(ll1.firstNode.next.data)

ll1.removeDuplicates()
print("No duplicates")
ll1.print()