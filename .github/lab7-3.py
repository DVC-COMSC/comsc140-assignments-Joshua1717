
def main():
    print("Enter 5 numbers:")
    numbers = []

    for i in range(0, 5):
        nums = int(input())   
        
        numbers.append(nums)

    total = sum(numbers)
    avg = total / len(numbers)

    print("The sum of numbers is:", total)
    print("The average is:", avg)
    print("The numbers greater than the average are: ", end =" ")

    for i in numbers:
        if i > avg:
            print(i, end=" ")

main()