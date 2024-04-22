import algo

class UCS(algo.Algorithm):
    def __init__(self, map, origin, destination):
        super().__init__(map, origin, destination)

    def chooseNode(self):
        # get node with lowest node.cost
        node = min(self.frontier, key=lambda node: node.cost)
        self.frontier.remove(node)
        return node