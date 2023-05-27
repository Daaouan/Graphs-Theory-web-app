import base64
import io
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.figure import Figure


@csrf_exempt
def first(request):
    return render(request,"first.html")

@csrf_exempt
def index(request):
    return render(request,"index.html")


@csrf_exempt
def save_matrix_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        dimension = data['dimension']
        matrix= data['matrix']

        

        # Save the JSON data to a file within your project's file system
        with open('file.json', 'w') as file:
            file.write(json.dumps(data))

        
        with open('file.json', 'r') as file:
            contents = file.read()

        js = json.loads(contents)
        dim = js['dimension']
        matr= js['matrix']
        GraphType=js['GraphType']
        graph_image=DisplayGraph(matr, GraphType,dim)
        # Generate and save the graph image
         
        return JsonResponse({'graph_image': graph_image})
    
        # Return the image file in the response
        
        
    # Return an error response for non-POST requests
    response_data = {'error': 'Invalid request method'}
    return JsonResponse(response_data, status=400)

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

    plt.clf()
    if graphType == "dp" or graphType == "up":
        layout = nx.spring_layout(G)
        nx.draw(G, layout, with_labels=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)
    if graphType == "dn" or graphType == "un":
        nx.draw(G, with_labels=True)
    
    # Convert the graph image to a base64-encoded string
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    graph_image = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    # Return the graph image as JSON response
    return graph_image
