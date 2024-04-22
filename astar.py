import algo

class AStar(algo.Algorithm):
    def __init__(self, map, origin, destination):
        super().__init__(map, origin, destination)

    def heuristic(self, node1, node2):
        # straight line distance
        return node1.distanceTo(node2)
        
    def chooseNode(self):
        # get lowest sum of cost and heuristic
        node = min(self.frontier, key=lambda node: node.cost + self.heuristic(node, self.destination))
        return self.frontier.pop(self.frontier.index(node))