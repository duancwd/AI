from InferenceEngine import *
from Tools import *
'''
Chao Duan

username: chaoduan
'''

class RuleBasedSystem:
    ###
    # a class defining a production system
    ###
    def __init__(self, rules, workingMemory):
        ###
        # initialization function to do necessary conversions for inference engine
        # and instantiate the production system
        ###
        self.rules = rules
        self.workingMemory = workingMemory

        # necessary for inference engine, NO TOUCHING
        self.workingMemoryList = [parseStringToArray(x) for x in self.workingMemory]

    def generateInferences(self):
        ###
        # calls the inference engine to update the working memory
        ###
        self.workingMemoryList = inferNewFacts(self.rules, self.workingMemoryList)
        self.workingMemory = [parseArrayToString(x) for x in self.workingMemoryList]

class Rule:
    ###
    # a class for holding all of the components of a rule (i.e. name, antecedent, consequents)
    ###
    def __init__(self, name, antecedents, consequents):
        ###
        # initialization function that will convert necessary things for inference
        # engine and instantiate instance of rule
        ###
        self.name = name
        self.antecedents = antecedents
        self.consequents = consequents

        # necessary for inference engine, NO TOUCHING
        self.antecedentList = [parseStringToArray(x) for x in self.antecedents]
        self.consequentList = [parseStringToArray(x) for x in self.consequents]


def tagSentence(sentence):
    Rules = []
    WorkingMemory = []
    antecedents = []
    consequents = []
    init_array = parseStringToArray(sentence)
    i = 0
    memory =[]
  #--------------- WorkingMemory---------------------------------- 
    while(i < len(init_array)):
        memory.append(init_array[i])
        #print memory
        i += 1
    memory.append("BEGIN_SENTENCE precedes "+init_array[0])
    i = 1
    while(i < len(init_array)):
         memory.append(init_array[i-1]+" precedes " + init_array[i])
         #print memory
         i += 1
    memory.append(init_array[len(init_array)-1] + " precedes END_SENTENCE")
   # print memory
    
    WorkingMemory =  memory   
    
        
        
   #-------------------rule1-verbs--------------------------      
    
    verbs_list=["love","is", "went", "ran", "bought", "go", "have", "be", "make", "see","knows", "moved"]
    i = 0
    rule1=[]
    while (i < len(verbs_list)):
                name = verbs_list[i]+"-Tag"
                antecedents=[verbs_list[i]]
                consequents=[verbs_list[i] + " = verb"]
                Rules.append(Rule(name, antecedents, consequents))
                i +=1
    #print antecedents
    #print consequents
    #print Rules
    #print "\n"
    
    #--------------------adverbs-----------------------
    adverbs_list=["quickly", "loudly", "easily", "too"]
    i = 0
    rule2=[]
    while (i < len(adverbs_list)):
                name = adverbs_list[i]+"-Tag"
                antecedents=[adverbs_list[i]]
                consequents=[adverbs_list[i] + " = adverb"]
                Rules.append(Rule(name, antecedents, consequents))
                i +=1
    #print antecedents
    #print consequents
    #print Rules
   # print "\n"
    
    #--------------------pronouns-----------------------
    pronouns_list=["he", "she", "it", "i", "they", "we", "them", "that"]
    i = 0
    while (i < len(pronouns_list)):
                name = pronouns_list[i]+"-Tag"
                antecedents=[pronouns_list[i]]
                consequents=[pronouns_list[i] + " = pronoun"]
                Rules.append(Rule(name, antecedents, consequents))
                i +=1
   # print Rules
   # print "\n"
    #print antecedents
    #print consequents  
    ###
    # a function that will take in a sentence and tag it
    ###

 #-------------------nouns----------------------------------------------------
    string = "time food item place store essence "


    nouns_list=parseStringToArray(string)
    i = 0
    while (i < len(nouns_list)):
                name = nouns_list[i]+"-Tag"
                antecedents=[nouns_list[i]]
                consequents=[nouns_list[i] + " = noun"]
                Rules.append(Rule(name, antecedents, consequents))
                i +=1
 #------------------adjectives---------------------------------------------------
    string = "good new first big old last brobdingnagian"


    adjectives_list=parseStringToArray(string)
    i = 0
    while (i < len(adjectives_list)):
                name = adjectives_list[i]+"-Tag"
                antecedents=[adjectives_list[i]]
                consequents=[adjectives_list[i] + " = adjective"]
                Rules.append(Rule(name, antecedents, consequents))
                i +=1
#------------------prepositions---------------------------------------------------
    string = "to of in for with on up"


    prepositions_list=parseStringToArray(string)
    i = 0
    while (i < len(prepositions_list)):
                name = prepositions_list[i]+"-Tag"
                antecedents=[prepositions_list[i]]
                consequents=[prepositions_list[i] + " = preposition"]
                Rules.append(Rule(name, antecedents, consequents))
                i +=1
#------------------determiners---------------------------------------------------
    string = "the a an no that"


    determiners_list=parseStringToArray(string)
    i = 0
    while (i < len(determiners_list)):
                name = determiners_list[i]+"-Tag"
                antecedents=[determiners_list[i]]
                consequents=[determiners_list[i] + " = determiner"]
                Rules.append(Rule(name, antecedents, consequents))
                i +=1
#==============================================================================
    aRules=[]           
#----------1--------pronoun---------------------------------------------------
    name = "BEGIN_SENTENCE-Tag"
    antecedents = ["BEGIN_SENTENCE precedes ?word"]
    consequents = ["?word = pronoun"]
    aRules.append(Rule(name, antecedents, consequents))

#-------------2-----Adverbs---------------------------------------------------
    name = "Adverbs_verb-Tag"
    antecedents = ["?word1 precedes ?word2", "?word2 = verb"]
    consequents = ["?word1 = adverb"]
    aRules.append(Rule(name, antecedents, consequents))
#-----------3-------Adjectives---------------------------------------------------
# Adjectives can go before a noun, before a pronoun, before an adjective, or after a verb
    name = "Adjective_noun-Tag"
    antecedents = ["?word1 precedes ?word2", "?word2 = noun"]
    consequents = ["?word1 = adjective"]
    aRules.append(Rule(name, antecedents, consequents))
    
    name = "Adjective_pronoun-Tag"
    antecedents = ["?word1 precedes ?word2", "?word2 = pronoun"]
    consequents = ["?word1 = adjective"]
    aRules.append(Rule(name, antecedents, consequents))

    name = "Adjective_adjective-Tag"
    antecedents = ["?word1 precedes ?word2", "?word2 = adjective"]
    consequents = ["?word1 = adjective"]
    aRules.append(Rule(name, antecedents, consequents))

    name = "verb_adjective-Tag"
    antecedents = ["?word1 precedes ?word2", "?word1 = verb"]
    consequents = ["?word2 = adjective"]
    aRules.append(Rule(name, antecedents, consequents))
#-------------4----Determiners---------------------------------------------------
  #  4. Determiners will always go before a noun or before a pronoun
    name = "Determiners_noun-Tag"
    antecedents = ["?word1 precedes ?word2", "?word2 = noun"]
    consequents = ["?word1 = determiner"]
    aRules.append(Rule(name, antecedents, consequents))

    name = "Determiners_pronoun-Tag"
    antecedents = ["?word1 precedes ?word2", "?word2 = pronoun"]
    consequents = ["?word1 = determiner"]
    aRules.append(Rule(name, antecedents, consequents))
#---------------5---Nouns---------------------------------------------------
  #  Nouns can go before a verb or
  #  they can go after a preposition that is followed by a determiner 
    name = "Nouns_verb-Tag"
    antecedents = ["?word1 precedes ?word2", "?word2 = verb"]
    consequents = ["?word1 = noun"]
    aRules.append(Rule(name, antecedents, consequents))

    name = "prepos_noun_dete-Tag"
    antecedents = ["?word1 precedes ?word2","?word2 precedes ?word3", "?word3 = preposition","?word1 = determiner"]
    consequents = ["?word2 = noun"]
    aRules.append(Rule(name, antecedents, consequents))

    name = "noun_dete-Tag"
    antecedents = ["?word1 precedes ?word2", "?word1 = determiner"]
    consequents = ["?word2 = noun"]
    aRules.append(Rule(name, antecedents, consequents))
#--------------6----Pronouns---------------------------------------------------
  #  6. Pronouns can go before a verb or they can go after a preposition
  #  that is followed by a determiner 
    name = "Pronouns_verb-Tag"
    antecedents = ["?word1 precedes ?word2", "?word2 = verb"]
    consequents = ["?word1 = pronoun"]
    aRules.append(Rule(name, antecedents, consequents))

    name = " preposition_pronoun_determiner-Tag"
    antecedents = ["?word1 precedes ?word2","?word2 precedes ?word3" ,"?word1 = preposition","?word2 = determiner"]
    consequents = ["?word3 = pronoun"]
    aRules.append(Rule(name, antecedents, consequents))


        
    
#-----------------7-Verbs--------------------------------------------------
  #  7. Verbs will always go after a noun or a pronoun



    name = " noun_verb-Tag"
    antecedents = ["?word1 precedes ?word2", "?word1 = noun"]
    consequents = ["?word2 = verb"]
    aRules.append(Rule(name, antecedents, consequents))

    name = " pronoun_verb-Tag"
    antecedents = ["?word1 precedes ?word2", "?word1 = pronoun"]
    consequents = ["?word2 = verb"]
    aRules.append(Rule(name, antecedents, consequents))

#---------------8--- Prepositions---------------------------------------------------
  #  8. Prepositions can follow a verb



    
    name = "Prepositions_verb-Tag"
    antecedents = ["?word1 precedes ?word2", "?word1 = verb"]
    consequents = ["?word2 = preposition"]
    aRules.append(Rule(name, antecedents, consequents))







    

    '''
   # Rules.extend(rule1)
    for rule in Rules:
        print rule.name
        print rule.antecedents
        print rule.consequents'''
    system = RuleBasedSystem(Rules, WorkingMemory)
    system.generateInferences()
   
    #print system.workingMemory
    copyoldworkingMemory=[]
    copyoldworkingMemory1=[]
    copyoldworkingMemory.extend(system.workingMemory)
    i = 0
    while (i < len(WorkingMemory)):
        copyoldworkingMemory.remove(WorkingMemory[i])
        i +=1
     #print copyoldworkingMemory
    copyoldworkingMemory1.extend(copyoldworkingMemory)
    #print copyoldworkingMemory1
    
#==========================================================================
     
    mysystem = RuleBasedSystem(aRules, system.workingMemory)
    mysystem.generateInferences()
    #print mysystem.workingMemory
    copyworkingMemory=[]
    copyworkingMemory.extend(mysystem.workingMemory)
    i = 0
    while (i < len(WorkingMemory)):
        copyworkingMemory.remove(WorkingMemory[i])
        i +=1
   # print " "
    #print "print system.workingMemory "
   # print mysystem.workingMemory
    #print copyworkingMemory
    i = 0
    '''
    while (i < len(copyworkingMemory)):

      # print len(copyworkingMemory)
      # print parseStringToArray(copyworkingMemory[i])
       #print i
       if (parseStringToArray(copyworkingMemory[i])[0] == "END_SENTENCE" or parseStringToArray(copyworkingMemory[i])[0] == 'BEGIN_SENTENCE') :
             
             copyworkingMemory[i]="0"
       i +=1'''
    checkedlist =[]
    for y in  init_array:
        for x in copyworkingMemory:
             if (parseStringToArray(x)[0] == y ):
                 for z in copyoldworkingMemory:
                     checkedlist.extend(parseStringToArray(z))
                     #print checkedlist
                 if parseStringToArray(x)[0] in checkedlist:
                      1  # print parseStringToArray(x)[0]
                 else:
                     
                         copyoldworkingMemory.append(x)
    mylist = []
    mylist.append(sentence)
    mylist.extend(copyoldworkingMemory)
    print " "
    print "yourSystem.workingMemory: "
    print mylist

    sortlist=[]
    for x in init_array:
        for y in copyoldworkingMemory:
            if x == parseStringToArray(y)[0]:
                sortlist.append(y)

    print " "
    print "taggedSentence: "
    #print sortlist
    
   # print copyoldworkingMemory1
            
            
            
            

         
        
    #copyworkingMemory.delete(0)
    #print copyworkingMemory.count('Mike = pronoun')
   # print copyworkingMemory
    return sortlist





#tagSentence("Mike went")

'''
    

    system = RuleBasedSystem(Rules, WorkingMemory)
    system.generateInferences()

    pass
'''
