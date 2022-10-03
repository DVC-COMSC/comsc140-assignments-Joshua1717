
while True:
    numbers = (input("Enter 5 numbers with space between them or x to quit: "))
    intnumbers = numbers.split()
    if numbers == "x":
        break

    # convert list to ints
    for i in range(len(intnumbers)):
        intnumbers[i] = int(intnumbers[i])
        

    print("The numbers in the list are: ", intnumbers)

    # Find max and min values
    i=1
    min = max = intnumbers[0]

    while i < len(intnumbers):
        if intnumbers[i] > max:
            max = intnumbers[i]
        if intnumbers[i] < min:
            min = intnumbers[i]
        i += 1
    print("The largest number is", max, "and the smallest number is", min)
    

