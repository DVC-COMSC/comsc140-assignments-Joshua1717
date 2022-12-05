def mineven(numbers):
	# evenlst = []
	# for v in numbers:
	# 	if v % 2 == 0:
	# 		evenlst.append(v)
	evenlst = [v for v in numbers if v % 2 == 0]
	minval = min(numbers)
	# minidx = numbers.index(minval)
	# numbers.pop(minidx)
	# for i in range(numbers.count(minval)):
	numbers.remove(minval)
	return minval


# main
num = [2,5,6,0,7]
ret = mineven(num)
print (num)  # [2,5,6,7]

