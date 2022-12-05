numbers = [3, 2, 0, 5, 4]
print("Oringal list:", numbers)

def split(numbers):
	#find middle elements
	tmp = numbers
	median = len(tmp) // 2

	for i in range(numbers[median-1]):
		numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
		#print(numbers)
	return numbers

print("Swapped list:", split(numbers))