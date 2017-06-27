from copy import deepcopy
import itertools
#-------------------------------------------------------------
def preset_into_rule(preset):
    strict_rule = []
    for i in range( len(preset) - 2 ):
        strict_rule.append( set( [ preset[i] ] ) ) #Python 3
    strict_rule.append(preset[-2])                 #Class label
    strict_rule.append(preset[-1])                 #Risk factor
    return strict_rule
#print(preset_to_rule([1,2,3,'A',1]))
#-------------------------------------------------------------
#   Before  is_compressible
def pattern_found(rule1,rule2):
    unions = []
    indexes = []
#   if rule1[-2] == rule2[-2]:
    difference = 0
    for i in range( len(rule1) - 2 ):
        #intersection =  rule1[i] & rule2[i]
        union = rule1[i] | rule2[i]
        unions.append(union)
        if rule1[i] != rule2[i]:
        #if intersection == set() or len(union) > len(intersection):#Note that this condition is rule formation, it isn't "intersection" between min and max.
            difference +=1
            indexes.append(i)
    if difference <= rule1[-1]: #  GENERAL distance Factor
        return [True, unions, indexes]
    else:
        return [False, None, None]
 #   else:
  #      return [False, None, None]
#print( pattern_found( [{1}, {2}, 'A', 1], [{2}, {2}, 'A', 1])  )
#print( pattern_found([{2}, {2}, 'A', 1],[{1}, {3}, 'A', 1])  )
#print( pattern_found([{1}, {2}, 'A', 1],[{1}, {2,3},'A',1]))

def expandRule(rule):
    rules = []
    sets = rule[0:-2]
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
#expandRule([{1,2,3},{2,3},'A',1])

def contradictions(rule,presets_other_classes):
    rules_other_classes = []
    for p in presets_other_classes:
        rules_other_classes.append(preset_into_rule(p))
    for r in rules_other_classes:
        r = r[0:-2]
    expand = expandRule(rule)
    for r in expand:
        for R in rules_other_classes:
            equal = 0
            for i in range(len(r)):
                if r[i].issubset(R[i]) == True:
                    equal +=1
            if equal == len(r):
                return True #  There are contradiction
    return False # No contradiction
#print(contradictions([{1,2},{3},'A',1],[[{1},{4},'B',1],[{4},{8},'C',1],[{1},{3},'B',1]]))

def create_rule(rule1, rule2, presets_other_classes):
    [pattern, unions, indexes] = pattern_found(rule1,rule2)
    if pattern == True:
        rule = rule1
        for index in indexes:
            rule[index] = unions[index]
        if rule1[-1]>=2:
            contradiction = contradictions(rule,presets_other_classes)
            if contradiction == False:
                return rule
        else:
            return rule
    else:
        return None
#print( create_rule([{1}, {2}, 'A', 1],[{2}, {2}, 'A', 1])  )
#print( create_rule([{2}, {2}, 'A', 1],[{1}, {3}, 'A', 1]) )
#print( create_rule([{1}, {2}, 'A', 1],[{1}, {2,3},'A',1]))

#  True if a rule1 is subset of rule2, False otherwhise
def contained( rule1, rule2 ):
    if rule1[-2] == rule2[-2]:
        equalParameters = 0
        for i in range( len(rule1) - 2 ):
            if rule1[i].issubset(rule2[i]):
                equalParameters +=1
        if equalParameters == len(rule1) - 2:
            return True
        else:
            return False
    else:
        return False
# TESTS
#print(contained( [{1},{1},'A',1],[{1},{1,2,3},'A',1]) )
#print(  contained( [{2},{7},'D',1],[{2,5},{7},'D',1]   )   )

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
# -----    test    -----
#rules = [ [{5}, {5}, 'D', 1], [{2}, {7}, 'D', 1], [{5}, {5, 7}, 'D', 1], [{2, 5}, {7}, 'D', 1] ]


#RULEX
def rulex_for_class(Presets, Rules,  presets_other_classes):
    if len(Rules) == 0:
        #move the first preset to rules tramsform it into a rule --->  {}, {}, 'A', 1
        Rules.append( preset_into_rule(Presets[0]) )
        #del Presets[0]
    preset_counter = -1
    for preset in Presets:
        preset_copy = deepcopy(preset)
        preset_counter +=1
        preset = preset_into_rule(preset)
        for i in range(len(Rules)):
            [pattern,b,c] = pattern_found(preset,Rules[i])#is compress OR possible_rule_formation
            if pattern == True:
                print('create : ', create_rule( preset, Rules[i],presets_other_classes) )
                Rules.append(create_rule( preset, Rules[i],presets_other_classes))#APPEND RULE
                Rules.append( preset_into_rule(preset_copy))#APPEND PRESET
        Rules.append(preset_into_rule(preset_copy))#APPEND PRESET
        #Presets[preset_counter] = None
    deleteRedundant(Rules)
    return Rules
def splitClasses(Presets, Rules):
    dictionary_of_classes = dict()
    for preset in Presets:
        preset_class = preset[-2]
        if preset_class not in dictionary_of_classes:
            dictionary_of_classes[preset_class] = [[],[]]
            dictionary_of_classes[preset_class][0].append(preset)
        else:
            dictionary_of_classes[preset_class][0].append(preset)
    for rule in Rules:
        rule_class = rule[-2]
        if rule_class not in doctionary_of_classes:
            dictionary_of_classes[rule_class] = [[],[]]
            dictionary_of_classes[rule_class][1].append(rule)
        else:
            dictionary_of_classes[rule_class][1].append(rule)
    return dictionary_of_classes
#-----------------------------------------------------------------

def rulexM(Presets,Rules):
    Extracted_rules = []
    dictionary_of_classes = splitClasses(Presets,Rules)
    for key in dictionary_of_classes:
        presets_other_classes = []
        for key1 in dictionary_of_classes:
            if key1 != key:
                for p in dictionary_of_classes[key1][0]:
                    presets_other_classes.append(p)
            else:
                presets_same_class = dictionary_of_classes[key][0]
                rules_same_class = dictionary_of_classes[key][1]
        print('presets same class as',key, presets_same_class)
        print('key',key, presets_other_classes)
        rules = rulex_for_class(presets_same_class,rules_same_class,presets_other_classes)
        for r in rules:
            if r != None:
                Extracted_rules.append(r)
    print('Extracted Rules', Extracted_rules)
    return Extracted_rules
