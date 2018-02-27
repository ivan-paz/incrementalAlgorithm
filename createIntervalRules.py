#_*_ coding: utf-8 _*_
from adjacent_matrix import createAdjacentMatrix
from generate_edges import * 
from break_edges import createSolutionSpace
#newSet = [[{2, 4}, {3, 5}, 'i'], [{3, 6, 7}, {4}, 'i']]

rulexOutput = [
[ {1, 2, 3, 8, 11}, {4, 6}, 'A'],
[ {9,12},           {5},    'C'],
[ {   5},           {4},    'B'],
[ {2, 5},           {7},    'D']
]

def identifyContradictions(rulexOutput):
    adjacentMatrix = createAdjacentMatrix(rulexOutput)
    edges = generate_edges(adjacentMatrix)
    simplifiedEdges = simplify_edges(edges)
    #print('simplifiedEdges: ', simplifiedEdges)
    return simplifiedEdges

#def separateRulesToCreatePartitions(simplifiedEdges,rulexOutput):
#    rulesToCreatePartitions = []
    

def createIntervalRules(rulexOutput,heuristic):
    #build the adjacent matrix
    #adjacentMatrix = createAdjacentMatrix(rulexOutput)
    #print('adjacent matrix   ' , adjacentMatrix)
    #edges = generate_edges(adjacentMatrix)
    #print('edges: ', edges)
    #simplifiedEdges = simplify_edges(edges)
    #print('simplified edges : ', simplifiedEdges)
    contradictions = identifyContradictions(rulexOutput)
    print(contradictions)
    solutionSpace = createSolutionSpace(contradictions,rulexOutput)

createIntervalRules(rulexOutput,1)
