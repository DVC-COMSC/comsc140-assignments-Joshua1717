def main():

    numlist = list(map(int, input("Enter some numbers for the list:").split()))
    sublist = list(map(int, input("Enter some numbers for the sublist:").split()))

    print(numlist)
    print(sublist)

    newlist = all(item in numlist for item in sublist)
    if newlist is True:
        print("True")
    else:
        print("False")

main()