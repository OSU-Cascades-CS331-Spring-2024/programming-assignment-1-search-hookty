import algo

class UCS(algo.Algorithm):
    def __init__(self, map, origin, destination):
        super().__init__(map, origin, destination)

    def chooseNode(self, verbose = False):
        # get node with lowest node.cost
        sorted = self.sortedFrontier(verbose)
        node = sorted[0]
        self.frontier.remove(node)
        return node
    
    def search(self, verbose = False):
        return super().search(verbose)