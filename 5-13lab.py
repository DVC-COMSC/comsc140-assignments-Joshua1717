import numbers

numbers = [1, 2, 3, 4, 5,6,7,8,9,10]

def findevennumbers(numbers):
    even = [i for i in numbers if i %2 ==0]
    return even
            
print (findevennumbers(numbers))


 
# return the generator for the even value elements

"""
def evengen(lst):
    for v in lst:
        if v % 2 == 0:
            yield v


mylist = [1, 2, 3, 4, 5]
mygen = evengen(mylist)
print(list(mygen))
"""