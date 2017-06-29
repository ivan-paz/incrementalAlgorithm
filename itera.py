from read_write_clean import *
from commitNewPattern import *
#from rulex_2 import *
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
        temp_rule.append(rule[-2])
        temp_rule.append(rule[-1])
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
            if type(p) == set:
                for e in p:
                    temporal.append(e)
            else:
                temporal.append(p)
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
presets = [ [1,2,'a'], [1,4,'a'] ]
def IntRulex(presets):
    for preset in presets:
        pattern = preset   

#Itera
#pattern = [5,2,'a']
#pattern = [1,2,'a']
#pattern = [1,4,'a']
#pattern = [5,4,'a']
pattern = [2,3,'b']

all_connected_sets = read('all_connected_sets.json')
[intersected_sets, indexes_of_intersected_sets] = intersected_connected_sets(pattern, all_connected_sets)
print('intersected sets', intersected_sets, 'indexes of intersected sets', indexes_of_intersected_sets)
intersected_sets = are_there_rules_to_expand(intersected_sets, pattern)
print('intersected sets are there rules to expand ', intersected_sets)
intersections_plus_pattern = pattern_plus_intersections(pattern, intersected_sets)
for rule in intersections_plus_pattern: rule.append(1) # 1 is the distance factor
print(intersections_plus_pattern)

setForRulexNeu = expand_rules( intersections_plus_pattern)
print( 'set for rulex neu', setForRulexNeu)
Presets = rules_to_presets(setForRulexNeu)
strictRules = rulexM(Presets,[])

#strict rules format to tuple format
def strictRules_Tuple(strictRules):
    strictRules_TupleFormat = []
    for rule in strictRules:
        temporal = []
        for param in rule:
            if type(param) == set:
                if len(param) > 1 :
                    temporal.append(tuple(param))
                else:
                    for i in param:
                        temporal.append(i)
            else:
                temporal.append(param)
        strictRules_TupleFormat.append(temporal)
    return strictRules_TupleFormat

new_set =  strictRules_Tuple(strictRules)
#####new_set = rulex(rulex_format)
print('the strict rules with Tuple format  ', new_set)
new_set = eliminateRisk(new_set)
print('new set without risk', new_set)
#    is it necessary the tuple format or it is possible to use lists     new_set =  [[[1, 5], 2, 'a']]

optimum_partition = optimum_partition(new_set)
if optimum_partition == False:
    optimum_partition = new_set
print('optimum partition : ', optimum_partition)


#--------------------------------------------- read
optimum_partitions = read('optimum_partitions.json')
optimum_partitions_indexes = read('connected_rules_indexes.json')#they share indexes
lonly_rules = read('lonly_rules.json')
lonly_rules_indexes = read('lonly_rules_indexes.json')

non_intersected = remaining_partitions(optimum_partitions,optimum_partitions_indexes,lonly_rules,lonly_rules_indexes,indexes_of_intersected_sets)
#print(non_intersected)
# The new rule base is optimum_partition(new_set) + non_intersected
#      if the new pattern does not intersect any set
# --->  the new rule base is non intersected + new pattern
def newRuleBase(optimum_partition, non_intersected):
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
#def write(file_name,data):
#    with open(file_name,'w') as f:
#        json.dump(data,f)
#------------------------------------   write
#all_connected_sets = extract_connected_sets(new_rule_base)
#write('all_connected_sets.json', all_connected_sets)
#[lonly_rules,lonly_rules_indexes,connected_rules,connected_rules_indexes] = connected_and_lonly_rules( all_connected_sets)
#write('lonly_rules.json',lonly_rules)
#write('lonly_rules_indexes.json',lonly_rules_indexes)
#write('connected_rules_indexes.json',connected_rules_indexes)
