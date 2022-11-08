numbers = [1, 2, 3]
print (id(numbers), 'numbers ID')




def myfunc(lst):
    print (id(lst), 'ID of lst in myfunc() as soon as the function starts')
    lst = [999, 2, 3]
    #lst[0] = 999
    print (id(lst), 'ID of lst in myfunc() after changing value')

    return lst

retlst = myfunc(numbers)
retlst[0] = 999
print (id(retlst), 'retlst ID: returned from myfunc')





# return lst

