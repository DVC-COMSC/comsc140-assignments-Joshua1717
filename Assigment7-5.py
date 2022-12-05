def main():

    
    num1 = list(map(int, input("Enter some numbers for the sublist:").split()))
    num2 = list(map(int, input("Enter some numbers for the list:").split()))

    print(num1)
    print(num2)

    if all(item in num2 for item in num1):
        print ("True")
    else:
        print("False")
    


main()