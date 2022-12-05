import xlrd
from functools import reduce

#exercise 1
def makeList():
	path = (r"C:\Users\joshu\Labs\comsc140-assignments-Joshua1717\student.xls")
	students = xlrd.open_workbook(path)
	#sheet = students.sheet_by_index(0)

	ws = students.sheet_by_index(0)
	rows = []

	#print (ws.nrows)

	keys = ws.row_values(0)
	#print (keys)

	students = []
	for rownumber in range(0, ws.nrows):
		#print (ws.row_values(rownumber)) 
		row = ws.row_values(rownumber)
		row[0], row[1], row[2]
		students.append(ws.row_values(rownumber))
	
	return 	students

#exercise 2
def printList(students):
	for v in zip(students):
		print(v)

#exercise 3	
def scoresbyStudent(students):
	
	scorelist = []
	for v in range(1,len(students)):
		scorelist.append(students[v])
	
	#print(scorelist)
	for i in range(0,len(scorelist)):
		scorelist[i].pop(0)
	for j in range(0,len(scorelist)):
		scorelist[j].pop(0)
		
	#print(scorelist)
	#for v in zip(*scorelist):
		#print(v)

	keys = ['1st', '2nd', '3rd', '4th', '5th']
	scorelist = dict(zip(keys, scorelist))
	#print(scorelist)
	
	return scorelist

#exercise 4
def findStudents(students):

	scores = []
	for v in range(1,len(students)):
		scores.append(students[v])

	for i in range(0,len(scores)):
		scores[i].pop(0)
	for j in range(0,len(scores)):
		scores[j].pop(0)

	sums = []
	for i in range(0,len(scores)):
		for j in range(0,3):
			total = reduce(lambda a, b: a + b, scores[i])
		sums.append(total)
	#print(sums)
	
	value = []
	result = filter(lambda x : x > 330, sums)
	for s in result:
		value.append(s)

	return value

#exercise 5
def getAvgList(students):
	studentscores = []
	for v in range(1,len(students)):
		studentscores.append(students[v])
	
	for i in range(0,len(studentscores)):
		studentscores[i].pop(0)
	for i in range(0,len(studentscores)):
		studentscores[i].pop(0)
	#print(studentscores)

	averageScores = []
	for i in range(0,len(studentscores)):
		for j in range(0,3):
			average = reduce(lambda a, b: a + b, studentscores[i]) / 4
		averageScores.append(average)
		
	return averageScores

print(' ')
print('Make a list of dictionaries from the Excel file ')
printList(makeList())
print(' ')
print('Print the list in a dictionary')
print(makeList())
print(' ')
print('Print the scores by subject ')
print(scoresbyStudent(makeList()))
print(' ')
print('Show scores geater then 330')
print(getAvgList(makeList()))
print(' ')
print('Show average scores for each student ')
print(findStudents(makeList()))
print(' ')