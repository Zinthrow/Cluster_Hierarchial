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
link_type = "A"
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
        cluster[y][x+2] = float(val)
    clust_avg[y] = clust_avg[y]/(x+1)

class Node(object):
    def __init__(self):
        self.gene_id = None
        self.name = None
        self.data = None
        self.avg = None
        self.leaf = True
        self.parent = None
        self.child = None
        self.val = None
        self.height = 0
    def set_data(self,cluster,clust_avg):
        self.gene_id = cluster[0]
        self.name = cluster[1]
        self.data = cluster[2:]
        self.avg = clust_avg
    
class clust(object):
    def __init__(self):
        self.leaf = False
        self.parent = None
        self.child = None
        self.avg = None
        self.val = None
        self.height = 0
        
class clustering(object):
    def __init__(self):
        self.cluster_count = 0
        self.clusters = []
    def insert(self, cluster,clust_avg,link_type):
        for a, b in zip(cluster, clust_avg):
            current = Node()
            current.set_data(a,b)
            self.clusters.append(current)
            self.cluster_count += 1
            if link_type == 'A':
                current.val = current.avg
            elif link_type == 'S':
                current.val = min(current.data)
            elif link_type == 'C':
                current.val = max(current.data)   
            
    #def update(self, cluster_a, cluster_b, val):
    #def find_clust(self,link_type,k):    
    def link(self, link_type, k):
        if link_type == 'A':
            while self.cluster_count > k:
                close = clust()
                close.val = float('inf')
                dist = {}
                for a in self.clusters:
                    for b in self.clusters:
                        difference =abs(a.val-b.val)
                        if a not in dist:
                            dist[a] = []
                            dist[a].append([difference, b])
                        else:
                            dist[a].append(difference)
                    iota = [float('inf'), None]
                    for c in dist:
                        if dist[c][0] < iota[0]:
                            iota = dist[c]
                    close_a =  (min(dist, key =lambda x: dist[x]))
                    if close_a.val < close.val:
                        close = close_a
                    
            
c = clustering()
c.insert(cluster,clust_avg)



#small_a =  min(dist, key =lambda x: x.avg)

        
