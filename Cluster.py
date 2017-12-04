#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:28:42 2017

@author: alex
"""
import os
import sys


#user_input = sys.argv
#data_file = user_input[1]
#link_type = user_input[2]
#k = user_input[3]

data_file = "tiny-yeast.tsv"
link_type = "S"
k = 2

if os.path.exists(data_file):
    lines = open(data_file, 'r') 
    lines = lines.readlines()

cluster = []
for x,lin in enumerate(lines):
    cluster.append(lin.split(sep='\t'))
    cluster[x][-1] = cluster[x][-1].rstrip()


clust_avg = []
x_len = 0
for y,s in enumerate(cluster):
    clust_avg.append(0)
    for x,val in enumerate(s[2:]):
        clust_avg[y] += float(val)
    clust_avg[y] = clust_avg[y]/(x+1)

class Node(object):
    def __init__(self):
        self.gene_id = None
        self.name = None
        self.data = None
        self.clust_avg = None
        self.leaf = True
        self.parent = None
        self.child = None
    def set_data(self,cluster,clust_avg):
        self.gene_identifier = cluster[0]
        self.name_description = cluster[1]
        self.data = cluster[2:]
        self.clust_avg = clust_avg
    
class clust(object):
    def __init__(self):
        self.leaf = False
        self.parent = None
        self.child = None
    def get_leaf(self):
        return self.leaf
class clustering(object):
    def __init__(self):
        self.cluster_count = 0
        self.clusters = []
    def insert(self, cluster,clust_avg):
        for a, b in zip(cluster, clust_avg):
            current = Node()
            current.set_data(a,b)
            self.clusters.append(current)
            
c = clustering()
c.insert(cluster,clust_avg)
for x in c.clusters:
    print (x)

           
