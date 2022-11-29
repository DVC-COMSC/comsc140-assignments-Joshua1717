N = 3
student = {}
for i in range(N):
    sname = input('Enter the student name')
    student[sname] = list(map(int, input('Enter Scores').split()))
    if i == 0 or maxsum < sum(student[sname]):
        maxsum = sum(student[sname])
        maxname = sname

for k, v in student.items():
    sumsc = sum(v)
    print('key: ', k, 'Value: ', v, 'Total ', sumsc)

print('The student who has the greatest sum ', maxname, ' Socres ',
      student[maxname])