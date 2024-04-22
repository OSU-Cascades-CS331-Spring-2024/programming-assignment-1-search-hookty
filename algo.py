class Algorithm:
    def __init__(self, map, origin, destination):
        self.map = map
        self.origin = origin
        self.destination = destination

        self.frontier = []
        self.visited = []

        self.frontier.append(origin)
        self.visited.append(origin)
        
        self.nodeParents = {}
        self.path = []
        self.cost = 0

    # needs to be overridden by subclasses
    def chooseNode(self):
        print('Algorithm not implemented!')
        return None

    def getPath(self, node):
        path = []
        while node is not None:
            path.append(node)
            node = self.nodeParents.get(node)
        return path[::-1]
    
    def search(self):
        while self.frontier:
            node = self.chooseNode()
           
            self.visited.append(node)
            
            if node == self.destination:
                self.path = self.getPath(node)
                return self.path
            
            for edge in node.neighbors:
                neighbor = self.map.findNode(edge)
                if neighbor not in self.visited:
                    self.nodeParents[neighbor] = node 
                    self.frontier.append(neighbor)
                    self.visited.append(neighbor)

        return None
    
    def __str__(self):
        string = self.__class__.__name__ + '\n'
        string += 'Path: ' + str(self.path) + '\n'
        string += 'Cost: ' + str(self.cost) + '\n'
        return string
    
    def __repr__(self):
        return str(self)