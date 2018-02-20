import itertools
import copy
#rule = [{1}, {2,3}, 'A']
#rule = [{1,4},{5,6},'B']
#rule = [[1,4], [5,6], 'B']
#def expand_rule(rule):
#    rule = copy.deepcopy(rule)
#    expanded_rule = []
#    for i in range(len(rule)):
#        if type(rule[i]) != list:
#            rule[i] = [rule[i]]
#    for i in itertools.product(*rule):
#        expanded_rule.append(list(i))
#    return expanded_rule

def expandRule(rule):
    expandedRule = []
    expandedRuleSetFormat = []
    for i in itertools.product(*rule):
        expandedRule.append(i)
    for i in expandedRule:
        print('expandiendo', i)
        tempRule = []
        for j in range(len(rule)-1):
            tempRule.append(set([i[j]]))
        tempRule.append(i[-1])
        expandedRuleSetFormat.append(tempRule)
    return expandedRuleSetFormat
#print(expandRule(rule))

def oneInstanceRules(affectedComponents):
    setForRulex = [ ]
    for affected in affectedComponents:
        for x in affected:
            expandedRule = expandRule(x)
            [setForRulex.append(y) for y in expandedRule]
    return setForRulex

def prepareRulesForRulex(affectedComponents, expandRules):
    setForRulex = [ ]
    if expandRules == True:
        setForRulex = oneInstanceRules(affectedComponents)
        return setForRulex
    else:
        for affected in affectedComponents:
            [setForRulex.append(y) for x in affected for y in x]
            return [setForRulex]
#affectedComponents=  [[[{2, 4}, {3, 5}, 'i']], [[{6, 7}, {4}, 'i']]]
#print(prepareRulesForRulex(affectedComponents,False))
#print('fux34aoqne ')
#print(prepareRulesForRulex(affectedComponents,True))
