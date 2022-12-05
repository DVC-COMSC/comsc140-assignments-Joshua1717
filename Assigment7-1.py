import numbers
from operator import index


def main():
    
    while True:
        numbers = (input("Enter some numbers with space between them or x to quit: "))
        intnumbers = numbers.split()
        if numbers == "x":
            break

        print(" ")

        # convert list to ints
        for i in range(len(intnumbers)):
            intnumbers[i] = int(intnumbers[i])
            

        print("The numbers in the list are: ", intnumbers)

        # Find the averavge
        total = 0
        for value in intnumbers:
            total += value
        
        avg = total / len(intnumbers)
        
        print("The sum of the numbers is:", total)
        print("The average of the numbers is:",f'{avg:.2f}')
        print("The difference between the average and each number is:")

        # Find the difference
        total = 0
        length = len(intnumbers)

        for num in range (0,length, 1):
            total = avg - intnumbers[num]
            if total < 0:
                total = total * -1
            print(f'{total:.2f}', end = ' ')
        
        print(" ")
        print(" ")
        
main()


 