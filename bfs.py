import algo

class BFS(algo.Algorithm):
    def __init__(self, map, origin, destination):
        super().__init__(map, origin, destination)
        self.frontier.append(origin)
        self.visited.append(origin)
        self.nodeParents = {}

    def search(self):
        while self.frontier:
            node = self.frontier.pop(0)
            self.visited.append(node)
            
            if node == self.destination:
                self.path = self.getPath(node)
                return self.path
            
            for edge in node.neighbors:
                neighbor = self.map.findNode(edge)
                if neighbor not in self.visited:
                    self.nodeParents[neighbor] = node  # Add this line
                    self.frontier.append(neighbor)
                    self.visited.append(neighbor)

        return None
    
    def getPath(self, node):
        path = []
        while node is not None:
            path.append(node)
            node = self.nodeParents.get(node)
        return path[::-1]
    
    def __str__(self):
        string = 'BFS\n'
        string += 'Path: ' + str(self.path) + '\n'
        string += 'Cost: ' + str(self.cost) + '\n'
        return string
    
    def __repr__(self):
        return str(self)