def main():

    num1 = list(map(int, input("Enter some numbers for the sublist:").split()))
    print ("The list of numbers is: ",num1)

    num1.insert(2, 25)
    print ("The new list of numbers is: ",num1)

main()