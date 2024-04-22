import algo

class BFS(algo.Algorithm):
    def __init__(self, map, origin, destination):
        super().__init__(map, origin, destination)
        
    def chooseNode(self):
        return self.frontier.pop(0) # get the first element, the oldest
    
    def search(self):
        return super().search()