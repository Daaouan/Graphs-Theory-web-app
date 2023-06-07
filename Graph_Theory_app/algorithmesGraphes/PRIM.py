import base64
from cmath import inf
import io
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import matplotlib
matplotlib.use('agg')

def PRIM(matrix, nodesNumber, graphType):
    matrix = np.array(matrix)
    new_graph = {}
    no_edge = 0
    selected_node = [False] * nodesNumber
    selected_node[0] = True
    ACM = 0 

    # printing for edge and weight
    while (no_edge < nodesNumber - 1):
        edges = []
        minimum = inf
        a = 0
        b = 0
        for m in range(nodesNumber):
            if selected_node[m]:
                for n in range(nodesNumber):
                    if ((not selected_node[n]) and matrix[m][n]):
                        # not in selected and there is an edge
                        if minimum > matrix[m][n]:
                            minimum = matrix[m][n]
                            a = m
                            b = n
        if chr(65 + a) in new_graph:
            edges = new_graph[chr(65 + a)]
        edges.append((chr(65 + b), matrix[a][b]))
        new_graph[chr(65 + a)] = edges
        selected_node[b] = True
        no_edge += 1
        ACM += matrix[a][b]
    # Convert to array
    plt.clf()
    graph = []
    for n in new_graph:
        node = new_graph[n]
        for l in node:
            edge = (n, l[0], l[1])
            graph.append(edge)

    if graphType == "up":
            G = nx.Graph()

    mapping = {}
    for i in range(int(nodesNumber)):
        mapping[i] = chr(65 + i)
    nx.relabel_nodes(G, mapping, copy=False)
    G.add_weighted_edges_from(graph)
    layout = nx.spring_layout(G)
    nx.draw(G, layout, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)
    print("ACM:", ACM)   
        # Convert the graph image to a base64-encoded string
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    graph_image = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    # Return the graph image as JSON response
    return graph_image

