# -*- coding: utf-8 -*-
#from intersection_functions import *
from searchIntersectionsOrRuleCreation import intersection
#----------------------------------------------------------

#R = [
#[ {1, 2, 3, 8, 11}, {4, 6}, 'A'],
#[ {9,12},        {5},     'C'],
#[ {   5},        {4},     'B'],
#[ {2, 5},        {7},     'D']
#]


#---------------------------------------------------------
#  A D J A C E N T           M A T R I X
#  THAT DO NOT CONSIDER INTERSECTIONS OF
#        RULES OF THE SAME CLASS
#---------------------------------------------------------

#def adjacent_matrix(R):
#    print('R', R)
#    graph = {}
#    for i in range( len(R) ):
#        graph[str(i)] =  [ ]    
#        for j in range( len(R) ):
#            if ( i != j ) and intersection ( R[i], R[j] ) == True and sameClass(R[i],R[j]) == False:
#                #print(R[i], R[j])
#                old = graph[str(i)]
#                new = old + [str(j)]
#                graph[str(i)] = new
#    print(graph)
#    return graph

def createAdjacentMatrix(setRules):
    graph = {}
    for i in range(len(setRules)):
        graph[i] = [ ] #æqui
        for j in range(len(setRules)):
            if (i!=j) and intersection(setRules[i],setRules[j])==True and setRules[i][-1]!=setRules[j][-1]:
                old = graph[i] #aqui
                new = old + [j] # before str(j)  BUT now I have the NUMBERS
                graph[i] = new  #aqui
#    print(graph)
    return graph
#print( adjacentMatrix( [ [{6, 9}, {11}, 'A'], [{8}, {10, 14}, 'B'] ] )  )
#print( adjacentMatrix( [ [{6, 9}, {11}, 'A'], [{8}, {10, 14}, 'A'] ] )  )
#matrix = adjacentMatrix(R)
#print(type(matrix['0']) , matrix['0'])         
