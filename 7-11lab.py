
    
numbers =  [ [10, 11, 12, 14],
                [20, 21, 22, 23, 24],
                [30, 31, 32, 33, 34]]
print ("The list of numbers is: ",numbers)
rnum = len(numbers)
cnum = len(numbers[0])

for i in range(rnum):
    rnum = 0
    for j in range(cnum):
         rnum += numbers[i][j]
        
    print (f'The summation of row {i+1}: {rnum}')
