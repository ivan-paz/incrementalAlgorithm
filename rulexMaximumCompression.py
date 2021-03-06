#from rulex_for_class import search_patterns
#from rulex_for_class import search_patterns_delete_redundant
from rulexForClass import search_patterns1
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
#-----------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------
#def rulex(Presets, Rules, d):
#    Extracted_rules = []
#    dictionary_of_classes = dictionary_of_categories(Presets,Rules)
#    print(dictionary_of_classes)
#    for key in dictionary_of_classes:
        #Create set with presets of other classes
        #presets_other_classes = []
        #for key1 in dictionary_of_classes:
         #   if key1 != key:
          #      for p in dictionary_of_classes[key1][0]:
           #         presets_other_classes.append(p)
            #else:
             #   presets_current_class = dictionary_of_classes[key][0]
              #  rules_current_class = dictionary_of_classes[key][1]
#        [presets_other_classes,presets_current_class,rules_current_class] = presets_other_categories(key,dictionary_of_classes)
#        print('key:',key, ';', 'presets other classes : ', presets_other_classes)
#        print('search_patterns function')
#        rules = search_patterns(presets_current_class,rules_current_class,presets_other_classes, d)
#        for r in rules:
#            if r != None:
#                Extracted_rules.append(r)
#    print('Extracted Rules', Extracted_rules)
#    return Extracted_rules

#---    deleting redundant rules after each iteration ----------------
def rulex(Presets, Rules, d, delete_redundant_every_iteration=True):
    final_rules = []
    dictionary_of_classes = dictionary_of_categories(Presets,Rules)
    print(dictionary_of_classes)
    for key in dictionary_of_classes:
        [presets_other_classes,presets_current_class,rules_current_class] = separate_presets_and_rules_other_categories(key,dictionary_of_classes)
        print('key:',key, ';', 'presets other classes : ', presets_other_classes)
        print('search_patterns function')
        #if delete_redundant_every_iteration == False:
        #    rules = search_patterns(presets_current_class,rules_current_class,presets_other_classes, d)
        #else:
        #    rules = search_patterns_delete_redundant(presets_current_class,rules_current_class,presets_other_classes, d)
        rules = search_patterns1(presets_current_class,rules_current_class,presets_other_classes,d,delete_redundant_every_iteration)
        for r in rules:
            if r != None:
                final_rules.append(r)
    print('Final Rules', final_rules)
    return final_rules
