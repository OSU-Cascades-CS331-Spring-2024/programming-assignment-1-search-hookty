import algo

class DFS(algo.Algorithm):
    def __init__(self, map, origin, destination):
        super().__init__(map, origin, destination)

    def chooseNode(self):
        return self.frontier.pop() # get the last element, the most recently added
    
    def search(self):
        return super().search()