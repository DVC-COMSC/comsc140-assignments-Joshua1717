numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)

mylambda1 = lambda x, f : list(f(x))

mylambda2 = lambda x, f : max(f(x))

collectOddElm = lambda numbers: [ numbers.pop(i) for i in range(len(numbers)//2)]

print(mylambda1(numbers, collectOddElm))
print(mylambda2(numbers, collectOddElm))

