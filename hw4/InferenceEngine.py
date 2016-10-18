'''
This will be the inference engine component of the rule-based expert system. Using forward-chaining
inferencing it will determine what new facts are true given the set of rules.
'''

def isVar(string):
    ###
    # this function just checks to see if the string in question is a variable or not
    # variables will be indicated with a '?' as the first character of the string
    ###
    return string[0] == '?'

def substituteVariables(substitutions, expression):
    ###
    # this function will take a dictionary of substitutions of the form (?var term) or (?var ?var) and expressions of
    # the form (?var went to the store) and return the result of replacing ?var in the expression with the 
    # associated term in substitutions
    ###
    resultingExpression = []
    hadSubstitution = True
    while hadSubstitution:
        hadSubstitution = False
        for term in expression:
            if type(term) is list:
                # if the term is a nested list we will want to substitute each of the components of the list
                # with their associated terms in the substitution dictionary. We assume that the algorithm is
                # correct and just pass into substituteVariables the nested list and substitutions
                substitutedMultiPartTerm = substituteVariables(substitutions, term)
                resultingExpression.append(substitutedMultiPartTerm)
            elif isVar(term):
                if term in substitutions:
                    # if it is a variable we want to replace it and mark that we made a replacement. If we do not 
                    # mark that we made a replacement then the algorithm won't do double, triple, quadruple, etc. substitutions
                    resultingExpression.append(substitutions[term])
                    hadSubstitution = True
                else:
                    resultingExpression.append(term)
            else:
                resultingExpression.append(term)
        # now we just start the whole process over again until we get through without substituting anything
        expression = resultingExpression
        resultingExpression = []
    return expression

def unification(substitution, pattern1, pattern2):
    ###
    # this algorithm takes two patterns and extracts matching variables to terms when pertinent
    # i.e. unification({}, ['Mike' 'likes' 'tofu'], ['?person', 'likes', 'tofu']) -> { '?person', 'Mike' }
    ###
    if pattern1 == [] or pattern2 == []:
        # if either of these expressions are the empty list then we need to return false if not equal and
        # the substitution if they both are. This will happen when we've gotten to the end of the list
        if pattern1 == pattern2:
            return substitution
        return False
    elif type(pattern1) is list and type(pattern2) is list:
        # this is probably the most important part, we split the first expressions from each list off
        # and match them together, if they produce a substitution then we want to incorporate that
        # substitution in subsequent checks along the list
        newSubstitutions = unification(substitution, pattern1[0], pattern2[0])
        if newSubstitutions != False:
            newSubstitutions.update(substitution)
            return unification(newSubstitutions, pattern1[1 : len(pattern1)], pattern2[1 : len(pattern2)])
        return False
    elif isVar(pattern1):
        # if this is matched it means a variable has been found and we will try to match it to the right
        # to produce a new substitution
        if pattern1 in substitution:
            return unification(substitution, substitution[pattern1], pattern2)
        if type(pattern2) is list:
            if contains(pattern1, pattern2):
                return False
        return { pattern1 : pattern2 }
    elif isVar(pattern2):
        # if this is matched it means a variable has been found and we will try to match it to the left
        # to produce a new substitution
        if pattern2 in substitution:
            return unification(substitution, pattern1, substitution[pattern2])
        if type(pattern1) is list:
            if contains(pattern2, pattern1):
                return False
        return { pattern2 : pattern1 }
    elif pattern1 == pattern2:
        # if this happens it's just two normal strings matching and we don't want to stop anything so we
        # return the substitutions we've been building up
        return substitution
    
    return False

def contains(expression, expressionList):
    ###
    # this function will make sure that nowhere in an arbtrarily nested list
    ###
    for element in expressionList:
        if type(element) is list and not contains(expression, element):
            return True
        if expression == element:
            return True
    return False

def matchAntecedent(antecedents, workingMemory, substitutions):
    ###
    # this function will take a list of antecedents and a working memory of current facts and a dictionary of substitutions
    # and then it will try to match the antecedents to the facts in working memory
    ###
    firstElement = antecedents[0]
    otherElements = antecedents[1 : len(antecedents)]
    return matchIndividualAntecedent(firstElement, otherElements, [], workingMemory, substitutions)

def matchIndividualAntecedent(antecedent, antecedents, states, workingMemory, substitutions):
    ###
    # this function will only attempt to match individual antecedents to the working memory to produce new substitutions
    ###
    if len(workingMemory) == 0:
        return states
    fact = workingMemory[0]
    workingMemory = workingMemory[1 : len(workingMemory)]
    newSubstitutions = unification(substitutions, antecedent, fact)
    if newSubstitutions != False:
        newState = []
        newState.append(antecedents)
        newState.append(newSubstitutions)
        states.append(newState)
        return matchIndividualAntecedent(antecedent, antecedents, states, workingMemory, substitutions)
    else:
        return matchIndividualAntecedent(antecedent, antecedents, states, workingMemory, substitutions)

def executeSubstitution(substitutions, consequents, workingMemory):
    ###
    # this function will perform as many substitutions as possible on each of the consequents and then
    # add the newly produced facts to working memory if they are not already in there
    ###
    newFacts = []
    for consequent in consequents:
        newPattern = substituteVariables(substitutions, consequent)
        if not newPattern in workingMemory:
            newFacts.append(newPattern)
    return newFacts

def matchRule(rule, workingMemory):
    ###
    # this function will determine if it is possible to match a rule using facts present in
    # working memory, and if so will produce the result of matching a rule
    ###
    ruleName = rule.name
    antecedents = rule.antecedentList
    consequents = rule.consequentList
    def match(queue, newWorkingMemory):
        if len(queue) == 0:
            return newWorkingMemory
        # now we want to take the first element off of the queue
        currentAntecedents, currentSubstitutions = queue.pop()
        if currentAntecedents == []:
            # when this is the case we have fully gotten through all of the antecedents
            # and produced a successful set of substitutions. using those substitutions
            # we will now add new facts to the working memory
            newFacts = executeSubstitution(currentSubstitutions, consequents, newWorkingMemory)
            newWorkingMemory.extend(newFacts)
            return match(queue, newWorkingMemory)
        else:
            newState = matchAntecedent(currentAntecedents, workingMemory, currentSubstitutions)
            if newState == []:
                # if we don't produce a new state we want to just go ahead and kill this particular path
                # so we just continue down the queue
                return match(queue, newWorkingMemory)
            # if we produce a new state that means this particular path is still viable and we want to continue
            # expanding it. In traditional DFS fashion we put it onto the list as the item that will be next popped
            # off in the next iteration
            queue.extend(newState)
            return match(queue, newWorkingMemory)
    # we will begin by getting an initial set of items that is the result of all possible instantiations of the first antecedent
    # and the facts in the working memory
    return match(matchAntecedent(antecedents, workingMemory, {}), [])

def checkExisting(item, fullList):
    ###
    # A custom function to check if a particular item (could be a nested list) is contained within
    # a list
    ###
    for element in fullList:
        if item == element:
            return True
    return False

def matchAllRules(rules, workingMemory):
    ###
    # this function generates all of the possible new facts that can be inferred from the given working
    # memory and rules and outputs those new facts
    ###
    newPatterns = []
    for rule in rules:
        newFacts = matchRule(rule, workingMemory)
        for fact in newFacts:
            if not fact in workingMemory and not fact in newPatterns:
                newPatterns.append(fact)
    return newPatterns

def inferNewFacts(rules, workingMemory):
    ###
    # uses forward chaining to find all possible new facts given a set of rules and existing facts
    ###
    newPatterns = matchAllRules(rules, workingMemory)
    while newPatterns:
        workingMemory.extend(newPatterns)
        newPatterns = matchAllRules(rules, workingMemory)
    return workingMemory
