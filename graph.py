from myQueue import Queue
from stack import Stack

class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

        if neighbor not in self.graph:
            self.graph[neighbor] = []
        self.graph[neighbor].append(node)

    def addVertex(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def removeEdge(self, node, neighbor):
        if node in self.graph and neighbor in self.graph[node]:
            self.graph[node].remove(neighbor)
        
        if neighbor in self.graph and node in self.graph[neighbor]:
            self.graph[neighbor].remove(node)


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

    def addEdge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)
        if neighbor not in self.graph:
            self.graph[neighbor] = []

    def addVertex(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def removeEdge(self, node, neighbor):
        if neighbor in self.graph[node]:
            self.graph[node].remove(neighbor)

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

        
    



graph = Graph()
graph.addEdge("A", "B")
graph.addEdge("A", "C")
graph.addEdge("C", "D")
graph.addEdge("D", "E")
# graph.addEdge("E", "F")
graph.addEdge("F", "G")
print(graph.graph)

graph.dfs("A")
graph.bfs("A")

directedGraph = DirectedGraph()
directedGraph.addEdge("A", "B")
directedGraph.addEdge("A", "C")
directedGraph.addEdge("C", "D")
directedGraph.addEdge("D", "E")
# directedGraph.addEdge("E", "C")
# directedGraph.addEdge("E", "F")
directedGraph.addEdge("F", "G")
# directedGraph.addEdge("G", "A")
directedGraph.addEdge("G", "H")
directedGraph.addEdge("H", "I")
print(directedGraph.graph)

print(directedGraph.dfs("A", "G"))
directedGraph.bfs("A")
print("Path A to G: ", directedGraph.pathFinding("A", "G"))

print("Undirected Path A to G: ", graph.pathFinding("A", "G"))
print(graph.connected())

print(directedGraph.acyclic())
print(directedGraph.topologicalSort())