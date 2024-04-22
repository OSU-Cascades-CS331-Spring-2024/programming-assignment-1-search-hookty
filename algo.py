import random

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

        #statistic variables
        self.totalVisited = 0
        self.totalSuccessors = 0
        self.totalFrontier = 0


    # needs to be overridden by subclasses
    def chooseNode(self):
        print('Algorithm not implemented! Randomly choosing node.')
        return self.frontier.pop(random.randint(0, len(self.frontier) - 1))

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
            self.totalVisited += 1
            
            if node == self.destination:
                self.path = self.getPath(node)
                return self.path, self.totalVisited, self.totalSuccessors, self.totalFrontier
            
            for edge in node.neighbors:
                neighbor = self.map.findNode(edge)
                if neighbor not in self.visited:
                    self.nodeParents[neighbor] = node 
                    self.frontier.append(neighbor)
                    self.visited.append(neighbor)
                    self.totalSuccessors += 1

                    #set the cost of the neighbor
                    neighbor.cost = node.cost + node.neighbors[edge]

            self.totalFrontier = len(self.frontier)
            
        return None
    
    def __str__(self):
        string = self.__class__.__name__ + '\n'
        string += 'Path: ' + str(self.path) + '\n'
        string += 'Cost: ' + str(self.cost) + '\n'
        return string
    
    def __repr__(self):
        return str(self)