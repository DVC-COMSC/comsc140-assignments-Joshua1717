def main():

    numbers = [10, 20, 30]

    def makeLambda(value):
        newlist = list(map(lambda x: x + value, numbers))
        return newlist

    myaddfunction = makeLambda(100)
    myminusfunction = makeLambda(-50)
    print(myaddfunction)
    print(myminusfunction)

main()