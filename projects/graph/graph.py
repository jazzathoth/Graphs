"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

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
        return
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if (v1 in self.vertices) and (v2 in self.vertices):
            self.vertices[v1].add(v2)
            #self.vertices[v2].add(v1)
        return

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()

        queue = Queue()

        queue.enqueue(starting_vertex)

        while queue.size() > 0:

            vert = queue.dequeue()
            if vert not in visited:
                print(vert, end=" ")
                visited.add(vert)
                for i in self.vertices[vert]:
                    queue.enqueue(i)
        print('\n\n')
        return

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        stack = Stack()

        stack.push(starting_vertex)

        while stack.size() > 0:
            current_v = stack.pop()

            if current_v not in visited:
                print(current_v, end=" ")
                visited.add(current_v)

                for nv in self.vertices[current_v]:
                    stack.push(nv)
        print('\n\n')
        return

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        visited = set()
        visited.add(starting_vertex)
        print(starting_vertex, end=" ")
        def dft_r(current_v):
            visited.add(current_v)
            print(current_v, end=" ")

            for nv_r in self.vertices[current_v]:
                if nv_r not in visited:
                    dft_r(nv_r)

        for nv in self.vertices:
            if nv not in visited:
                dft_r(nv)
        print('\n\n')
        return

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #Empty queue and enqueue a path to the starting vertex ID
        #Create a set to store visited verticies
        #While the queue is not empty
            #dequeue the first Path
            #get last vertex from path
            #If that vertex not visited
                # check if it is target. If so return path
                #Mark as visited
                #Add a path to it's neighbors to back of queue
                #Copy path
                #append the Neighbor to back
        #if non found return none

        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()

        while queue.size() > 0:
            path = queue.dequeue()

            current_v = path[-1]

            if current_v not in visited:
                if current_v == destination_vertex:
                    return path
                visited.add(current_v)

                for next_v in self.vertices[current_v]:
                    path_copy = list(path)
                    path_copy.append(next_v)
                    queue.enqueue(path_copy)
        print(path)
        print('\n')
        return path


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        stack = Stack()
        stack.push([starting_vertex])

        visited = set()

        while stack.size() > 0:
            path = stack.pop()

            current_v = path[-1]

            if current_v not in visited:
                if current_v == destination_vertex:
                    print(path)
                    return path
                else:
                    visited.add(current_v)
                    for next_v in self.vertices[current_v]:
                        path_copy = list(path)
                        path_copy.append(next_v)
                        stack.push(path_copy)


        print(path)
        return path





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
    #print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    #graph.dft(1)

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
    #graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    #graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    #print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
