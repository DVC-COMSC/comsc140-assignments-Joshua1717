from unittest import result


def main():
    import random

    num1 = random.sample(range(0, 100), 10)
    num2 = random.sample(range(0, 100), 10)

    print(str(num1))
    print(str(num2))

    result = []
    for i in range(0, len(num1)):
        result.append(num1[i]+ num2[i])

    print ("Result list is " + str(result)) 

    

main()
