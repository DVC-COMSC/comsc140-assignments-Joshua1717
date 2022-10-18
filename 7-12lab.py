import numbers


rnum = 3
cnum = 5

numbers =  [    [10, 11, 12, 13, 14],
                [20, 21, 22, 23, 24],
                [30, 31, 32, 33, 34]]

for i in range(cnum):
    cnum = 0
    for j in range(rnum):
         cnum += numbers[j][i]
        
    print ("The summation of column {0}: {1}".format(i, cnum))