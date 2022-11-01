def myfunc(lst):

numbers = [1, 2, 3]
print (id(numbers), 'numbers ID')


print(id(lst), 'ID of lst myfunc() as soon as the function starts')
lst[0] = 999
print(id(lst), 'ID of lst myfunc() after changing value')


retlst = myfunc(numbers)
retlst[0] = 999
print (id(retlst), 'retlst ID: returned from myfunc')



# return lst

