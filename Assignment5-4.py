
strval = 'Python programming section 2'
isspace = lambda string : string.isalpha()


def mystrip(strval):
    print(isspace(strval))
    str = strval.replace(" ","")
    return str
     
    

res = mystrip(strval)
print (res)