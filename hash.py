class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, s):
        return sum([ord(c) for c in s])%self.size    

    def insert(self, data):
        address = self.hash(data)
        if data not in self.table[address]:
            self.table[address].append(data)

    def search(self, data):
        address = self.hash(data)
        if data in self.table[address]:
            return True
        else:
            return False

    def delete(self, data):
        address = self.hash(data)
        try:
            self.table[address].remove(data)
            print(data, " deleted.")
        except ValueError:
            print(data, " not in table.")

    def resize(self):
        numItems = sum(len(innerList) for innerList in self.table)
        loadFactor = numItems / self.size
        print("Load factor: ", loadFactor)
        if loadFactor > 0.7:
            print("Resizing.")
            self.size *= 2
            copyTable = [item for sublist in self.table for item in sublist]
            self.table = [[] for _ in range(self.size)]
            for item in copyTable:
                self.insert(item)

hTable = HashTable(11)
print(hTable.hash("banana"))
print(ord('b'))
print(hTable.table)
hTable.insert("apple")
hTable.insert("banana")
hTable.insert("orange")
hTable.insert("grapefruit")
print(hTable.table)

print("grapefruit in table? ", hTable.search('grapefruit'))
print("grape in table? ", hTable.search('grape'))

hTable.delete('orange')
print(hTable.table)

hTable.resize()
hTable.insert("cherry")
hTable.insert("lime")
hTable.insert("blueberry")
hTable.insert("raspberry")
hTable.insert("mango")
print(hTable.table)
hTable.resize()
print(hTable.table)
