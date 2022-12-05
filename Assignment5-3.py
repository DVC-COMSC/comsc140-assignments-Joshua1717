stringvalue = input("Enter a string: ")
N = int(input("Enter number of spaces to shift elements: "))
direction = int(input("Enter the direction (0 = left, 1 = right): "))

def shiftN(stringvalue, direction, N):

    if direction == 0:
        shiftedspaces = stringvalue[N:] + stringvalue[:N]
        return shiftedspaces

    if direction == 1:
        shiftedspaces = stringvalue[len(stringvalue)-N:] + stringvalue[0:len(stringvalue)-N]
        return shiftedspaces

print(shiftN(stringvalue, direction, N))