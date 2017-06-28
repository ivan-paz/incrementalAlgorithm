
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#       " INCREMENTAL ALGORITHM "
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#---------------------------------------------------------------
#   1. Read a new pattern and a existing Rule Base
#   2. modify the Rule base according the new pattern.
#---------------------------------------------------------------
#   The rule base is expressed in terms of connected sets and lonly_rules
#---------------------------------------------------------------
from intersection_functions import intersection_or_possible_rule_formation
from intersection_functions import is_contained
from expand_rule import expand_rule
#from rulex_2 import *
from optimum_partition_for_Q import optimum_partition
#---------------------------------------------------
# Read file all_connected_sets
# all_connected_sets = read('all_connected_sets.json')
# print('Original connected sets:')
# for i in all_connected_sets: print(i)

#--------------------------------------------------------
#  When a new pattern comes, as we already have    ------
#  the optimum partition for each connected set    ------
#  we find wich of the original connected_sets     ------
#  are intersected by the new instance             ------
#--------------------------------------------------------

def intersected_connected_sets( new_pattern, all_connected_sets ):
    indexes_of_intersected_sets = [ ]
    intersected_sets = []
    index_counter = -1
    for connected_set in all_connected_sets:
        index_counter += 1
        include_set = False
        for rule in connected_set:
            #intersects = intersection(new_pattern, rule) # INTERSECTIONS OF ALREADY RULEXED INSTANCES
            # Function that considers intersection or possible rule formation with Rulex
            intersects = intersection_or_possible_rule_formation( new_pattern, rule, 1 )
            print('The intersection of', new_pattern, 'with',rule, 'is', intersects)
            if intersects == True:
                include_set = True
        if include_set == True:
            indexes_of_intersected_sets.append( index_counter )
            intersected_sets.append( connected_set )
    return [ intersected_sets,  indexes_of_intersected_sets ]

#pattern = ( 2, 5, 'A')
#pattern = ( 5, 5, 'A')
#pattern = ( 5, 5, 'B' ) # Pattern Test 1 ***
#pattern = (5, 5, 'D')   # Pattern for Test 3
#pattern = (5, 11, 'A')  # Pattern for Test 2
#pattern = (1, 1, 'D')   # Pattern with no intersections
#pattern = (4,7,'D')
#[ intersected_sets,  indexes_of_intersected_sets ] = intersected_connected_sets( pattern, all_connected_sets)
#print('Intersected sets', intersected_sets, 'indexes', indexes_of_intersected_sets)


# Check in the intersected sets, if the pattern is coniained into a rule
# expand that rule to apply the rulex
def are_there_rules_to_expand(intersected_sets, pattern):
    index = -1
    for intersected_set in intersected_sets:
        index += 1
        expansion = []
        for rule in intersected_set:
            contained = False
            if rule[-1] == pattern[-1]:
                for i in range(len(pattern) - 1):
                    if is_contained(pattern[i],rule[i]) == True:
                        contained = True
                        print('is contained', rule)
            if contained == True:
                expanded_rule = expand_rule(rule)
                #remove and change for its expansion
                intersected_set.remove(rule)
                for ele in expanded_rule:
                        expansion.append(ele)
        for element in expansion:
            intersected_set.append(element)
        #if the set has changed incorpore the new set (by now I'm changing alll)
        intersected_sets[index] = intersected_set
    return intersected_sets

# intersected_sets = are_there_rules_to_expand(intersected_sets, pattern)

#  print('Intersected_sets with expanded rules', intersected_sets)

#Create new set with the new pattern + intersections
def pattern_plus_intersections(pattern, intersected_sets):
        new_set = []
        for intersected_set in intersected_sets:
            for rule in intersected_set:
                new_set.append(rule)
        new_set.append(pattern)
        return new_set

# print('This is the set for Rulex : ' )
#  new_set = pattern_plus_intersections(pattern, intersected_sets)
#  print(new_set)


#rulex_format =  rulex_format(new_set,1)
#new_set = rulex(rulex_format)
#print('Rulex of new set:', new_set )
#---------------------------------
# Eliminate RISK to calculate the
# optimum partition for new_set
#---------------------------------
def eliminateRisk(new_set):
    set_without_risk_parameter = []
    for rule in new_set:
        rule = list(rule)
        del rule[-1]
        set_without_risk_parameter.append(rule)
    return set_without_risk_parameter
# new_set = eliminateRisk(new_set)
# print('new_set', new_set )
# print('Optimum partition for the new set: ', optimum_partition(new_set))
#------------------------------------------------------------------------------
#           Exclude from optimim_partitions or lonly rules                   --
#           the indexes_of_intersected_sets, keep the rest of the partitions --
#------------------------------------------------------------------------------
#optimum_partitions = read('optimum_partitions.json')
#optimum_partitions_indexes = read('connected_rules_indexes.json')  #  They share indexes
#lonly_rules = read('lonly_rules.json')
#lonly_rules_indexes = read('lonly_rules_indexes.json')

#print('------------------')
#print('indexes of intersected sets :  ' , indexes_of_intersected_sets)
#print('optimum_partitions_indexes:',optimum_partitions_indexes)
#print('lonly_rules_indexes:', lonly_rules_indexes)


#  Compare the indexes of optimum_partitions (partitions for the connected rules) and lonly rules
#  with the indexes of the intersected sets
#  if they match, eliminate the entrance either in the optimim_partitions of in the lonly_rules
#  return as final set {lonly_rules, optimum_partitions}\{elements_at_indexes_of_intersected_rules}
def remaining_partitions(optimum_partitions, optimum_partitions_indexes, lonly_rules, lonly_rules_indexes, indexes_of_intersected_sets):
    kept_partitions = []
    kept_lonly = []

    for i in range( len(optimum_partitions_indexes) ):
        index = optimum_partitions_indexes[i]
        flag = index in indexes_of_intersected_sets
        if flag == False:
            kept_partitions = kept_partitions + optimum_partitions[i]

    for i in range( len(lonly_rules_indexes) ):
        index = lonly_rules_indexes[i]
        flag = index in indexes_of_intersected_sets
        if flag == False:
            kept_lonly.append(lonly_rules[i])
    return [ kept_partitions, kept_lonly ]

#print( 'Optimum partitions of the not_intersected sets : ')
#not_intersected = remaining_partitions(optimum_partitions, optimum_partitions_indexes, lonly_rules, lonly_rules_indexes, indexes_of_intersected_sets)
#print(not_intersected)

#if len(intersected_sets) == 0:
#   print('there are no intersections')
