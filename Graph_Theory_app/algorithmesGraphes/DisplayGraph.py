import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def DisplayGraph(matrix, graphType,nodesNumber):
    mat = np.array(matrix)
    if graphType == "dn":
        G = nx.from_numpy_array(mat, create_using=nx.DiGraph)
    if graphType == "un":
        G = nx.from_numpy_array(mat, create_using=nx.Graph)
    if graphType == "dp":
        G = nx.from_numpy_array(mat, create_using=nx.DiGraph)
    if graphType == "up":
        G = nx.from_numpy_array(mat, create_using=nx.Graph)
    mapping = {}
    for i in range(int(nodesNumber)):
        mapping[i] = chr(65 + i)
    nx.relabel_nodes(G, mapping, copy=False)
    if graphType == "dp" or graphType == "up":
        layout = nx.spring_layout(G)
        nx.draw(G, layout, with_labels=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)
    if graphType == "dn" or graphType == "un":
        nx.draw(G, with_labels=True)
    return plt.show()


nodesNumber=3
graphType="dp"
mat=[[0,1,0],
     [0,0,1],
     [1,0,0]]

DisplayGraph(mat,graphType,nodesNumber)

