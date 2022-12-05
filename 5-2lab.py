def getinput(n1, n2): # call by value
	print ('in the function id', id(n1))
	n1 = int(input()) #10
	print ('after getting input', id(n1))
	n2 = int(input()) #20



num1 = 0
num2 = 0

print ('in the main id', id(num1))
getinput(num1, num2)
print (num1, num2) # 0 

