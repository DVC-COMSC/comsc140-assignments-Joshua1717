names =  input("Enter students names: ").split()

print("Enter 4 scores for" , names[0], ":", end= " ")
score1 = (input(" ")).split()
print("Enter 4 scores for" , names[1], ":", end= " ")
score2 = (input(" ")).split()
print("Enter 4 scores for" , names[2], ":", end= " ")
score3 = (input(" ")).split()

for i in range(len(score1)):
    score1[i] = int(score1[i])

for i in range(len(score2)):
    score2[i] = int(score2[i])

for i in range(len(score3)):
    score3[i] = int(score3[i])

sum1 = sum(score1)
avg1 = sum1/len(score1)

sum2 = sum(score2)
avg2 = sum2/len(score2)

sum3 = sum(score3)
avg3 = sum3/len(score3)

print(f'{names[0]} {sum1} {avg1:.0f}')
print(f'{names[1]} {sum2} {avg2:.0f}')
print(f'{names[2]} {sum3} {avg3:.0f}')