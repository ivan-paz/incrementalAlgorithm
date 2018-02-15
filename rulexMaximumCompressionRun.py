from rulexMaximumCompression import rulex
from copy import deepcopy
#from rulex import rulex1
#Example  1 rulex description
#Presets = [
#        [1,2,'a'], 
#        [1,4,'a'], 
#        [5,2,'a'],
#        [5,4,'a']
#        [2,1,'b',1],
#        [2,3,'b',1],
#        [4,1,'b',1],
#        [4,3,'b',1]
#                    ]
#Example 2
#Presets = [[5,4,'B',1],[5,5,'B',1],[5,6,'B',1],[4,4,'B',1],[3,4,'B',1],[4,6,'B',1]]
#---------------------------------------------------------------------------

#--  Example 2 TABLEs  4 and 5

#    test with risk = 2
#    Test 1
#Presets = [[1, 1, 'A'], [2, 2, 'A'], [3, 3, 'A']]
#    Test   1.1
#Presets = [[1, 1, 'A'], [2, 2, 'A'], [3, 3, 'A'], [1, 3, 'B']]
#---------------------------------------------------------------------------

# Test different types of data
#Presets = [ [ 1, 'cat', 1/3, True, 'A', 1 ], [ 1, 'dog', 1/3, True, 'A', 1 ] ]

#----------------------------------------------------------------------
#                        parameter order independent
#CASE 1
#Presets = [ [1,1,'A',1], [2,1,'A',1], [1,2,'A',1] ]
# invert P1 and P2
#Presets = [ [1,1,'A',1], [1,2,'A',1], [2,1,'A',1] ]
#changin the order of the presets
#Presets = [ [1,1,'A',1], [1,2,'A',1], [2,1,'A',1] ]
#-----------------------------------------------------------------------

# test 1 for the incremental algorithm
#Presets = [[1,2,'a'],[1,4,'a'],[5,2,'a'],[5,4,'a']]

#Presets = [[1,1,'a'],[2,1,'a'],[3,1,'a'],[4,1,'a'],[5,1,'a'],[6,1,'a'],[7,1,'a'],[8,1,'a']]
#Presets = [[1,1,'a'],[2,1,'a'],[3,1,'a']]

#Example section of algorithm complexity
#Presets =[[1,1,'a'],[1,2,'a'],[2,1,'a']] 

# set of presets Table 1 whose rules are in table Table 2
#Presets = [	[50, 150, 0.2,  'Part A'],[50, 150, 0.15, 'Part A'],[100,150, 0.15, 'Part A'],[100,150, 0.2,  'Part A']]

# Set of presets Table 3 permutation of Table 1
#Presets = [[50, 150, 0.2,  'Part A'],[100,150,0.2,'Part A'], [50, 150, 0.15, 'Part A'],[100,150, 0.15, 'Part A']]

#Presets = [
#[200, 159, 0.2, 161, 0.4, 160, 0.5, 0.27, 200, 159, 0.01, 161, 0.4, 160, 0.5, 0.01,'Part A'],
#[200, 150, 0.23,150, 0.3, 160, 0.5, 0.3,  200, 150, 0.01, 150, 0.3, 160, 0.5, 0.01,'Part B'],
#[200, 150, 0.26,150, 0.3, 160, 0.4, 0.36, 200, 150, 0.01, 150, 0.3, 160, 0.4, 0.01,'Part B'],
#[200, 150, 0.23,150, 0.3, 161, 0.5, 0.3,  200, 150, 0.001,150, 0.3, 161, 0.5, 0.001,'Part B'],
#[20,  150, 0.25,101, 0.3, 102, 0.5, 0.33, 20,  150, 0.01, 101, 0.3, 102, 0.5, 0.01, 'Part C'],
#[200, 150, 0.28,150, 0.6, 160, 0.4, 0.38, 200, 150, 0.01, 150, 0.6, 160, 0.4, 0.01, 'Part C'],
#[100, 100, 0.25,100, 0.6, 102, 0.4, 0.33, 100, 100, 0.25, 100, 0.6, 102, 0.4, 0.33, 'Part C'],
#[20, 150, 0.25, 101, 0.3, 102, 0.5, 0.33, 20,  150, 0.25, 101, 0.3, 102, 0.5, 0.33, 'Part D'],
#[200,150, 0.28, 150, 0.6, 160, 0.4, 0.38, 200, 150, 0.28, 150, 0.6, 160, 0.4, 0.38, 'Part D'],
#[100,100, 0.25, 100, 0.6, 102, 0.4, 0.33, 100, 100, 0.25, 100, 0.6, 102, 0.4, 0.33, 'Part D'],
#[20, 150, 0.25, 101, 0.3, 102, 0.5, 0.33, 20,  150, 0.25, 101, 0.3, 102, 0.5, 0.33, 'Part E'],
#[200,150, 0.28, 150, 0.6, 160, 0.4, 0.38, 200, 150, 0.28, 150, 0.6, 160, 0.4, 0.38, 'Part E'],
#[100,100, 0.25, 100, 0.6, 102, 0.4, 0.33, 100, 100, 0.25, 100, 0.6, 102, 0.4, 0.33, 'Part E'],
#[100,100, 0.25, 100, 0.6, 102, 0.4, 0.28, 0,   0,   0,    0,   0,   0,   0,   0,   'Part F'],
#[440,880, 0.2,  660, 0.3, 661, 0.5, 0.25, 0,   0,   0,    0,   0,   0,   0,   0,   'Part F'],
#[440,880, 0.23, 660, 0.3, 661, 0.5, 0.22, 0,   0,   0,    0,   0,   0,   0,   0,   'Part G'],
#[440,660, 0.2,  441, 0.3, 661, 0.4, 0.22, 0,   0,   0,    0,   0,   0,   0,   0,   'Part G'],
#[220,440, 0.2,  660, 0.3, 221, 0.5, 0.23, 0,   0,   0,    0,   0,   0,   0,   0,   'Part G'],
#[110,240, 0.2,  660, 0.3, 221, 0.5, 0.23, 0,   0,   0,    0,   0,   0,   0,   0,   'Part G'],
#[110,240, 0.2,  330, 0.3, 221, 0.5, 0.23, 0,   0,   0,    0,   0,   0,   0,   0,   'Part G'],
#[110,240, 0.2,  165, 0.3, 221, 0.5, 0.23, 0,   0,   0,    0,   0,   0,   0,   0,   'Part G'],
#[110,240, 0.2,  82.5,0.3, 110.5,0.5,0.23, 0,   0,   0,    0,   0,   0,   0,   0,   'Part G'],	
#[55, 120, 0.2,  82.5,0.3, 110.5,0.5,0.23, 0,   0,   0,    0,   0,   0,   0,   0,   'Part G']
#]
#
#Rules = []

#             presets  rules  dist delete_redundant after each iteration
#             False is the predefined value
#   linea antes de la funci'on
# rules = rulex(Presets, Rules, 1, False)

#Eliminationg redundant
#print('second version rulex1')
#Presets =[[1,1,'a'],[1,2,'a'],[2,1,'a']]
#R = []
#rules = rulex(Presets, Rules, 1, 1)

#-------------------------------------------------------------------
#                   Rulex Maximum compression
#-------------------------------------------------------------------
def dictionary_of_categories(Presets, Rules):
    dictionary_of_classes = dict()
    for preset in Presets:
        preset_class = preset[-1]
        if preset_class not in dictionary_of_classes:
            dictionary_of_classes[preset_class] = [[],[]]
            dictionary_of_classes[preset_class][0].append(preset)
        else:
            dictionary_of_classes[preset_class][0].append(preset)
    for rule in Rules:
        rule_class = rule[-1]
        if rule_class not in dictionary_of_classes:
            dictionary_of_classes[rule_class] = [[],[]]
            dictionary_of_classes[rule_class][1].append(rule)
        else:
            dictionary_of_classes[rule_class][1].append(rule)
    return dictionary_of_classes

def separate_presets_and_rules_other_categories(key,dictionary_of_classes):
    #Create set with presets of other classes
    presets_other_classes = []
    for key1 in dictionary_of_classes:
        if key1 != key:
            for p in dictionary_of_classes[key1][0]:
                presets_other_classes.append(p)
        else:
            presets_current_class = dictionary_of_classes[key][0]
            rules_current_class = dictionary_of_classes[key][1]
    return [presets_other_classes, presets_current_class, rules_current_class]

def pattern_found(rule1,rule2, d):
    unions = []
    indexes = []
    difference = 0
    for i in range( len(rule1) - 1 ):
        union = rule1[i] | rule2[i]
        unions.append(union)
        if rule1[i] != rule2[i]:
        #if intersection == set() or len(union) > len(intersection):#Note that this condition is rule formation, it isn't "intersection" between min and max.
            difference +=1
            indexes.append(i)
    if difference <= d: #  GENERAL distance Factor
        return [True, unions, indexes]
    else:
        return [False, None, None]

def expandRule(rule):
    rules = []
    sets = rule[0:-1]
    #print('sets', sets)
    combinations = itertools.product(*sets)
    for i in combinations:
        temp_rule = []
        combination = i
        #print(combination,type(combination))
        for j in combination:
            _set = set()
            _set.add(j)
            temp_rule.append(_set)
        #for k in rule[-2:]: temp_rule.append(k)
        rules.append(temp_rule)
    #print(rules)
    return rules
#expandRule([{1,2,3},{2,3},'A'])

def contradictions(rule, presets_other_classes):
    rules_other_classes = []
    for p in presets_other_classes:
        rules_other_classes.append(preset_into_rule(p))
    for r in rules_other_classes:
        r = r[0:-1]
    expand = expandRule(rule)
    for r in expand:
        for R in rules_other_classes:
            equal = 0
            for i in range(len(r)):
                if r[i].issubset(R[i]) == True:
                    equal +=1
            if equal == len(r):
                return True #  There are contradiction

def create_rule(rule1, unions, indexes, presets_other_classes, d):
    rule = deepcopy(rule1) # D E E P C O P Y 28 SEPT 2017
    for index in indexes:
        rule[index] = unions[index]
    if d >=2:#Here the distance factor is used
        contradiction = contradictions(rule,presets_other_classes)
        if contradiction == False:
            return rule
        else:
            return None
    else:
        return rule

#  True if a rule1 is subset of rule2, False otherwhise
def contained( rule1, rule2 ):
    #if rule1[-1] == rule2[-1]:
    equalParameters = 0
    for i in range( len(rule1) - 1 ):
        if rule1[i].issubset(rule2[i]):
            equalParameters +=1
    if equalParameters == len(rule1) - 1:
        return True
    else:
        return False

def deleteRedundant( rules ):
    for i in range(0, len(rules)):
        redundant = False
        rule1 = rules[i]
        #print('rule1',  rule1)
        for j in range(0, len(rules)):
            rule2 = rules[j]
         #   print(rule2)
            if rule1 != None and rule2 != None and i != j and contained(rule1,rule2) == True:
          #      print(rule1,'contained in', rule2)
                redundant = True
        if redundant == True:
            rules[i] = None
    return rules


#def compressRules(Presets,previousRules,d,delete_every_iteration):
#    setOfRules = []
#    dictionary = dictionary_of_categories(Presets,previousRules)
#    for key in dictionary:
#        [presets_other_classes,presets_current_class,rules_current_class] = separate_presets_and_rules_other_categories(key,dictionary)
#        print('rules current class', rules_current_class,len(rules_current_class))
#        for i in range(len(rules_current_class)):
#            rule1 = rules_current_class[i]
#            for rule2 in setOfRules:
#                [pattern,unions,indexes] = pattern_found(rule1,rule2,d)
#                if pattern:
#                    rule = create_rule(rule1,unions,indexes,presets_other_classes,d)
#                    print('created rule',rule)
#                    setOfRules.append(rule)
#                setOfRules=[ii for n,ii in enumerate(setOfRules) if ii not in setOfRules[:n]]
#            setOfRules.append(rule1)
#        setOfRules = deleteRedundant(setOfRules)
#    setOfRules = [x for x in setOfRules if x is not None]  
#    return setOfRules

def compressRules(Presets,previousRules,d,delete_every_iteration):
    setOfRules = []
    dictionary = dictionary_of_categories(Presets,previousRules)
    for key in dictionary:
        [presets_other_classes,presets_current_class,rules_current_class] = separate_presets_and_rules_other_categories(key,dictionary)
        print('rules current class',rules_current_class,len(rules_current_class))
        for i in range(len(rules_current_class)):
            rule1 = rules_current_class[i]
            for rule2 in setOfRules:
                if rule2!=None: # to avoid comparison with None
                    [pattern,unions,indexes] = pattern_found(rule1,rule2,d)
                    if pattern:
                        rule = create_rule(rule1,unions,indexes,presets_other_classes,d)
                        print('created rule',rule)
                        setOfRules.append(rule)
                    setOfRules=[ii for n,ii in enumerate(setOfRules) if ii not in setOfRules[:n]]
            setOfRules.append(rule1)
        setOfRules = deleteRedundant(setOfRules)
    setOfRules = [x for x in setOfRules if x is not None]
    return setOfRules


#Rules = [] #start with empty rules
#Presets = [
#	[2,3,'A'],
#	[2,6,'A'],
#	[4,3,'A'],
#	[4,6,'A'],
#	[3,4,'B']
#	]
#Presets = [ [2,3,'A'],[2,6,'A']]


def rulexMaxCompress(Presets,Rules,d,delete_every_iteration):
    previousRules = []
    rules = rulex(Presets,Rules,d,delete_every_iteration)
    cont = 0
    while rules != previousRules:
        cont +=1
        print('rules != previousRules',cont)
        previousRules = rules
        rules = compressRules(Presets, previousRules, d, delete_every_iteration)
    print('final set of rules: ',rules)
    return rules

#Presets First Example d1 d2 and d3 paper Rio de Janeiro
#Presets = [
#	[82.5,55.25,0.5,0.5,0.23,'intro'],
#	[660,221,0.3,0.5,0.23,'intro'],
#	[330,221,0.3,0.5,0.23,'intro'],
#	[660,110.5,0.3,0.5,0.23,'intro']
#]

#presets for the last example ruo de janeiro
#Presets = [
#[200, 150, 0.23, 150, 0.3, 160, 0.5, 0.3, ' Part B'],
#[200, 150, 0.26, 150, 0.3, 160, 0.4, 0.3, ' Part B'],
#[200, 150, 0.23, 150, 0.3, 161, 0.5, 0.3, ' Part B']
#]
#Presets = [
#[20 , 150, 0.25, 101, 0.3, 102, 0.5, 0.33,' Part E'],
#[200, 150, 0.28, 150, 0.6, 160, 0.4, 0.33,' Part E'],
#[100, 100, 0.25, 100, 0.6, 102, 0.4, 0.33,' Part E']
#]
#
#Presets = [
#[ 20,  150, 0.25,101, 0.3, 102, 0.5, 0.33, 'Part C'],
#[200,  150, 0.28,150, 0.6, 160, 0.4, 0.38, 'Part C'],
#[100,  100, 0.25,100, 0.6, 102, 0.4, 0.33, 'Part C']
#]


#Presets = [
#	[2,5,'i'],
#	[4,5,'i'],
#	[2,3,'i'],
#	[4,3,'i'],
#	[6,4,'i'],
#	[7,4,'i']
#	]
#print('The Presets :  ', Presets)

#rules = rulexMaxCompress(Presets, Rules, 1, False)


#rules = rulex(Presets, Rules,4, True)
#Rules = []
#Presets = [
#	[2,3,'A'],
#	[2,6,'A'],
#	[4,3,'A'],
#	[4,6,'A'],
#	[3,4,'B']
#	]
#Presets = [[2,3,'A']]
#rules = rulex(Presets,Rules,1,False)
#print('...........................................')
#[print(x) for x in rules] 

