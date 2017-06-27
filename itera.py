from commitNewPattern import *
from rulex_2 import *
from optimum_partition_for_Q import optimum_partition
import json
from splitR_version1 import * #this script is autocontained

# imports for RULEX NEU
import itertools
from rulexMultiparameter import rulexM
#----------------------------------------------------
#     functions to expand rules into presets
def rules_as_sets(rules):
    strict_rules = []
    for rule in rules:
        temporal_rule = rule[0:-2]
        strict_rule = []
        for parameter in temporal_rule:
            if type(parameter) == list or type(parameter) == tuple:
                _set = set(parameter)
                strict_rule.append(_set)
            else:
                _set = set([parameter])
                strict_rule.append(_set)
        strict_rule.append(rule[-2])
        strict_rule.append(rule[-1])
        strict_rules.append(strict_rule)
    return strict_rules

def expandRule(rule):
    rules = []
    sets = rule[0:-2]
    combinations = itertools.product(*sets)
    for i in combinations:
        temp_rule = []
        combination = i
        for j in combination:
            _set = set()
            _set.add(j)
            temp_rule.append(_set)
        rules.append(temp_rule)
    return rules

def expand_rules(rules):
    presets_as_rules = []
    rules = rules_as_sets(rules)
    for rule in rules:
        the_components = expandRule(rule)
        for i in the_components:
            presets_as_rules.append(i)
    return presets_as_rules

def rules_to_presets(rules):
    Presets = []
    for rule in rules:
        temporal = []
        for p in rule:
            for e in p:
                temporal.append(e)
        Presets.append(temporal)
    return Presets
#---------------------------------------------------

#pattern = (5,4,'B')
#pattern = (5,5,'B')
#pattern = (5,6,'B')
#pattern = (4,4,'B')
#pattern = (3,4,'B')
#pattern = (4, 6, 'B')

#Example 1
pattern = (1,2,'a')
pattern = (1,4,'a')
pattern = (5,2,'a')
pattern = (5,4,'a')

all_connected_sets = read('all_connected_sets.json')
[intersected_sets, indexes_of_intersected_sets] = intersected_connected_sets(pattern,all_connected_sets)
print('intersected sets', intersected_sets, 'indexes of intersected sets', indexes_of_intersected_sets)
intersected_sets = are_there_rules_to_expand(intersected_sets, pattern) # *
new_set = pattern_plus_intersections(pattern, intersected_sets)
rulex_format = rulex_format(new_set,1)
print('new set sent to rulex: ', rulex_format)

#set_for_rulex = expand_rules( rulex_format )
#print( 'set for rulex', set_for_rulex)
#Presets = rules_to_presets(set_for_rulex)
#print('presets : ', Presets)
#print('this should be the set sent to the rulex: ', set_for_rulex )
#result = rulexM(Presets,[])



new_set = rulex(rulex_format)
new_set = eliminateRisk(new_set)
optimum_partition = optimum_partition(new_set)
if optimum_partition == False:
    optimum_partition = new_set
#---------------------------------------------
optimum_partitions = read('optimum_partitions.json')
optimum_partitions_indexes = read('connected_rules_indexes.json')#they share indexes
lonly_rules = read('lonly_rules.json')
lonly_rules_indexes = read('lonly_rules_indexes.json')
non_intersected = remaining_partitions(optimum_partitions,optimum_partitions_indexes,lonly_rules,lonly_rules_indexes,indexes_of_intersected_sets)
#print(non_intersected)
# The new rule base is optimum_partition(new_set) + non_intersected
#      if the new pattern does not intersect any set
# --->  the new rule base is non intersected + new pattern
def newRuleBase(optimum_partition,non_intersected):
    new_rule_base = []
    for rule in optimum_partition:
        new_rule_base.append(rule)
    for rule in non_intersected:
        if rule != []:
            new_rule_base.append(rule)
    return new_rule_base
new_rule_base = newRuleBase(optimum_partition,non_intersected)
print('New Rule Base : ', new_rule_base)

#   WRITE THE RESULTS INTO json files
def write(file_name,data):
    with open(file_name,'w') as f:
        json.dump(data,f)
#------------------------------------
#all_connected_sets = extract_connected_sets(new_rule_base)
#write('all_connected_sets.json', all_connected_sets)
#[lonly_rules,lonly_rules_indexes,connected_rules,connected_rules_indexes] = connected_and_lonly_rules( all_connected_sets)
#write('lonly_rules.json',lonly_rules)
#write('lonly_rules_indexes.json',lonly_rules_indexes)
#write('connected_rules_indexes.json',connected_rules_indexes)

