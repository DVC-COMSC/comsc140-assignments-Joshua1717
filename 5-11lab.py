
num1 = [0, 2, 3]
num2 = [1, 4, 5, 6, 9]
  

print ("The first list is : " + str(num1))
print ("The second list 2 is : " + str(num2))
  
# using naive method 
# to combine two sorted lists
size_1 = len(num1)
size_2 = len(num2)
  
res = []
i, j = 0, 0
  
while i < size_1 and j < size_2:
    if num1[i] < num2[j]:
      res.append(num1[i])
      i += 1
  
    else:
      res.append(num2[j])
      j += 1
  
res = res + num1[i:] + num2[j:]
  
# printing result
print ("The merge list is : " + str(res))