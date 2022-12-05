import numbers
import random

def main():
    print("Enter a list of numbers:")
    strval = input().split()
    numbers = []
    
    for v in strval:
        numbers.append(int(v))
    print(numbers)
    num = int(input("Enter a number from the list:"))

    count = 0
    for i in range(0, len(numbers)):
        if numbers[i] == num:
            count += 1

    print("The number", num, "appeared", count, "times")

main()

    
     
 
 
