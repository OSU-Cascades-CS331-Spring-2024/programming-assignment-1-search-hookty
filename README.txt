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

We can see that UCS gets the most wins, 
but also does the most work. A* is the most efficient, 
but only wins 4 times. I was pretty 
suprised that DLS did not do better, 
but I guessed at finding a limit. 
It is pretty clear why astar is a rockstar, 
with way way less exploration and still finding a good enough path.