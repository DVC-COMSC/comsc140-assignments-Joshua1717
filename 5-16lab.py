import numbers


greater = lambda a, b : a if(a > b) else b
print(greater(10, 20))

numbers = [10, 30, 40, 55, 60]
mylist = list(filter(lambda number: number > 50, numbers))

print(mylist)