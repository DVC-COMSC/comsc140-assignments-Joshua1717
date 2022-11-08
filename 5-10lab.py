numbers = [2, 3, 0, 5, 4, 1, 6, 9, 8, 7]


def foldandswap(numbers):
	N = len(numbers)
	j=1
	for i in range(N//2):
		temp = numbers[i]
		numbers[i] = numbers[N - j]
		numbers[N - j] = temp
		j= j+1
		print(numbers)
	print("The list with numbers swapped is", numbers)

print("The orignal list is: ", numbers)

foldandswap(numbers)







