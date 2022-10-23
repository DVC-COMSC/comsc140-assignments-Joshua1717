numbers =  [    [99, 11, 66, 86, 55],
                [44, 21, 65, 88, 24],
                [33, 77, 32, 33, 34]] 

rows = 3
cols = 5
sum = 0

print("Sum of rows:", end=" ")
for r in range(rows):
    for c in range(cols):
        sum += numbers[r] [c]
    print(sum, end=" ")
    sum = 0
print(" ")

print("Sum of columns:", end=" ")
for c in range(cols):
    for r in range(rows):
        sum += numbers[r][c]
    print(sum, end=" ")
    sum = 0
print(" ")

rowers = 0
rowidx = 0
maxRow = 0
for i in range(rows):
    sum = 0
    for j in range(cols):
        sum += numbers[i][j]
    if (sum > maxRow):
        maxRow = sum
        rowidx = i
        rowers = rowidx
print("The row that has greatest sum:", rowers)



listrows = len(numbers)
listcols = len(numbers[0])
listmax = numbers[0][0]

for n in range(listrows):
    for m in range(listcols):
      if(numbers[n][m] > listmax):
        listmax = numbers[n][m]
print('The greatest number:', listmax)