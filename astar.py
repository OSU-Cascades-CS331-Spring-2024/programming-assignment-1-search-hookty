import algo

class AStar(algo.Algorithm):
    def __init__(self, map, origin, destination):
        super().__init__(map, origin, destination)

    def heuristic(self, node1, node2):
        # straight line distance
        return node1.distanceTo(node2)
        
    def chooseNode(self, verbose = False):
        sorted = self.sortedFrontier(verbose)
        # get lowest sum of cost and heuristic
        node = sorted[0]
        for n in sorted:
            if n.cost + self.heuristic(n, self.destination) < node.cost + self.heuristic(node, self.destination):
                node = n
        return self.frontier.pop(self.frontier.index(node))
    
    def search(self, verbose = False):
        return super().search(verbose)