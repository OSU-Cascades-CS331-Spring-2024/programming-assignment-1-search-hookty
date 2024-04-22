import os
import math

class Node:
    def __init__(self, name, lat, lon, neighbors = {}):
        #lat and lon are in dms, like (degrees, minutes, seconds, direction)
        self.lat = lat 
        self.latD = 0

        self.lon = lon
        self.lonD = 0

        x, y = self.convertToXY(lat, lon)
        
        self.x = x
        self.y = y
        self.cost = 0
        self.name = name.lower()
        self.neighbors = neighbors

    def addNeighbor(self, neighbor, travelDistance):
        self.neighbors[neighbor] = travelDistance

    def __str__(self):
        return str(self.name + ' ' + str(round(self.latD, 2)) + ' ' + str(round(self.lonD, 2)) + ' ' + str(self.cost))
    
    def __repr__(self):
        return str(self)
    
    def dmsToDecimal(self, dms):
        #converts degrees, minutes, seconds to decimal
        mToD = 1/60
        sToD = 1/3600
        
        #switch on the directions N, S, E, W
        if dms[-1].lower() == 'n' or dms[-1].lower() == 'e':
            sign = 1
        else:
            sign = -1
        
        return sign * (int(dms[0]) + int(dms[1]) * mToD + int(dms[2]) * sToD)

    def convertToXY(self, lat, lon):
        #latitudes range from 90 to -90
        #longitudes range from 180 to -180

        dlat = self.dmsToDecimal(lat)
        dlon = self.dmsToDecimal(lon)

        self.latD = dlat
        self.lonD = dlon

        #convert to radians
        lat = math.radians(dlat)
        lon = math.radians(dlon)

        r = 6378 #radius of the earth in km

        x = r * math.cos(lat) * math.cos(lon)
        y = r * math.cos(lat) * math.sin(lon)

        return x, y
    
    def distanceToR(self, node):
        return math.sqrt((self.x - node.x)**2 + (self.y - node.y)**2)
    
    def distanceTo(self, node):
        #scales back to kilometers from x, y
        return self.distanceToR(node) * 1000
    
    def findNeighbor(self, name):
        for neighbor in self.neighbors:
            if neighbor.name == name.lower():
                return neighbor
        return None
    
    def findClosestNeighbor(self):
        closest = None
        for neighbor in self.neighbors:
            if closest is None or self.neighbors[neighbor] < self.neighbors[closest]:
                closest = neighbor
        return closest
    
class Map:
    def __init__(self, filename):
        self.nodes = []
        self.loadMap(filename)
        
    def loadMap(self, filename):
        sep = '-->'
        delim = 'va-'

        # sep[0] is cityname d m s n/s d m s e/w, space delimited
        # sep[1] is many cityname travelDistance, space delimited
            
        with open(filename, 'r') as file:
            for line in file:
                
                #split the line into two parts
                parts = line.split(sep)
                
                #split sep[0] into cityname and lat/lon
                s1 = parts[0].split(' ')
                name = s1[0]
                lat = s1[1:5]
                lon = s1[5:9]

                neighbors = {}
                s2 = parts[1].split(delim)
                for neighbor in s2:
                    if neighbor in ['\n', '', ' ']:
                        continue
                    elif neighbor.find('\n') != -1:
                        neighbor = neighbor.replace('\n', '')

                    n = neighbor.split(' ')
                    neighbors[n[0]] = int(n[1])

                self.nodes.append(Node(name, lat, lon, neighbors))

    def findNode(self, name):
        if type(name) is Node:
            name = name.name
        for node in self.nodes:
            if node.name == name.lower():
                return node
        print('Node ' + name + ' not found in ' + str(self.nodes))
        return None
    
    def reset(self, verbose = False):
        for node in self.nodes:
            if verbose and node.cost != 0:
                print('Final Cost of ' + str(node) + ': ' + str(node.cost))
            node.cost = 0
    
    def __str__(self):
        string = ''
        for node in self.nodes:
            string += str(node) + '\n'
            for neighbor in node.neighbors:
                string += '\t' + str(neighbor) + ' ' + str(node.neighbors[neighbor]) + '\n'

        return string

    def __repr__(self):
        return str(self)