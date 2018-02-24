def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append([node, neighbour])

    return edges

#graph = {'0': [1, 2], '1': [0], '2': [0]}

def simplify_edges(edges):
    simplified_edges = [ ]
    for edge in edges:
#        print('edge : ', edge)
#        print(type(edge[0]))
#        print(type(edge[1]))
#        print('if ', [edge[0], edge[1]],    [str(edge[1]), int(edge[0])])
        if (  [edge[0], edge[1]] and [str(edge[1]), int(edge[0]) ] ) not in simplified_edges:
            simplified_edges = simplified_edges + [edge]
    return simplified_edges


#edges = generate_edges(graph)
#print('edges', edges)
#s = simplify_edges(edges)
#print('simplified edges  :  ',  s)
