str1 = '13579'
# initializing substring
A = 1
# create a result list
result = []
for i in range(0, len(str1), A):
    # convert to int, after the slicing process
    result.append(int(str1[i : i + A]))
  
print("The resultant list : " + str(result))