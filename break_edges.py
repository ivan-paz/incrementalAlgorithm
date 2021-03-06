# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 16:25:56 2017

@author: ivan
"""
import copy
from adjacent_matrix import createAdjacentMatrix
#from create_partitions_from_connected_component import *
#from function_to_create_subsets import *
from create_rules import partitions
#from functions_to_calculate_the_volume_of_a_partition import *
#from intersection_of_rules import *
from generate_edges import *


def exclude_current_edge(edge,edges):
    temp = copy.deepcopy(edges)
    temp.remove(edge)
    return temp


def identifyContradictions(rulexOutput):
    adjacentMatrix = createAdjacentMatrix(rulexOutput)
    edges = generate_edges(adjacentMatrix)
    simplifiedEdges = simplify_edges(edges)
    #print('simplifiedEdges: ', simplifiedEdges)
    return simplifiedEdges

rulexOutput  = [
[ {1, 2, 3, 8, 11}, {4, 6}, 'A'],
[ {9,12},           {5},    'C'],
[ {   5},           {4},    'B'],
[ {2, 5},           {7},    'D']
]
#contradictions = [[1, 0], [2, 0]]
def createPartitionsTree(rulexOutput):
    intersections = True
    while intersections == True:
        intersections = False
        contradictions = identifyContradictions(rulexOutput)
        for i in range(len(contradictions)): contradictions[i] = sorted(contradictions[i])
        for edge in contradictions:
           branch = []
           pieces  = partitions(rulexOutput[edge[0]],rulexOutput[edge[1]])
           [branch.append(p) for p in pieces]
    print(branch)
createPartitionsTree(rulexOutput)




#   antes cut    
def createSolutionSpace(contradictions,rulexOutput):
    print('Connected_set to break tree-like :', contradictions)
    #matrix = createAdjacentMatrix(Q)
    #print('Matrix', matrix)
    #edges = generate_edges(matrix)
    #edges = simplify_edges(edges)
    #print('Edges', edges)
    for i in range(len(contradictions)): contradictions[i] = sorted(contradictions[i])
        #contradictions = sorted(contradictions, key = operator.itemgetter(1))
    solutionSpace = [ ]
    for edge in contradictions:
        #print('breaking union', edge)
        temp_partitions = [ ]
#        print( rulexOutput[ edge[0] ], rulexOutput[ edge[1] ] )
#        print(partitions(rulexOutput[edge[0]],rulexOutput[edge[1]]))
        r1 = rulexOutput[ edge[0] ]
        r2 = rulexOutput[ edge[1] ]
        print(partitions(r1,r2))
        #temp_partitions = temp_partitions + partitions( rulexOutput[edge[0]], rulexOutput[edge[1]] )
        #print(temp_partitions)
        #clone_rulexOutput = copy.deepcopy(rulexOutput)
        #clone_rulexOutput.remove(rulexOutput[edge[0]])
        #clone_rulexOutput.remove(rulexOutput[edge[1]])
        #print('clone_rulexOutput', clone_rulexOutput)
        
        #for p in temp_partitions:
        #    for x in clone_rulexOutput:
        #        p.append(x)
            #print('p: ',p)
        #solutionSpace.append(temp_partitions) #########  Eliminate levels Rompe la herarquia
    return solutionSpace
#print( createSolutionSpace(contradictions,rulexOutput) )
#print( partitions( [{1,3},{1},'A'],[{2},{1},'B']) )


"""
Q = [
        ( (1,2,3,8,11), (4,6), 'A'),
        (       (9,12),     5, 'C'),
        (            5,     4,'B')    
    ]
"""
#----------------------------------------------------
#   a = np.array([(5, 4, 'B'), ((1, 2, 3, 8, 11), (4, 6), 'A'), ((9, 12), 5, 'C')], dtype = object)
import numpy as np
def shape(a):
    a = np.array(a,   dtype = object) # dtype = object
    return(a.shape)

#--------------------------------------------------
#          ORIGINAL WORKING FUNCTION
#---------------------------------------------------
def tee(q):
    tree_leafs = []
    i = 0
    d = {}
    leafs = True
    while leafs == True:
        j = 0
        leafs = False
        if len(shape(q)) == 1:
            #print('Case1 ' , q)
            temp1 = []
            
            i = i + 1
            
            for element in q:    
                temp = cut(element)
                
                
                for k in temp:
                    j = j + 1
                    d[str(i)+ ',' +str(j)] = k
                    
                
                temp1 = temp1 + temp
                if temp != []:
                    leafs = True
                else:
                    new_leaf = element
                    #print('LEAF: ', element)
                    tree_leafs.append(new_leaf)
                    
            temp = temp1
            q = temp ###
        else:
            #print('Case2', q)
            temp = cut(q)
            leafs = True
            q = temp
            
            i = i + 1
            for k in q:
                j = j + 1
                d[str(i)+ ',' +str(j)] = k
    #print('leafs' , tree_leafs)
    return [d, tree_leafs]

#Q = [((6, 9), 11, 'A'), (8, (10, 14), 'A')]
#Q = [(12, (10, 13), 'B'), ((11, 13), (11, 13), 'D')]
#d  = tee(Q)
#[d, leafs] = tee(Q)
#[d,leafs] = tee(Q)
#print(d)
#print(leafs)
#for leaf in leafs:
#    print(leaf)
#----------------------------------------------------------------------------
