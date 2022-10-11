import itertools

num1 = list(map(int, input("Enter some numbers for the first list:").split()))
num2 = list(map(int, input("Enter some numbers for the second list:").split()))
print(num1)
print(num2)

merged = [x for x in itertools.chain.from_iterable(itertools.zip_longest(num1, num2))if x]
print(merged)