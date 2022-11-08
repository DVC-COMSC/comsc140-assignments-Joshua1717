import numbers

numbers = [1, 2, 3, 4, 5,6,7,8,9,10]

def findevennumbers(numbers):
    even = [i for i in numbers if i %2 ==0]
    return even
            
print (findevennumbers(numbers))


 
