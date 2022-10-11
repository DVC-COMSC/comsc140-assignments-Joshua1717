def main():

    numbers = list(map(int,(5, 20, 30, 35, 50)))
    print ("The list of numbers is: ",numbers)

    numbers.insert(2, 25)
    print ("The new list of numbers is: ",numbers)

main()