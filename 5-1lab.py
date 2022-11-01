def getinput():
	num = int(input())
	return num

def getsum(n1, n2):
	total = n1 + n2
	return total

def printval(n1, n2, tot):
	print (n1, n2, tot)

def main():
	num1 = getinput()
	num2 = getinput()
	result = getsum(num1, num2)
	printval(num1, num2, result)

if __name__ == '__main__':
	main()
