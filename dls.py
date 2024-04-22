import algo

class DLS(algo.Algorithm):
    def __init__(self, map, origin, destination):
        frac = 3
        self.max_depth = int(len(map.nodes) / frac)
        self.current_depth = self.max_depth
        super().__init__(map, origin, destination)

    def chooseNode(self, verbose = False):
        if self.current_depth > 0:
            self.current_depth -= 1
            return self.frontier.pop() # get the last element, the most recently added
        else:
            self.current_depth = self.max_depth
            return self.frontier.pop(0) # max depth reached, try another path
    
    def search(self, verbose = False):
        return super().search(verbose)