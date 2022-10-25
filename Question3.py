import random

N = int(input("Enter number of elements for the list: "))
numbers = [random.randrange(0, 100) for val in range(N)]
    
print("Number list: ")
print(numbers)

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
       
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print("Output:", numbers)