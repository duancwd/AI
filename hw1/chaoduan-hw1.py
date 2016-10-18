#Q5
def function1(sort_list):
    length = len(sort_list)
    if length < 2:
        return sort_list
    for i in range(1, length):
        k = sort_list[i]
        j = i - 1
        while j>=0 and sort_list[j]>k:
            sort_list[j+1] = sort_list[j]
            j =j - 1
            sort_list[j+1] = k
    return sort_list
print(function1([1,4,2,1]))

#Q6
def funtion2(lst, numb):
  
    leng = len(lst)
    if leng <1:
        print 0
        return 0
    elif lst[0] < numb:
        lst.pop(0)
        return funtion2(lst, numb)
    elif lst[-1]> numb:
        lst.pop(-1)
        return funtion2(lst, numb)
    else:
        
        return len(lst)
        
    
    
print(funtion2([1,3,4,5,5,5,6],5))


#Q7
def funtion3(rows):
    r1 = [1]
    r2 = [1, 1]
    tra = [r1,r2]
    r = []
    if rows <= 1:
        r1[0] = str(r1[0])
        print(' '.join(r1))
    elif rows == 2:
        for i in tra:
            for a in range(len(i)):
                i[a] = str(i[a])
            print((' ')*(rows-(a+1))+ (' '.join(i)))
    else:
        for i in range(2, rows):
            tra.append([1]*i)
            for j in range(1, i):
                tra[i][j] = (tra[i-1][j-1]+tra[i-1][j])
            tra[i].append(1)
        for x in range(len(tra)):
            for y in tra[x]:
                #print(tra[x])
                s = str(y)
                r.append(s)
            print((' ')*(rows-(x+1))+ (' ' .join(r)))
            r = []

funtion3(1)
funtion3(2)
funtion3(5)

