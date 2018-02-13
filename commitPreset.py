#-----------------------------------------------------------------------------------------

#            c    o    m    m    i    t    P    r    e    s    e    t
#

#-----------------------------------------------------------------------------------------
from createConnectedComponents import createConnectedComponents
from searchIntersectionsOrRuleCreation import searchIntersectionsOrRuleCreation


#Ejemple3
ruleSet = [
 [{2, 4}, {3, 5}, 'i'],
 [{6, 7}, {4}, 'i']
]
preset = [1,1,'i']
d = 1
deleteEveryIteration = False
heuristic = 1

def commitPreset(preset,ruleSet,d,deleteEveryIteration,heuristic):
    affectedComponents = []
    index = -1

    connectedComponents = createConnectedComponents(ruleSet)
    for connectedComponent in connectedComponents:
        index += 1
        print('connectedComponent : ', connectedComponent)
        intersectionsOrRuleCreation = searchIntersectionsOrRuleCreation([{3},{3},'b'],connectedComponent)
        print(intersectionsOrRuleCreation)
        if intersectionsOrRuleCreation:
            affectedComponents.append([connectedComponent,index])
    print('the affected components are : ', affectedComponents)

commitPreset(preset,ruleSet,d,deleteEveryIteration,heuristic)
