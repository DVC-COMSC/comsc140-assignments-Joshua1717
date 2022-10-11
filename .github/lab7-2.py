import random

def main():   
    numbers = []

    for count in range(10):
        numbers.append((random.randint(0, 100)))

    smallest = min(numbers)

    print(numbers, end=' ')
    print(" ")
    print("The smallest number is", smallest)
    print("The index for", smallest, "is", numbers.index(smallest))

main()