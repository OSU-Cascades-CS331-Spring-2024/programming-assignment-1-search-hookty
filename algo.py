class Algorithm:
    def __init__(self, map, origin, destination):
        self.map = map
        self.origin = origin
        self.destination = destination
        self.frontier = []
        self.visited = []
        self.path = []
        self.cost = 0
        self.search()