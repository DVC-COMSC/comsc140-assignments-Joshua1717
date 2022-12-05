strval = "Python programming section 2"
print("Original string ", strval)

def getalnum(strval):
    if strval.isalnum() == False:
        str = strval.replace(" ", "")
        yield str

    else:
        print("No spaces found in original or string")

res = getalnum(strval)

for v in res:
    print(v)
