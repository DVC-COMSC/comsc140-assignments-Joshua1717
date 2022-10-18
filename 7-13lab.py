import numbers



numbers = [    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
               [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
               [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
               [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

rownum = len(numbers)
colnum = len(numbers[0])

cnt = 0
for i in range(1,rownum-1): # 1 to the 2nd row from last row
	for j in range(1, colnum-1): 
		if ( numbers[i][j] == 1) and (numbers[i-1][j] == 1) and  (numbers[i+1][j] == 1) and  (numbers[i][j-1] == 1) and  (numbers[i][j+1] == 1) :
			cnt += 1

print (cnt)

