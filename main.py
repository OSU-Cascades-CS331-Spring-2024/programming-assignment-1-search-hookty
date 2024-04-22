import os
import sys
import map
import dls
import bfs
import ucs
import astar

#parse command line arguments, always preceded with '-'
searchAlgorithm = ['bfs']
searchAlgorithms = ['bfs', 'dls', 'ucs', 'astar']
def setSearch(arg):
    global searchAlgorithm
    if arg in searchAlgorithms:
        searchAlgorithm = [arg]
    else:
        print('Invalid search algorithm. Please choose from the following: bfs, dls, ucs, astar')
        raise SystemExit
    
mapFile = './france.txt'
Gmap = map.Map(mapFile)
def setMap(arg = None):
    global mapFile
    global Gmap

    mapFile = arg if arg is not None else mapFile

    Gmap = None

    if os.path.exists(mapFile):
        Gmap = map.Map(mapFile)
    else:
        print('Map file not found.')
        raise SystemExit

origin = None
def setOrigin(arg):
    global origin
    if Gmap.findNode(arg) is not None:
        origin = Gmap.findNode(arg)
    else:
        print('Origin node not found in map.')
        raise SystemExit
    
destination = None
def setDestination(arg):
    global destination
    if Gmap.findNode(arg) is not None:
        destination = Gmap.findNode(arg)
    else:
        print('Destination node not found in map.')
        raise SystemExit
    
verbose = False
def setVerbose():
    global verbose
    verbose = True
    
args = {
    'm': setMap, #need checks for map first to initialize the map
    's': setSearch,
    'a': setOrigin,
    'b': setDestination,
    'v': setVerbose,
}

done = []

def parseArgs(argv):
    #check against the args dictionary 
    for flag in args:
        for i in range(1, len(argv)):
            if argv[i][1].lower() == flag and flag not in done:
                if flag == 'v':
                    args[flag]()
                else:
                  args[flag](argv[i + 1])
                done.append(flag)

def clearFile(openFile):
    openFile.seek(0)
    openFile.truncate()

def writeOut(path, i1, i2, i3, name = ''):
    file1 = open("solutions.txt", "a")
    
    file1.write(name + '\n')

    for node in path:
        file1.write(str(node) + '\n')

    l1 = " // visited"
    l2 = " // successors"
    l3 = " // frontier"

    file1.write(str(i1) + l1 + '\n')
    file1.write(str(i2) + l2 + '\n')
    file1.write(str(i3) + l3 + '\n')
    file1.write('\n')

    file1.close()

def avgList(l):
    return sum(l) / len(l)

def writeAvg(i1, i2, i3, i4):
    file2 = open("README.txt", "a")
    clearFile(file2)

    l1 = " // avg visited"
    l2 = " // avg successors"
    l3 = " // avg frontier"
    l4 = " // wins"
    
    wins = {}

    for algorithm in searchAlgorithm:
        wins[algorithm] = 0

    for i in range(len(i4['bfs'])):
        for algorithm in searchAlgorithm:
            if i4[algorithm][i] == min([i4[a][i] for a in searchAlgorithm]):
                wins[algorithm] += 1

    for algorithm in searchAlgorithm:
        file2.write(algorithm + '\n')
        
        s1 = str(round(avgList(i1[algorithm]), 2))
        s2 = str(round(avgList(i2[algorithm]), 2))
        s3 = str(round(avgList(i3[algorithm]), 2))

        file2.write(s1 + l1 + '\n')
        file2.write(s2 + l2 + '\n')
        file2.write(s3 + l3 + '\n')
        
        file2.write(str(wins[algorithm]) + l4 + '\n')
        file2.write('\n')

    file2.close()

def main(argv):
    global searchAlgorithm
    #parse command line arguments
    parseArgs(argv)
    
    if Gmap is None:
        setMap()

    if verbose:
        print(Gmap)

    origins = []
    destinations = []
    if origin is None or destination is None: #do them all
        clearFile(open("solutions.txt", "w"))

        searchAlgorithm = searchAlgorithms 

        dests = ["Nice", "Calais", "Bordeaux", "Grenoble", "Paris", "Grenoble", "Brest", "Nantes", "Strasbourg"]
        orgs = ["Brest", "Montpellier", "Strasbourg", "Paris", "Grenoble", "Brest", "Grenoble", "Nice", "Caen"]

        for i in range(len(dests)):
            origins.append(Gmap.findNode(orgs[i]))
            destinations.append(Gmap.findNode(dests[i]))

    else:
        origins.append(Gmap.findNode(origin))
        destinations.append(Gmap.findNode(destination))

    print('Origins: ' + str(origins))
    print('Destinations: ' + str(destinations) + '\n')

    outPathl = {}
    vsl = {}
    ssl = {}
    frl = {}
    cstl = {}
    for algorithm in searchAlgorithm:
        outPathl[algorithm] = []
        vsl[algorithm] = []
        ssl[algorithm] = []
        frl[algorithm] = []
        cstl[algorithm] = []

    for i in range(len(origins)):
        for algorithm in searchAlgorithm:
            print('Algorithm: ' + algorithm + ', Origin: ' + origins[i].name + ', Destination: ' + destinations[i].name)

            Gmap.reset(verbose)
            
            #switch algo
            if algorithm == 'bfs':
                algo = bfs.BFS(Gmap, origins[i], destinations[i])
            elif algorithm == 'dls':
                algo = dls.DLS(Gmap, origins[i], destinations[i])
            elif algorithm == 'ucs':
                algo = ucs.UCS(Gmap, origins[i], destinations[i])
            elif algorithm == 'astar':
                algo = astar.AStar(Gmap, origins[i], destinations[i])

            ao = algo.search(verbose)
            outPath, vs, ss, fr = ao

            if verbose:
                f = 0
                for node in outPath:
                    print('Node ' + str(f) + ': ' + str(node) + ' Cost: ' + str(node.cost))
                    f += 1
            else:
                print('Path: ' + str([node.name for node in outPath]))

            print('\n')

            writeOut(outPath, vs, ss, fr, algorithm)

            outPathl[algorithm].append(outPath)
            vsl[algorithm].append(vs)
            ssl[algorithm].append(ss)
            frl[algorithm].append(fr)
            cstl[algorithm].append(destinations[i].cost)
    
    writeAvg(vsl, ssl, frl, cstl)

if __name__ == '__main__':
    main(sys.argv)