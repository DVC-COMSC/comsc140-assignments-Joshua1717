numbers = (input("Enter some numbers with space between them: "))
intnumbers = numbers.split()

# convert list to ints
for i in range(len(intnumbers)):
    intnumbers[i] = int(intnumbers[i])
    
print("Input: ")
print(intnumbers)
print("Output:")
# Find min value and sort

for i in range(len(intnumbers)):
    for j in range(i + 1, len(intnumbers)):
       
        if intnumbers[i] > intnumbers[j]:
            intnumbers[i], intnumbers[j] = intnumbers[j], intnumbers[i]
    print (intnumbers)