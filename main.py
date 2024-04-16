import os
import map

#parse command line arguments, always preceded with '-'
searchAlgorithm = 'bfs'
searchAlgorithms = ['bfs', 'dfs', 'ucs', 'astar']
def setSearch(arg):
    global searchAlgorithm
    if arg in searchAlgorithms:
        searchAlgorithm = arg
    else:
        print('Invalid search algorithm. Please choose from the following: bfs, dfs, ucs, astar')
        raise SystemExit
    
mapFile = './france.txt'
Gmap = None
def setMap(arg = None):
    global mapFile
    global Gmap

    mapFile = arg if arg is not None else mapFile

    if os.path.exists(mapFile):
        Gmap = map.Map(mapFile)
    else:
        print('Map file not found.')
        raise SystemExit

origin = None
def setOrigin(arg):
    global origin
    if map.findNode(arg) is not None:
        origin = map.findNode(arg)
    else:
        print('Origin node not found in map.')
        raise SystemExit
    
destination = None
def setDestination(arg):
    global destination
    if map.findNode(arg) is not None:
        destination = map.findNode(arg)
    else:
        print('Destination node not found in map.')
        raise SystemExit
    
args = {
    'm': setMap, #checks for map first to initialize the map
    's': setSearch,
    'a': setOrigin,
    'b': setDestination,
}

def parseArgs(argv):
    #check against the args dictionary 
    for flag in args:
        for i in range(1, len(argv)):
            if argv[i][1].lower() == flag:
                args[flag](argv[i + 1])
            
def main(argv):
    global searchAlgorithm
    #parse command line arguments
    parseArgs(argv)
    
    if Gmap is None:
        setMap()


    origins = []
    destinations = []
    if origin or destination is None: #do them all
        searchAlgorithm = searchAlgorithms 

        dests = ["Nice", "Calais", "Bordeaux", "Grenoble", "Paris", "Grenoble", "Brest", "Nantes", "Strasbourg"]
        orgs = ["Brest", "Montpellier", "Strasbourg", "Paris", "Grenoble", "Brest", "Grenoble", "Nice", "Caen"]

        for i in range(len(dests)):
            origins.append(Gmap.findNode(orgs[i]))
            destinations.append(Gmap.findNode(dests[i]))

    else:
        origins.append(Gmap.findNode(origin))
        destinations.append(Gmap.findNode(destination))
        