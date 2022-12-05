str = input("Enter some words ")
word=str.split()
smallest=largest=word[0]
word.sort()

for i in range(0,len(word)):
    if len(smallest)>len(word[i]):
        smallest=word[i]
    if len(largest)<len(word[i]):
        largest=word[i]

print("Smallest word in string is", smallest)
print("Largest word in string is", largest)