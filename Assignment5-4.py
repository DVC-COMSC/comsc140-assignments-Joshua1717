


from functools import reduce


strval = 'Python programming section 2'


def mystrip(strval):
    
    return reduce(lambda x, y: (x + y) if(y != " ") else x, strval )
     
    

res = mystrip(strval)
print (res)