"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

#  Vertex
#  Identifier (int, string, ect... )
#  Edges

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            f'Warning, vertex exists already.'
    def add_edge(self, vertex_from, vertex_to):
        """
        Add a directed edge to the graph.
        """
        if vertex_from in self.vertices and vertex_to in self.vertices:
            self.vertices[vertex_from].add(vertex_to)
        else: 
            print("Warning: this vertex does not exist.")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()

        q.enqueue(starting_vertex)

        found = [starting_vertex, ]

        while q.size() > 0:
            for vertex in self.vertices[q.queue[0]]:
                if vertex not in found:
                    q.enqueue(vertex)
                    found.append(vertex)

            q.dequeue()

            print(f'BTF: {found}')

    def dft(self, starting_vertex):
        s = Stack()

        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:
            v = s.pop()

            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.vertices[v]:
                    s.push(next_vert)

        print(f'DFT: {visited}')

    def dft_recursive(self, starting_vertex, cache = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if starting_vertex not in cache:
            print(starting_vertex)
            cache.add(starting_vertex)
            if len(self.vertices[starting_vertex]) > 0:
                for neighbor in self.vertices[starting_vertex]:
                    self.dft_recursive(neighbor, cache)
        # print(f'cache:{cache}')
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q= Queue()
        q.enqueue([starting_vertex])
        visited = set()
        while q.size() > 0:
            path = q.dequeue()
            vertex = path[-1]
            if vertex == destination_vertex:
                return path
            elif vertex not in visited:
                visited.add(vertex)
                for neighbor in self.vertices[vertex]:
                    new_path = path[:]
                    new_path.append(neighbor)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()

        s.push([starting_vertex])

        visited = set()

        while s.size() > 0:
            path = s.pop()
            vertex = path[-1]

            if vertex == destination_vertex:
                return path

            elif vertex not in visited:
                visited.add(vertex)

                if destination_vertex in self.vertices[vertex]:
                    path.append(destination_vertex)
                    return path

                for neighbor in self.vertices[vertex]:
                    new_path = path[:]
                    new_path.append(neighbor)
                    s.push(new_path)





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
