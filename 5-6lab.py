def printfunction1(*str):
    print (str)
    for v in str:
        print (v)

def printfunction2(str):
    print (str)
    for v in str:
        print (v)



def main():
    str = 'Python Programming'
    printfunction1(*str)
    printfunction2(str)

    morestr = 'C++ Programing'
    printfunction1(str, morestr)
    # printfunction2(str, morestr) # Error
main()