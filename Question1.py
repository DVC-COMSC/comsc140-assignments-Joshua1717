words = input("Enter some words: ").split()

keyword = input ("Enter a keyword: ")

output = [i for i in words if any(char in keyword for char in i)]

print(output)


