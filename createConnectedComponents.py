#------------------------------------------------------------
#
#    This function takes a rule Set and separates it into
#    its connected Components, i.e. into sets with rules
#    which intersects among them
#------------------------------------------------------------

#Example1
ruleSet = [
	[ {1,3},   {3,5},  'A'],
	[ {2,5},   {4},    'A'],
	[ {2},     {2,6},  'A'],
	[ {5.5,9}, {1},    'A'],
        [ {7},  {0.5,2.5}, 'A'],
        [ {8},     {4.5},  'A']
]

#Example2
#ruleSet = [
#[ {1, 2, 3, 8, 11}, {4, 6},   'A'],
#[ {9,12},            {5},     'A'],
#[    {5},            {4},     'A'],
#[ {2,5},             {7},     'A']
#]

# This function finds the minimum and maximum values
# of a set containing numbers
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
#print(intersection([ {1, 2, 3, 8, 11}, {4, 6},   'A'],[    {5},            {4},     'B']))


def createConnectedComponents(ruleSet):
    connectedComponents = [ ]

    while ruleSet:
        intersections = [ ]
        r = ruleSet[0]
        ruleSet.remove(r)
        intersections.append(r)

        connectedComponent = [ ]
        while intersections:
            _r = intersections[0]
            connectedComponent.append(_r)
            intersections.remove(_r)
            #search intersections r in ruleSet
            print('comparing', _r, 'with the ruleSet',  ruleSet)
            for i in range(len(ruleSet) - 1):
                print('comparing', _r, ruleSet[i])
                if intersection(_r, ruleSet[i]):
                    print('intersection')
                    ruleSet.remove(ruleSet[i])
                    intersections.append(ruleSet[i])
        print('--------------------------------------')
        print('connected component',connectedComponent)
        if connectedComponent:
            connectedComponents.append(connectedComponent)
    [print(i) for i in connectedComponents]
    return connectedComponents



createConnectedComponents(ruleSet)
