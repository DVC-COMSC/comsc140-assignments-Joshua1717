import random

num1 = random.randint(0, 100)
num2 = random.randint(0, 100)
num3 = random.randint(0, 100)

print ("The three numbers are:", num1, num2, num3)

if num1 > num2:
    num1,num2 = num2,num1
if num1 > num3:
    num1,num3 = num3,num1
if num2 > num3:
    num2,num3 = num3,num2


print ("The smallest number is:", num1)





