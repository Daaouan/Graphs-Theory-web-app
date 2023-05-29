import base64
import io
import matplotlib.pyplot as plt
import networkx as nx
from numpy import mat
import matplotlib
matplotlib.use('agg')

def WARSHALL(matrix,nodesNumber,graphType):

    # Convert to dict
    graph = {}
    for i in range(nodesNumber):
        edges = []
        for j in range(nodesNumber):
            if matrix[i][j] != 0:
                edges.append(chr(65 + j))
        graph[chr(65 + i)] = edges
    # Warshall
    new_graph = graph
    pre = 0
    suc = 0
    for n in graph:
        suc = graph[n]
        for m in graph:
            if n in graph[m]:
                pre = m
                for s in suc:
                    if s not in graph[pre]:
                        new_graph[pre].append(s)
    # Convert to array
    plt.clf()
    graph = []
    for n in new_graph:
        node = new_graph[n]
        for nodeList in node:
            edge = (n, nodeList[0])
            graph.append(edge)

    # Plot the graph
    if graphType == "dp" or graphType == "dn":
        G = nx.DiGraph()
    if graphType == "up" or graphType == "un":
        G = nx.Graph()

    mapping = {}
    for i in range(int(nodesNumber)):
        mapping[i] = chr(65 + i)
    nx.relabel_nodes(G, mapping, copy=False)
    G.add_edges_from(graph)
    
    nx.draw(G, with_labels=True)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    graph_image = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    # Return the graph image as JSON response
    return graph_image
    

# nodesNumber=3
# graphType="dp"
# mat=[[0,1,0],
#      [0,0,1],
#      [1,0,0]]

# WARSHALL(mat,nodesNumber,graphType)
