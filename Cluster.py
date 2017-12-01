#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:28:42 2017

@author: alex
"""
import os
import sys
import csv

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
'''
with open(data_file, 'r') as tsv:
        tsv = csv.readlines(tsv, delimter='\t')
        print (tsv)
  '''      
print (lines[0].split())
    
class Node(object):
    def __init__(self):
        self.child = {}
        self.parent = None