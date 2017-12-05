#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:28:42 2017

@author: alex
"""
import os
import sys

#Takes the user input from an .sh script and uses those parameters
user_input = sys.argv 
data_file = user_input[1] #specify which tsv file you want to draw from
link_type = user_input[2] #link type, options are "S" "C" and "A"
k = int(user_input[3]) # how many clusters do you want the program to consolidate to

#data_file = "tiny-yeast.tsv" # test tsv file
#link_type = "C" # test link_type 
#k = 2 # test k number


if os.path.exists(data_file): #opens .tsv 
    lines = open(data_file, 'r') 
    lines = lines.readlines()

cluster = [] #process data and remove extra characters
for x,lin in enumerate(lines):
    cluster.append(lin.split(sep='\t'))
    cluster[x][-1] = cluster[x][-1].rstrip()


clust_avg = []
len_start = 0
for y,s in enumerate(cluster): # finds the cluster avg and converts to float
    clust_avg.append(0)
    for x,val in enumerate(s[2:]):
        clust_avg[y] += float(val)
        cluster[y][x+2] = float(val)
    clust_avg[y] = clust_avg[y]/(x+1)
    len_start += 1
    

class Node(object): #leaf object that holds a gene's raw data
    def __init__(self):
        self.gene_id = None #gene identifier
        self.name = None  #gene name
        self.data = None #raw data
        self.avg = None #raw data avg
        self.leaf = True #leaf status
        self.parent = None
        self.val = None #typically avg but written to be other if needed

    def set_data(self,cluster,clust_avg): #sets raw info
        self.gene_id = cluster[0]
        self.name = cluster[1]
        self.data = cluster[2:]
        self.avg = clust_avg
    
class clust(object): #an agglomerative cluster built on prior clusters
    def __init__(self):
        self.leaf = False
        self.parent = None
        self.child = [] #list of all leaf objects associated with this cluster
        self.avg = None
        self.val = None
        
class clustering(object): # main function to cluster data
    def __init__(self):
        self.cluster_count = 0
        self.clusters = []
        
    def insert(self, cluster,clust_avg,link_type): #insert data
        for a, b in zip(cluster, clust_avg):
            current = Node()
            current.set_data(a,b)
            self.clusters.append(current)
            self.cluster_count += 1 #total clusters
            if link_type == 'A': #average type
                current.val = current.avg
            elif link_type == 'S': #single linked type
                current.val = current.avg # min(current.data) #changable
            elif link_type == 'C': #complete link type
                current.val = current.avg # max(current.data) #changable
            
    def update(self, link_type, current): #updates value of each clust object
        if link_type == 'A': #takes average of all child nodes
            total = 0
            for x,obj in enumerate(current.child):
                total += obj.val
            current.val = total/(x+1)
        elif link_type == 'C': # takes the greatest value of all childnodes
            maxnum = -float('inf')
            for obj in current.child:
                if obj.val > maxnum:
                    maxnum = obj.val
            current.val = maxnum
        elif link_type == 'S': # take the smallest value of all childnodes
            minum = float('inf')
            for obj in current.child:
                if obj.val < minum:
                    minum = obj.val
            current.val = minum
            
    def link(self, link_type, k): # agglomerative procces "bottom up" building
        while self.cluster_count > k:
            close = [float('inf'),'object cluster a','object cluster b']
            for a in self.clusters:
                for b in self.clusters:
                    if b != a:
                        difference =abs(a.val-b.val) #finds the difference 
                        if difference < close[0]:    #between clusters values
                            close[0] = difference
                            close[1] = a
                            close[2] = b
            current = clust()
            for d in close[1:]: #adds sub-clusters to master-cluster
                if d.leaf == False:
                    current.child.extend(d.child)
                else:
                    current.child.append(d)
                self.clusters.remove(d)
                d.parent = current
            self.update( link_type, current) #calls update function to update
            self.clusters.append(current)    #the master function
            self.cluster_count -= 1 # shows net master-clusters decline
        current.child = sorted(current.child, key=lambda x: x.val)
        self.clusters = sorted(self.clusters, key = lambda x: x.val)
            
    def output(self): #prints out the master clusters and their sub clusters
        for e in self.clusters:
            print (" ")
            if e.leaf == True:
                print (e.gene_id + e.name + "      " + "%.3f" % e.avg)
                print ('Cluster Avg:  ' +"%.3f" % e.avg)
            else:
                for f in e.child:
                    print (f.gene_id + f.name +"     " + "%.3f" % f.avg)
                print ('Cluster AVg:  '+ "%.3f" % f.avg)
                
            
c = clustering()
c.insert(cluster,clust_avg,link_type)
c.link(link_type, k)
c.output()
        
