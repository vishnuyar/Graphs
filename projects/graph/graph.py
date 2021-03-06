"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if (v1 in self.vertices) & (v2 in self.vertices):
            self.vertices[v1].add(v2)
        else:
            raise Exception("vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise Exception("vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        bft_queue = Queue()
        bft_queue.enqueue(starting_vertex)
        #visited.add(starting_vertex)
        while bft_queue.size() > 0:
            vertex = bft_queue.dequeue()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for neighbour in self.get_neighbors(vertex):
                    bft_queue.enqueue(neighbour)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        bft_stack = Stack()
        bft_stack.push(starting_vertex)
        #visited.add(starting_vertex)
        while bft_stack.size() > 0:
            vertex = bft_stack.pop()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for neighbour in self.get_neighbors(vertex):
                    bft_stack.push(neighbour)
   



    def dft_recursive(self, starting_vertex,visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        
        if visited is None:
            print(starting_vertex)
            visited = []
            visited.append(starting_vertex)
            for edge in self.get_neighbors(starting_vertex):
                    self.dft_recursive(edge,visited)
        else:
            if starting_vertex not in visited:
                print(starting_vertex)
                visited.append(starting_vertex)
                for edge in self.get_neighbors(starting_vertex):
                    self.dft_recursive(edge,visited)



    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        paths = []
        visited = set()
        bft_queue = Queue()
        bft_queue.enqueue([starting_vertex])
        while bft_queue.size() > 0:
            vertex_path = bft_queue.dequeue()
            print(vertex_path)
            vertex = vertex_path[-1]
            if vertex not in visited:
                visited.add(vertex)
                for neighbour in self.get_neighbors(vertex):
                    if neighbour == destination_vertex:
                        path.append(vertex_path.append(neighbour))
                    else:
                        bft_queue.enqueue(vertex_path.append(neighbour))
        print(path)
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('reached')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
