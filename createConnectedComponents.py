
ruleSet = [
	[ {1,3},   {3,5},  'A'],
	[ {2,5},   {4},    'A'],
	[ {2},     {2,6},  'A'],
	[ {5.5,9}, {1},    'A'],
        [ {7},  {0.5,0.25},'A'],
        [ {8},     {4.5},  'A']
]

# For numbers
# For strings call another function 
def findMinMax(_set):
    minimum = min(_set) 
    maximum = max(_set)
    return [minimum,maximum]

def intersection(rule1,rule2):
    intersections = 0
    for p in range(len(rule1) - 1):
        [a,b] = findMinMax(rule1[p])
        [x,y] = findMinMax(rule2[p])
        if b >= x and a <= y:
            intersections+=1
    if intersections == len(rule1) - 1:
        return True
    else:
        return False
#print(intersection([{1,3},{3,5},'A'],[{2,5}, {4}, 'A']) )

def createConnectedComponents(ruleSet):
    connectedComponents = [ ]

    while len(ruleSet) > 0:
        intersections = [ ]
        r = ruleSet[0]
        ruleSet.remove(r)
        intersections.append(r)

        connectedComponent = []
        while len(intersections) > 0:
            _r = intersections[0]
            connectedComponent.append(_r)
            intersections.remove(_r)
            # 	search intersections r in ruleSet
            for rule in ruleSet:
                #print('rule',rule)
                if intersection(_r,rule):
                    ruleSet.remove(rule)
                    intersections.append(rule)      
        if connectedComponent:
            connectedComponents.append(connectedComponent)
    [print(i) for i in connectedComponents]
    return connectedComponents
createConnectedComponents(ruleSet)
