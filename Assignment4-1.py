import string

alphabet = ("abcdefghijklmnopqrstuvwxyz")
#print (alphabet)

start = str(input("Enter the first letter: "))
end = str(input("Enter the last letter: "))

index_start=alphabet.find(start)
index_end= alphabet.find(end)

# Check that letters are entered
while not (str.isalpha(start)):
    start = str(input("Enter only letters for the first letter. Enter letter: "))
    index_start=alphabet.find(start)
    while not (str.isalpha(end)):
        end = str(input("Enter only letters for the last letter. Enter letter: "))
        index_end= alphabet.find(end)

# Check that start letter is less then end letter
while start > end:
    start = str(input("start letter should be less then last letter. Enter letter: "))
    end = str(input("Enter the last letter: "))
    index_start=alphabet.find(start)
    index_end= alphabet.find(end)

#print("Start = ", index_start, "End = ", index_end )

for number in range (index_start, index_end + 1):
    print(chr(97 + number),end=' ')