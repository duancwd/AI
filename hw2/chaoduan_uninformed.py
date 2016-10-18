import time
from pydoc import deque
from heapq import heappush, heappop
goalState = []


def uninformedSearch(queue, limit, numRuns):


    if queue == []:
     
        return
    elif testProcedure(queue[0]):

        outputProcedure(numRuns, queue[0])
    elif limit == 0:
     
        return
    else:
        limit -= 1
        numRuns += 1
   
        uninformedSearch(expandProcedure(queue[0], queue[1:len(queue)]), limit, numRuns)





def expandProcedure(queue, state):
    visited = []
    path = deque([queue])
    n = state
       
        
    queue = path.popleft()
    if n not in visited:
     
         visited.append(n)
         
    successors = []
    blankPos = 0
    adjacent = []
 
    for i in range(len(state)):
        if state[i] == 0:
            blankPos = i
  
 
    if (blankPos % 3 != 2):
        nextPos = blankPos + 1
        adjacent.append(nextPos)


    if (blankPos % 3 != 0):
        prev = blankPos - 1
        adjacent.append(prev)


    if (blankPos > 2):
        up = blankPos - 3
        adjacent.append(up)


    if (blankPos < 6):
        down = blankPos + 3
        adjacent.append(down)

    succ = state
    for pos in adjacent:
        succ = list(state)
    

        if pos >= 0 and pos <= 8:
            temp = succ[blankPos]
            succ[blankPos] = succ[pos]
            succ[pos] = temp
            successors.append(succ)
    return successors
    successors = expandProcedure(n)     
    for succ in successors:
        new_path = temp_path + [succ]
        path.append(new_path)
      
    q.extend(successors)

                  
    return queue  




   


        
def testProcedure(queue):
    if (queue == goalState):
        return True
    else:
        return False
     
def outputProcedure(numRuns, path):

    idx = 0    
    for i in path:
        
       
        idx += 1
        print (" " if i[0] == 0 else i[0]) , " " , (" " if i[1] == 0 else i[1]) , " " , (" " if i[2] == 0 else i[2]) 
        print (" " if i[3] == 0 else i[3]) , " " , (" " if i[4] == 0 else i[4]) , " " , (" " if i[5] == 0 else i[5]) 
        print (" " if i[6] == 0 else i[6]) , " " , (" " if i[7] == 0 else i[7]) , " " , (" " if i[8] == 0 else i[8]), "\n"
        
        

    

def makeState(nw, n, ne, w, c, e, sw, s, se):
    statelist = [nw, n, ne, w, c, e, sw, s, se]
    for i in range(len(statelist)):

        if statelist[i] == "blank":
            statelist[i] = 0
    return statelist
    



def testUninformedSearch(initialState, goalState, limit):

    t1 = time.time()
    uninformedSearch ([initialState], limit, 0)
    t2 = time.time()
    print (t2-t1)

   

goalState = makeState(1, 2, 3, 4, 5, 6, 7, 8, "blank")

# First group of test cases - should have solutions with depth <= 5
initialState1 = makeState(2, "blank", 3, 1, 5, 6, 4, 7, 8)
initialState2 = makeState(1, 2, 3, "blank", 4, 6, 7, 5, 8)


# Second group of test cases - should have solutions with depth <= 10
initialState3 = makeState(2, 8, 3, 1, "blank", 5, 4, 7, 6)
initialState4 = makeState(1, 2, 3, 4, 5, 6, "blank", 7, 8)


# Third group of test cases - should have solutions with depth <= 20
initialState5 = makeState("blank", 5, 3, 2, 1, 6, 4, 7, 8)
initialState6 = makeState(5, 1, 3, 2, "blank", 6, 4, 7, 8)


# Fourth group of test cases - should have solutions with depth <= 50
initialState7 = makeState(2, 6, 5, 4, "blank", 3, 7, 1, 8)
initialState8 = makeState(3, 6, "blank", 5, 7, 8, 2, 1, 4)

print "Test 1 Uninformed ___________________"
testUninformedSearch(initialState1, goalState, 10000000)
print "Test 2 Uninformed ___________________"
testUninformedSearch(initialState2, goalState, 10000000)
print "Test 3 Uninformed ___________________"
testUninformedSearch(initialState3, goalState, 10000000)
print "Test 4 Uninformed ___________________"
testUninformedSearch(initialState4, goalState, 10000000)
print "Test 5 Uninformed ___________________"
testUninformedSearch(initialState5, goalState, 10000000)
print "Test 6 Uninformed ___________________"
testUninformedSearch(initialState6, goalState, 10000000)
print "Test 7 Uninformed ___________________"
testUninformedSearch(initialState7, goalState, 10000000)
print "Test 8 Uninformed ___________________"
testUninformedSearch(initialState8, goalState, 10000000) 
    
