# Walugi

# Arguments
-S(earch) {bfs, dls, ucs, astar} // default is bfs, unless A and b are unspecified, then all
-A start // optional, but must be specified if B is specified
-B destination // optional, but must be specified if A is specified
-M(ap) file name of map. // default is ./france.txt


# Map
class that keeps track of the map

# City
class that keeps track of each city
default cities if a / b are not specified:
1. Brest -> Nice
2. Montpellier -> Calais
3. Strasbourg -> Bordeaux
4. Paris -> Grenoble
5. Grenoble -> Paris
6. Brest -> Grenoble
7. Grenoble -> Brest
8. Nice -> Nantes
9. Caen -> Strasbourg

# Agent
class that defines actions that an agent can take 
agent can use multiple different types of search:
1. Breadth-first search (bfs)
2. Iterative deepening depth-limited search (dls)
3. Uniform-cost search (ucs) 
4. A* search (astar)

# Step function 
should compute average per algorithm:
1. The average number of nodes explored or entered (i.e., the number of nodes removed
from the frontier)
2. The average number of nodes expanded (i.e., the total number of successors)
3. The average number of nodes maintained (i.e., stored in the frontier)
4. The number of times it found the optimal solution (optimal here is measured as “found
the best solution out of the four search algorithms)

# Output
outputs a list of cities
1. The number of nodes explored, entered, or visited (i.e., the number of nodes removed
from the frontier)
2. The number of nodes expanded (i.e., the total number of successors)
3. The number of nodes maintained (i.e., stored in the frontier)
If we are running all, save the output to a file called solution.txt
returns null if no path is found
and output the averages to README.txt

# copied from readme.txt
bfs
14.22 // avg visited
15.22 // avg successors
3.0 // avg frontier
2 // wins

dls
14.56 // avg visited
16.33 // avg successors
3.78 // avg frontier
2 // wins

ucs
14.89 // avg visited
15.67 // avg successors
2.78 // avg frontier
7 // wins

astar
6.0 // avg visited
10.78 // avg successors
6.78 // avg frontier
4 // wins

We can see that UCS gets the most wins, but also does the most work. A* is the most efficient, but only wins 4 times. I was pretty suprised that DLS did not do better, but I guessed at finding a limit. It is pretty clear why astar is a rockstar, with way way less exploration and still finding a good enough path.