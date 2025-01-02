from myQueue import Queue
from stack import Stack

class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, node, neighbor, weight):
        if node not in self.graph:
            self.graph[node] = {}
        self.graph[node][neighbor] = weight

        if neighbor not in self.graph:
            self.graph[neighbor] = {}
        self.graph[neighbor][node] = weight

    def addVertex(self, node):
        if node not in self.graph:
            self.graph[node] = {}

    def removeEdge(self, node, neighbor):
        if node in self.graph and neighbor in self.graph[node]:
            del self.graph[node][neighbor]
        
        if neighbor in self.graph and node in self.graph[neighbor]:
            del self.graph[neighbor][node]


    def removeVertex(self, node):
        if node in self.graph:
            del self.graph[node]

    def dfs(self, start=None, end=None):
        if start == None:
            start = next(iter(self.graph))

        if end == None:
            end = list(self.graph)[-1]

        if start in self.graph and end in self.graph:
            visited = set()
            dfsStack = Stack(len(self.graph))
            dfsStack.push(start)
            path = []

            while dfsStack.stack:
                currentNode = dfsStack.pop()
                visited.add(currentNode)
                path.append(currentNode)
                if currentNode is end:
                    return path

                for child in self.graph[currentNode]:
                    if child not in visited:
                        dfsStack.push(child)

        return None

    def bfs(self, start=None, end=None, endFlag=True):
        if start == None:
            start = next(iter(self.graph))

        if end == None and endFlag == True:
            end = list(self.graph)[-1]

        if start in self.graph and (end in self.graph or endFlag == False):
            visited = set()
            bfsQueue = Queue(len(self.graph))
            bfsQueue.enqueue(start)
            path = [start]

            while bfsQueue.queue:
                currentNode = bfsQueue.dequeue()
                if currentNode is end:
                    return path
                
                if currentNode not in visited:
                    visited.add(currentNode)
                    for child in self.graph[currentNode]:
                        if child not in visited:
                            bfsQueue.enqueue(child)
                            path.append(child)

            if endFlag == False:
                return path

        return None

    def pathFinding(self, node1, node2):
        path = self.dfs(node1, node2)

        if path is not None:
            return path
        else:
            return None
        
    def connected(self):
        if self.graph:
            pathFromStart = self.bfs(endFlag=False)
            return len(pathFromStart) == len(self.graph)

class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, node, neighbor, weight):
        if node not in self.graph:
            self.graph[node] = {}
        self.graph[node][neighbor] = weight
        if neighbor not in self.graph:
            self.graph[neighbor] = {}

    def addVertex(self, node):
        if node not in self.graph:
            self.graph[node] = {}

    def removeEdge(self, node, neighbor):
        if neighbor in self.graph[node]:
            del self.graph[node][neighbor]

    def removeVertex(self, node):
        if node in self.graph:
            del self.graph[node]

    def dfs(self, start=None, end=None):
        if start == None:
            start = next(iter(self.graph))

        if end == None:
            end = list(self.graph)[-1]

        if start in self.graph and end in self.graph:
            visited = set()
            dfsStack = Stack(len(self.graph))
            dfsStack.push(start)
            path = []

            while dfsStack.stack:
                currentNode = dfsStack.pop()
                visited.add(currentNode)
                print(currentNode)
                path.append(currentNode)
                if currentNode is end:
                    return path

                for child in self.graph[currentNode]:
                    if child not in visited:
                        dfsStack.push(child)

        return None

    def bfs(self, start=None, end=None):
        if start == None:
            start = next(iter(self.graph))

        if end == None:
            end = list(self.graph)[-1]

        if start in self.graph and end in self.graph:
            visited = set()
            bfsQueue = Queue(len(self.graph))
            bfsQueue.enqueue(start)
            path = [start]

            while bfsQueue.queue:
                currentNode = bfsQueue.dequeue()
                if currentNode is end:
                    return path
                
                if currentNode not in visited:
                    visited.add(currentNode)
                    for child in self.graph[currentNode]:
                        if child not in visited:
                            bfsQueue.enqueue(child)
                            path.append(child)

        return None

    def pathFinding(self, node1, node2):
        if node1 and node2 in self.graph:
            path12 = self.dfs(node1, node2)
            path21 = self.dfs(node2, node1)

            if path12 is not None:
                if path21 is not None:
                    if len(path12) < len(path21):
                        return path12
                    else:
                        return path21
                else:
                    return path12
                    
            if path21 is not None:
                return path21
            
        return None
    
    def acyclic(self):
        if self.graph:
            for start in self.graph:
                visiting = set()
                visited = set()
                dfsStack = Stack(len(self.graph))
                dfsStack.push(start)

                while dfsStack.stack:
                    currentNode = dfsStack.pop()
                    
                    visiting.add(currentNode)

                    childrenVisited = True
                    for child in self.graph[currentNode]:
                        if child in visiting:
                            return False

                        if child not in visited:
                            dfsStack.push(child)
                            childrenVisited = False

                    if childrenVisited:
                        visiting.remove(currentNode)
                        visited.add(currentNode)

        return True
    
    def topologicalSort(self):
        if self.graph:
            visited = set()
            finished = Stack(len(self.graph))
            
            def dfs(node):
                visited.add(node)

                for child in self.graph[node]:
                    if child not in visited:
                        dfs(child)

                finished.push(node)

            for node in self.graph:
                if node not in visited:
                    dfs(node)

            sorted = []
            while finished.stack:
                sorted.append(finished.pop())
            
            return sorted
        
        return []

    def kruskal(self):

        nodeToIndex = {node: i for i, node in enumerate(self.graph)}

        sortedEdges = []
        for node, children in self.graph.items():
            for child, weight in children.items():
                sortedEdges.append((node,child,weight))

        sortedEdges = sorted(sortedEdges, key=lambda x: x[2])

        mst = {}

        uf = UnionFind(len(self.graph))

        edgesAdded = 0
        for edge in sortedEdges:
            if uf.find(nodeToIndex[edge[0]]) == uf.find(nodeToIndex[edge[1]]):
                continue
            else:
                if edge[0] not in mst:
                    mst[edge[0]] = {}
                mst[edge[0]][edge[1]] = edge[2]
                uf.union(nodeToIndex[edge[0]], nodeToIndex[edge[1]])
                edgesAdded += 1

            if edgesAdded > len(self.graph) - 1:
                break
        
        return mst
    
    def prim(self):
        if self.graph:
            node = list(self.graph)[0]
            mst = set()
            mst.add(node)
            
            while len(mst) < len(self.graph):
                listOfPotentialVertices = [item for d in [x[1] for x in self.graph.items() if x[0] in mst] for item in d.items()]
                print(listOfPotentialVertices)
                minimumValue = min([item[1] for item in listOfPotentialVertices if item[0] not in mst])
                mst.add([key for key, value in listOfPotentialVertices if value == minimumValue and key not in mst][0])

            print(mst)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, data):
        if self.parent[data] != data:
            self.parent[data] = self.find(self.parent[data])
        return self.parent[data]

    def union(self, data1, data2):
        parent1, parent2 = self.find(data1), self.find(data2)
        if parent1 == parent2:
            return

        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
        elif self.rank[parent2] > self.rank[parent1]:
            self.parent[parent1] = parent2
        else:
            self.parent[parent2] = parent1
            self.rank[parent1] += 1
    



graph = Graph()
graph.addEdge("A", "B", 4)
graph.addEdge("A", "C", 2)
graph.addEdge("C", "D", 5)
graph.addEdge("D", "E", 3)
# graph.addEdge("E", "F", 1)
graph.addEdge("F", "G", 6)
print(graph.graph)

graph.dfs("A")
graph.bfs("A")

directedGraph = DirectedGraph()
directedGraph.addEdge("A", "B", 3)
directedGraph.addEdge("A", "C", 2)
directedGraph.addEdge("C", "D", 1)
directedGraph.addEdge("D", "E", 4)
# directedGraph.addEdge("E", "C", 5)
directedGraph.addEdge("E", "F", 3)
directedGraph.addEdge("F", "G", 2)
# directedGraph.addEdge("G", "A", 4)
directedGraph.addEdge("G", "H", 1)
directedGraph.addEdge("H", "I", 3)
print(directedGraph.graph)

print(directedGraph.dfs("A", "G"))
directedGraph.bfs("A")
print("Path A to G: ", directedGraph.pathFinding("A", "G"))

print("Undirected Path A to G: ", graph.pathFinding("A", "G"))
print(graph.connected())

print(directedGraph.acyclic())
print(directedGraph.topologicalSort())

print(directedGraph.kruskal())

uf = UnionFind(5)
uf.union(1,2)
uf.union(3,4)
print(uf.find(2))
print(uf.rank)
print(uf.parent)

directedGraph.prim()