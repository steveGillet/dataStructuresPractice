class MinHeap:
    def __init__(self):
        self.heap = []
    def insert(self,data):
        self.heap.append(data)
        currentIndex = len(self.heap) - 1
        while currentIndex > 0 and self.heap[currentIndex] < self.heap[(currentIndex - 1) // 2]:
            temp = self.heap[(currentIndex - 1) // 2]
            self.heap[(currentIndex - 1) // 2] = self.heap[currentIndex]
            self.heap[currentIndex] = temp
            currentIndex = (currentIndex - 1) // 2

    def extractMin(self):
        if not self.heap:
            return None
        
        tempMin = self.heap[0]
        self.heap[0] = self.heap.pop()
        if self.heap:
            currentIndex = 0
            while currentIndex < len(self.heap) // 2:
                if self.heap[currentIndex] > self.heap[currentIndex * 2 + 1]:
                    self.heap[currentIndex], self.heap[currentIndex * 2 + 1] = self.heap[currentIndex * 2 + 1], self.heap[currentIndex]
                    currentIndex = currentIndex * 2 + 1
                elif self.heap[currentIndex] > self.heap[currentIndex * 2 + 2]:
                    self.heap[currentIndex], self.heap[currentIndex * 2 + 2] = self.heap[currentIndex * 2 + 2], self.heap[currentIndex]
                    currentIndex = currentIndex * 2 + 2
                else:
                    break

        return tempMin

heap = MinHeap()
heap.insert(5)
heap.insert(4)
heap.insert(6)
heap.insert(3)

print(heap.heap)
print(heap.extractMin())
print(heap.heap)