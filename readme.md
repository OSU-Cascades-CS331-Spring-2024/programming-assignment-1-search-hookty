# Walugi

# Arguments
-S(earch) {bfs, dls, ucs, astar} // default is bfs, unless A and b are unspecified, then all
-A start // optional
-B destination // optional
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