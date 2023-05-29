import base64
import io
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def DFS(matrix,source):

    mat = np.array(matrix)
    plt.clf()
    G = nx.from_numpy_array(mat, create_using=nx.DiGraph)
    nodesNumber=mat.shape[0]
    print(nodesNumber)
    mapping = {}
    for i in range(int(nodesNumber)):
        mapping[i] = chr(65 + i)
    nx.relabel_nodes(G, mapping, copy=False)
    # affichage d'arbre DFS si le graphe est direct
    tree = nx.dfs_tree(G, source)
    print(tree.edges())
    # create table of nodes DFS
    tab = []
    flag=0
    for edg in tree.edges():
        if(flag == 0) :
            tab.append(edg[0])
        flag = 1
        tab.append(edg[1])
    nx.relabel_nodes(tree, mapping, copy=False)
    nx.draw(tree, with_labels=True)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    graph_image = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    # Return the graph image as JSON response
    return graph_image

# mat=[[0,1,0],
#      [0,0,1],
#      [1,0,0]]
# source="B"

# Dfs(mat,source)
