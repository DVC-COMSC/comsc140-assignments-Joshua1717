def findmin(numbers):
	minidx = numbers.index(min(numbers))
	numbers[0], numbers[minidx] = numbers[minidx], numbers[0]
	# return numbers


numbers = [5, 4, 3, 2, 1]

others = numbers
for i in range(len(numbers)-1):
	findmin(others)
	firstval, *others = others
	numbers[i] = firstval


print (numbers)