#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 09:44:33 2017

@author: eddie
"""
import numpy as np
import networkx as nx
#import matplotlib.pyplot as plt
#import ast
#import json

SymMat = open("SymMat.txt",'r')
GrpSz = open("GrpSz.txt",'r')

Mat = SymMat.read()
sz = int(GrpSz.read())

Mat = Mat.replace(" ","")
Mat = Mat.replace("\n","")
Mat = Mat.replace("[","")
Mat = Mat.replace("]","")

Mat = Mat.split(",")

Mat = [float(i) for i in Mat]

Mat = [Mat[x:x+sz] for x in range(0, len(Mat), sz)]

Mat = np.array(Mat)

Mat = np.triu(Mat)

#Mat = json.loads(Mat)
#Mat = ast.literal_eval(Mat)

graph = nx.from_numpy_matrix(Mat)
graph.edges(data=True)

#layout = nx.circular_layout(graph)  # or whatever layout you wish   
#nx.draw_circular(graph)

#mapping = {0:r'$e$',1:r'$\delta$',2:r'$\sigma$',3:r'$\rho$',4:r'$\rho^2$',5:r'$\gamma$'}
#graph=nx.relabel_nodes(graph,mapping)

"""
edgeLabels = {}  # dictionary of node tuples to edge labels: {(nodeX, nodeY): aString}
for a, b in graph.edges():     # loop over all the edges
    edgeLabels[(a, b)] = str(graph.get_edge_data(a, b, {"weight":0})["weight"]) 
    
#nx.draw_networkx_edge_labels(graph,pos=layout, edge_labels=edgeLabels)
"""

#print(graph.edges())
#nx.draw(graph,with_labels=True)
nx.draw(graph, node_size=0.8)
