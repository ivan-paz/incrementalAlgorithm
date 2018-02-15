#-----------------------------------------------------------------------------------------

#            c    o    m    m    i    t      P    r    e    s    e    t
#

#-----------------------------------------------------------------------------------------
from createConnectedComponents import createConnectedComponents
from searchIntersectionsOrRuleCreation import searchIntersectionsOrRuleCreation
from rulexMaximumCompressionRun import rulexMaxCompress
from expand_rule import expandRule
from rulexForClass import preset_into_rule

#Ejemple3    ---------  this has to be in rules.json
ruleSet = [
 [{2, 4}, {3, 5}, 'i'],
 [{6, 7}, {4}, 'i']
]

#    This has to be in configuration.py
preset = [3,4,'i']
d = 1
deleteEveryIteration = False
heuristic = 1
#--------------------------------------

def commitPreset(preset,ruleSet,d,deleteEveryIteration,heuristic):
    affectedComponents = []
    indexesOfAffectedComponents = []
    setForRulex = []
    index = -1

    connectedComponents = createConnectedComponents(ruleSet)#1
    for connectedComponent in connectedComponents:
        index += 1
        print('connectedComponent : ', connectedComponent)
        r = preset_into_rule(preset)
        intersectionsOrRuleCreation = searchIntersectionsOrRuleCreation(r,connectedComponent)#2
        print(intersectionsOrRuleCreation)
        if intersectionsOrRuleCreation:
            affectedComponents.append(connectedComponent)
            indexesOfAffectedComponents.append(index)
    print('connectedComponents : ', connectedComponents)
    print('the affected components are : ', affectedComponents,'indexes of affected components', indexesOfAffectedComponents)
    for affected in affectedComponents:
        for x in affected:
            expandedRule = expandRule(x)
            [setForRulex.append(y) for y in expandedRule]
    print('set for rulex', setForRulex)
    print('preset : ', preset)
    newSet = rulexMaxCompress([preset],setForRulex,d,False)
    print('newSet de los affected components', newSet)


commitPreset(preset,ruleSet,d,deleteEveryIteration,heuristic)
