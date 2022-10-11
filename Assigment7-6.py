def main():

    
    num1 = list(map(int, input("Enter some numbers for the first list:").split()))
    num2 = list(map(int, input("Enter some numbers for the second list:").split()))

    print(num1)
    print(num2)

    merged = num1 + num2

    print ("The merged list is", merged)
    


main()