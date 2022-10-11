def main():

    numbers = [5, 20, 30, 30, 50]
    print ("The list of numbers is: ",numbers)

    delnumber = (int(input("Enter a number to delete: ")))

    while delnumber in numbers:
        numbers.remove(delnumber)
    else:
        numbers.clear()

    print (numbers)

main()