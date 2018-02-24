#-----------------------------------------------------------------------------------------

#            c    o    m    m    i    t      P    r    e    s    e    t
#

#-----------------------------------------------------------------------------------------
from createConnectedComponents import createConnectedComponents
from searchIntersectionsOrRuleCreation import searchIntersectionsOrRuleCreation
from rulexMaximumCompressionRun import rulexMaxCompress
from expand_rule import prepareRulesForRulex
from rulexForClass import preset_into_rule
from createIntervalRules import createIntervalRules

#Ejemple3
#    i  n  p  u  t    d  a  t  a -------  this has to be in rules.json or something lile that.
ruleSet = [
 [{2, 4}, {3, 5}, 'i'],
 [{6, 7}, {4}, 'i']
]
#    This has to be in configuration.py
preset = [3,4,'i']
d = 1
heuristic = 1
splitRules = True
#--------------------------------------

def commitPreset(preset,ruleSet,d,heuristic,splitRules):
    affectedComponents = [ ]
    indexesOfAffectedComponents = [ ]
    #setForRulex = [ ]
    index = -1

    connectedComponents = createConnectedComponents(ruleSet)#1
    rule = preset_into_rule(preset) #1.1 

    for connectedComponent in connectedComponents:
        index += 1
        intersectionsOrRuleCreation = searchIntersectionsOrRuleCreation(rule,connectedComponent)#2
#        print(intersectionsOrRuleCreation)
        if intersectionsOrRuleCreation:
            affectedComponents.append(connectedComponent)
            indexesOfAffectedComponents.append(index)

    print('connectedComponents : ', connectedComponents)
    print('preset', preset)
    print('the affected components are : ', affectedComponents)
    print('indexes of affected components', indexesOfAffectedComponents)
    #Prepare set for rulex
    #for affected in affectedComponents:
    #    for x in affected:
    #        expandedRule = expandRule(x)
    #        [setForRulex.append(y) for y in expandedRule]
    setForRulex = prepareRulesForRulex(affectedComponents, splitRules)
    print('set for rulex', setForRulex)
    newSet = rulexMaxCompress([preset],setForRulex,d,False)#3
    print('newSet de los affected components',newSet)
    intervalRules = createIntervalRules(newSet,heuristic)




commitPreset(preset,ruleSet,d,heuristic,splitRules)
