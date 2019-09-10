# Graphs

## Objectives

* [Graph Intro](objectives/graph-intro)
* [Graph Representations](objectives/graph-representations)
* [Breadth First Search](objectives/breadth-first-search)
* [Depth First Search](objectives/depth-first-search)
* [Randomness](objectives/randomness)
* [Connected Components](objectives/connected-components)

## Projects

### Day 1
* [Graph Traversal and Search](projects/graph)

#### NOTES

# Graphs - Day One

#### Important Info:
  - "A graph is simply a set of linked data represents by vertices and edges"
  - Vertices and edges can be linked together under very loose requirements.

#### Graphs are useful for representing:
  * Networks or sets of connected objects
  * Multiway relational data
      Some examples include
        - A collection of cities and linking roads or metros
        - A collection of computers on a network
        - A population of people who know each other (Kevin Bacon)
        - A trade relationship between nations

## What are graphs?
  - A collection of related data
  - Similar to trees
  - Connections can be made from any node to any other node
  - "All trees are graphs, but not all graphs are trees."

![1cece3c1.png](:storage/5346452b-7925-4e66-bf88-4156e9aad80a/1cece3c1.png)

## What are the components of a graph?
  *** An edge denotes a relationship / linkage between the two verts
  - VERTEXES, VERTICES, OR VERTS: The nodes in a graph
  - EGDES: The connections between the verts

![10cdf0a6.png](:storage/5346452b-7925-4e66-bf88-4156e9aad80a/10cdf0a6.png)

  
## What are the types of graphs?
The main graphs we'll be going over are undirected, directed, cyclic, weighted graphs, and DAG.

![c4f14934.png](:storage/5346452b-7925-4e66-bf88-4156e9aad80a/c4f14934.png)

#### Directed 
  - If the edges are "one way" (linear), the graph is said to be a directed graph.

![062b3793.png](:storage/5346452b-7925-4e66-bf88-4156e9aad80a/062b3793.png)

#### Undirected
  - If there are no clear lines, the edges are bidirectional and the graph is undirected.

![91c37e1f.png](:storage/5346452b-7925-4e66-bf88-4156e9aad80a/91c37e1f.png)

#### Cyclic / Acyclic
  - If a cycle can be formed the graph is cyclic. For example:
    - If you can follow the edges and arrive again at a vert you have already visited

![639e9e60.png](:storage/5346452b-7925-4e66-bf88-4156e9aad80a/639e9e60.png)

  - If not, it is acyclic

![dafcdc1a.png](:storage/5346452b-7925-4e66-bf88-4156e9aad80a/dafcdc1a.png)


#### Weighted graphs
  - Graphs with values (weights) associates with the edges
  - The type of graph determines the meaning of the weight
  - Weights can be used to decide if a particular route should be chosen over another
  - For example
    - A graph might have a weight to represent the length of a road. The higher the total weight of a route on the graph, the longer the trip is.
  - Weight CAN be modified!! (Google adjusting traffic times on maps)

![daf7c749.png](:storage/5346452b-7925-4e66-bf88-4156e9aad80a/daf7c749.png)

#### Directed Acyclic Graphs (DAGs)
A DAG is a collection of all the tasks you wants to run in an organized way that reflects their relationships and dependencies.

For example, a DAG could consist of three tasks: A, B, and C. A DAG describes how you want to carry out your workflow. A, B, and C could be any tasks but the IMPORTANT thing is that that the DAG is not concerned with WHAT tasks it's given; it's job is to make sure they happen in the right order, the right time, and account for any handling of unexpected issues.
  

![5f02d821.png](:storage/5346452b-7925-4e66-bf88-4156e9aad80a/5f02d821.png)








### Useful Links
- [Cyclic, Acyclic, Sparse & Dense Graphs \| Study.com](https://study.com/academy/lesson/cyclic-acyclic-sparse-dense-graphs.html)

- [Social Network for Developers](https://morioh.com/p/e78aa5350ce2/a-review-of-basic-algorithms-and-data-structures-in-python-graph-algorithms)

- [Concepts — Airflow Documentation](https://airflow.apache.org/concepts.html)


### Day 2
* [Earliest Ancestor](projects/ancestor)

#### NOTES :

# Graphs - Day Two

Learn how to describe a depth-first search and its uses, and can manually run a DFS on a graph

#### "While BFS can be a good strategy for searching a graph, there are some scenarios where BFS is inefficient (for example, if the target node is near the bottom of a tree). To optimize the performance of your applications, it is important to understand when using depth-first search (DFS) will produce better results."

### Depth First Search
  - Searches as far down as it can go before backtracking and searching down the next branch.
  - Never attempts to explore a vert that it either has explored or is exploring.
  

#### Example:
  When starting from the upper left, the numbers on this graph show a vertex visitation order in a DFS:
![https://github.com/LambdaSchool/Graphs/raw/master/objectives/depth-first-search/img/dfs-visit-order.png](:storage/9d72b6e5-dbed-4878-8879-18319d7bbf27/194298d9.png)
KEY:
  - BOLD: Edges were followed
  - THIN: Edges were NOT followed because their destination nodes had already been visited

### Applications of DFS:

#### Finding Minimum Spanning Trees of Weighted Graphs

###### What is a Minimum Spanning Tree?

[Minimum spanning trees](https://www.ics.uci.edu/~eppstein/161/960206.html)

[Minimum Spanning Tree Tutorials & Notes \| Algorithms | HackerEarth](https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/)

The best example of a Minimum Spanning Tree is the "traveling salesman problem". The goal is to find the shortest path that visits each point at least once.

  - The spanning tree where the cost is minimum among all the spanning trees. 
  - There can be many minimum spanning trees


#### Path Finding

(http://ww3.algorithmdesign.net/handouts/DFS.pdf)

  - We can specialize the DFS algorithm to find a path between two given vertices u and z using the template method pattern
  - We call DFS(G, u) with u as the starting vertex
  - We use a stack S to keep track of the path between the starting vertex and the current vertex
  - As soon as destination vertex z is encountered, we return the path as the contents of the stack

```
Algorithm pathDFS(G, v, z)
  setLabel(v, VISITED)
  S.push(v)
  if v = z
    return S.elements()
  for all e ∈ G.incidentEdges(v)
    if getLabel(e) = UNEXPLORED
      w ← opposite(v, e)
      if getLabel(w) = UNEXPLORED
        setLabel(e, DISCOVERY)
        S.push(e)
        pathDFS(G, w, z)
        S.pop() { e gets popped }
      else
        setLabel(e, BACK)
  S.pop() { v gets popped }
```


#### Detecting Cycles in Graphs

  - We can specialize the DFS to find a simple cycle using the template method pattern
  - We use a stack S to keep track of the starting vertex and the current vertex
  - As soon as a back edge (v, w) is encountered, we return the cycle as the potion of the stack from the top to vertex "w"

```
Algorithm cycleDFS(G, v, z)
  setLabel(v, VISITED)
  S.push(v)
  for all e ∈ G.incidentEdges(v)
    if getLabel(e) = UNEXPLORED
      w ← opposite(v,e)
      S.push(e)
      if getLabel(w) = UNEXPLORED
        setLabel(e, DISCOVERY)
        pathDFS(G, w, z)
        S.pop()
    else
      C ← new empty stack
      repeat
        o ← S.pop()
        C.push(o)
      until o = w
        return C.elements()
  S.pop()
```

#### Topographical Sorting
[Topological Sorting - GeeksforGeeks](https://www.geeksforgeeks.org/topological-sorting/)
  - This is useful for scheduling sequences of dependent jobs
  - Topological Sorting for a graph is ONLY possible if the graph is a DAG

###### Topological Sorting vs Depth First Traversal (DFS):
![646415ab.png](:storage/9d72b6e5-dbed-4878-8879-18319d7bbf27/646415ab.png)

  - In Topological Sorting, we need to print a vertex before its adjacent vertices. 
  - Example: in the graph above, the vertex '5' should be printed before vertex '0', but unlike the DFS, the vertex '4' should also be printed before vertex '0'

###### Algorithm to find Topological Sorting 
 - In Topological Sorting, we use a temporary stack
 - Don't print the vertex immediately!!!
 - First, recursively call topographical sorting for all its adjacent vertices
 - Then, push it to a stack
 - Finally, print the contents of the stack
 - *** A vertex is pushed to a stack only when all of its adjacent vertices (and their adjacent vertices and so on) are already in the stack

![ad5c3c2f.png](:storage/9d72b6e5-dbed-4878-8879-18319d7bbf27/ad5c3c2f.png)

```
#Python program to print topological sorting of a DAG 
from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # A recursive function used by topologicalSort 
    def topologicalSortUtil(self,v,visited,stack): 
  
        # Mark the current node as visited. 
        visited[v] = True
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        # Push current vertex to stack which stores result 
        stack.insert(0,v) 
  
    # The function to do Topological Sort. It uses recursive  
    # topologicalSortUtil() 
    def topologicalSort(self): 
        # Mark all the vertices as not visited 
        visited = [False]*self.V 
        stack =[] 
  
        # Call the recursive helper function to store Topological 
        # Sort starting from all vertices one by one 
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        # Print contents of the stack 
        print stack 
  
g= Graph(6) 
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 
  
print "Following is a Topological Sort of the given graph"
g.topologicalSort() 
```

```
g= Graph(6) 
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 
  
print "Following is a Topological Sort of the given graph"
g.topologicalSort() 
```
Output:
```
Following is a Topological Sort of the given graph
5 4 2 3 1 0
```

##### Applications:
  - Instruction scheduling
  - Ordering of formula cell evaluation when recomputing formula values in spreadsheets
  - Logic synthesis
  - Data serialization


#### DFS and Maze Traversal

[Solving mazes using Python: Simple recursivity and A* search \| Laurent Luce's Blog](https://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search/)

[Recursion: Solving a Maze](https://www.cs.bu.edu/teaching/alg/maze/)
  - The DFS algorithm is similar to a classic strategy for exploring a maze
    - We mark each intersection, corner and dead end (vertex) visited
    - We mark each corridor (edge) traversed
    - We keep track of the path back to the entrance (starting vertex) by means of a 'rope' (recursion stack)



#### Coloring Vertexes

As The graph is explored, it's useful to color verts as you are searching and they have been searched
  - Unvisited: White
  - Currently Being Explored: Gray
  - No Unexplored Neighbors: Black

#### Recursion
Since we want to explore as much of the graph as possible, and the 'back up' to an earlier branch point to explore that way, recursion is a good approach to keep track of where we left off.

###### Example:
```
explore(graph) {
    visit(this_vert);
    explore(remaining_graph);
}
```

### Pseudocode for DFS

```
DFS(graph):
    for v of graph.verts:
        v.color = white
        v.parent = null

    for v of graph.verts:
        if v.color == white:
            DFS_visit(v)

DFS_visit(v):
    v.color = gray

    for neighbor of v.adjacent_nodes:
        if neighbor.color == white:
            neighbor.parent = v
            DFS_visit(neighbor)

    v.color = black
```

#### "When searching a graph, one of the approaches is called breadth-first search. This explores the graph outwards in rings of increasing distance from the starting vertex."

Learn to describe what breadth-first search and its uses, and can manually run a sample BFS

### Breadth-first Search
  - The algorithm never attempts to explore a vert that it either has or is exploring. 

For example,  when starting from the upper left, the numbers on this graph show a vertex visitation order in a BFS:

![1628f277.png](:storage/9d72b6e5-dbed-4878-8879-18319d7bbf27/1628f277.png)

- BOLD: edges were followed
- THIN: Edges were NOT followed because their destination nodes had already been visited

### USES OF BFS

[Applications of Breadth First Traversal - GeeksforGeeks](https://www.geeksforgeeks.org/applications-of-breadth-first-traversal/)

#### Pathfinding, Routing
  - To find a path between two verts
  - This implementation returns all possible paths between two verticxes, the first being the shortest


```
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

list(bfs_paths(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
```
  
  - Knowing that the shortest path will be returned first from the BFS path generator method, we can create a useful method with simply returns the shortest path or "None" if no path exists

```
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

shortest_path(graph, 'A', 'F') # ['A', 'C', 'F']
```

#### Find neighbor nodes in a P2P network like Bittorrent

In Peer to Peer Networks like BitTorrent, BFS is used to find all the neighbor nodes.

#### Web Crawlers

Crawlers build index using BFS. The idea is to start from source page and follow all links from the source.

#### Finding People 'n' connections away on a social site

In social networks, we can find people within a given distance 'k' from a person using BFS until 'k' levels.

#### Find Neighboring Locations on a Graph

BFS is used to find all neighboring locations.


#### Broadcasting in a Network

In networks, a broadcasted packet follows BFS to reach all nodes.

#### Cycle Detection in a Graph

BFS can be used to detect a cycle in UNDIRECTED graphs.
```
# Python Program to detect cycle in an undirected graph 
  
from collections import defaultdict 
   
#This class represents a undirected graph using adjacency list representation 
class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
  
   
    # function to add an edge to graph 
    def addEdge(self,v,w): 
        self.graph[v].append(w) #Add w to v_s list 
        self.graph[w].append(v) #Add v to w_s list 
   
    # A recursive function that uses visited[] and parent to detect 
    # cycle in subgraph reachable from vertex v. 
    def isCyclicUtil(self,v,visited,parent): 
  
        #Mark the current node as visited  
        visited[v]= True
  
        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            # If the node is not visited then recurse on it 
            if  visited[i]==False :  
                if(self.isCyclicUtil(i,visited,v)): 
                    return True
            # If an adjacent vertex is visited and not parent of current vertex, 
            # then there is a cycle 
            elif  parent!=i: 
                return True
          
        return False
           
   
    #Returns true if the graph contains a cycle, else false. 
    def isCyclic(self): 
        # Mark all the vertices as not visited 
        visited =[False]*(self.V) 
        # Call the recursive helper function to detect cycle in different 
        #DFS trees 
        for i in range(self.V): 
            if visited[i] ==False: #Don't recur for u if it is already visited 
                if(self.isCyclicUtil(i,visited,-1))== True: 
                    return True
          
        return False
  
# Create a graph given in the above diagram 
g = Graph(5) 
g.addEdge(1, 0) 
g.addEdge(0, 2) 
g.addEdge(2, 0) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 
  
if g.isCyclic(): 
    print "Graph contains cycle"
else : 
    print "Graph does not contain cycle "
g1 = Graph(3) 
g1.addEdge(0,1) 
g1.addEdge(1,2) 
  
  
if g1.isCyclic(): 
    print "Graph contains cycle"
else : 
    print "Graph does not contain cycle "
```

#### Finding Connected Components

BFS can be used to find if there is a path between two vertices.

#### Solving a Number of Theoretical Graph Problems


#### Coloring Vertexes

As The graph is explored, it's useful to color verts as you are searching and they have been searched
  - Unvisited: White
  - Currently Being Explored: Gray
  - No Unexplored Neighbors: Black

#### Keeping Track of What We Need to Explore 
In BFS, it's useful to track which nodes we still need to follow up on. For example, in the diagram above, when we get to node 2, we need to explore node 3 and 4 in the future, in order.

We can track that by adding neighbors to a queue, and then exploring the verts in that queue.

### Psudocode for BFS:
```
BFS(graph, startVert):
  for v of graph.vertexes:
    v.color = white

  startVert.color = gray
  queue.enqueue(startVert)

  while !queue.isEmpty():
    u = queue[0]  // Peek at head of queue, but do not dequeue!

    for v of u.neighbors:
      if v.color == white:
        v.color = gray
        queue.enqueue(v)

    queue.dequeue()
    u.color = black
```

`Why can't we use recursion for BFT?`

We can't use recursion for BFT because in order to fully complete the traversal, we have to visit each node. BFT travels across all of the nodes before going down into a deeper level so to properly traverse, we must "backtrack".

### Day 3
* [Random Social Network](projects/social)

#### NOTES:

# Graphs - Day Three

Learn to demonstrate and show understanding of randomness and its applications.

#### "Randomness has a variety of uses, from algorithm optimization to seeding with robust test data. Understanding the applications of randomness and pseudo-randomness will allow us to utilize randomness as an effective tool when it is appropriate."

### How Random is Random?
  - Most 'random' data generated with Python is not fully random.
  - PRNG: Pseudo-Random Number Generator
  - Any algorithm for generating seemingly random but still reproducible data.
  - TRNG: True Random Number Generator


### PRNGs in Python
##### The random Module

The random.random() function returns a random float in the interval [0.0, 1.0). 

```
# Don't call `random.seed()` yet
import random
random.random()

random.random()
```

With random.seed(), you can make results reproducible, and the chain of calls after random.seed() will produce the same trail of data.

```
random.seed(444)
random.random()
0.3088946587429545


random.random()
0.01323751590501987

random.seed(444)  # Re-seed
random.random()
0.3088946587429545


random.random()
0.01323751590501987
```


With random.randint(), you can generate a random integer between two endpoints.

```
random.randint(0, 10)

random.randint(500, 50000)
```


With random.randrange(), you can exclude the right-hand side of the interval, meaning the generated number always lies within [x, y) and will always be smaller than the right endpoint:

```
random.randrange(1, 10)
```

With random.uniform(), you can generate random floats that lie within a specific [x, y] interval.

```
>>> random.uniform(20, 30)
27.42639687016509
>>> random.uniform(30, 40)
36.33865802745107
```

To pick a random element from a non-empty sequence (list / tuple), you can use random.choice(). For choosing multiple elements from a sequence with replacement (dups are possible), use random.choices().

```
>>> items = ['one', 'two', 'three', 'four', 'five']
>>> random.choice(items)
'four'

>>> random.choices(items, k=2)
['three', 'three']
>>> random.choices(items, k=3)
['three', 'five', 'four']
```

To mimic sampling w/o replacement, use random.sample()

```
>>> random.sample(items, 4)
['one', 'five', 'four', 'three']
```

random.shuffle() will randomize a sequence in-place by modifying the sequence object and randomize the order of elements

```
>>> random.shuffle(items)
>>> items
['four', 'three', 'two', 'one', 'five']
```


### Day 4
* [Adventure Map Traversal](projects/adventure)
