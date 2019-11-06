from graph import Graph
from util import Queue, Stack

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for parent, child in ancestors:
        if parent not in graph.vertices:
            graph.add_vertex(parent)
        if child not in graph.vertices:
            graph.add_vertex(child)
        graph.add_edge(child, parent)

    return get_longest(graph, starting_node)


def get_longest(graph, starting_vertex):
    stack = Stack()
    visited = set()
    paths = []
    stack.push([starting_vertex])

    while stack.size() > 0:
        current_path = stack.pop()
        current_v = current_path[-1]

        if current_v not in visited:
            if len(graph.vertices[current_v]) == 0:
                visited.add(current_v)
                paths.append(current_path)
            else:
                visited.add(current_v)
                for next_v in graph.vertices[current_v]:
                    cpath_copy = list(current_path)
                    cpath_copy.append(next_v)
                    stack.push(cpath_copy)

    len_fin = list(zip([len(x) for x in paths], [x[-1] for x in paths]))
    if (len(len_fin) == 1) and (len_fin[0][0] == 1):
        return -1
    else:
        longest = 0
        final = 0
        for lon, fin in len_fin:
            if lon > longest:
                longest = lon
                final = fin
            elif lon == longest:
                if fin < final:
                    longest = lon
                    final = fin
        return final


    return

