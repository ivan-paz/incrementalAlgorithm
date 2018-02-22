#----------------------------------------------------------------------------------------

#
#              I  N  T  E  R  S  E  C  T  I  O  N  S
#                             O  R
#              R  U  L  E     C  R  E  A  T  I  O  N
#
#

#----------------------------------------------------------------------------------------

# This function finds the minimum and maximum values
# of a set containing numbers
# For strings call another function
def findMinMax(_set):
    minimum = min(_set)
    maximum = max(_set)
    return [minimum,maximum]

# Returns True if rule1 intersects rule2 False otherwise
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

def ruleCreation(rule1,rule2):
    if rule1[-1] == rule2[-1]:
        for par in range(len(rule1) -1):
            # although there is only one element
            for element in rule1[par]:
                if element in rule2[par]:
                    return True
    return False

def searchIntersectionsOrRuleCreation(r, conectedComponent):
    #Variables min max for parameter of rule r and ri
    intersectionOrRuleCreation = False
    for ri in conectedComponent:
        if intersection(r,ri):
            intersectionOrRuleCreation = True
#            print('intersection')
            return intersectionOrRuleCreation
        if ruleCreation(r,ri):
            intersectionOrRuleCreation = True
#            print('rule Creation')
            return intersectionOrRuleCreation
    return intersectionOrRuleCreation

#  EXAMPLE 1
#connectedComponent = [	
#	[{2, 4}, {3, 5}, 'i']
#        [{6, 7}, {4}, 'i']
#	]
#r = [{1},{1},'i']
#r = [{4},{4},'i']
#r = [{3},{4},'b']
#r = [{3},{3},'b']
#r = [{2},{1},'i']
#r = [{10},{5},'i']
#print(searchIntersectionsOrRuleCreation(r,connectedComponent))











