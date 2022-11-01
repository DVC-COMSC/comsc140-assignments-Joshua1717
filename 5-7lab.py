from email.errors import ObsoleteHeaderDefect
from numpy import number

def main(:)

    numbers = [5, 4, 3, 2, 1]

    others = numbers

    for i in range(len(numbers)-1):
        findmin(others)
        firstval, *others = others
        numbers[i] = firstval


    def findmin(numbers):
        smallest = min(numbers)
        numbers[0]= smallest
        print(smallest)
        return numbers
        


main()