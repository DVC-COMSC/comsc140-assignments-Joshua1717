import xlrd
from statistics import mean

def makeList():

    path = (r"C:\Users\joshu\Labs\comsc140-assignments-Joshua1717\student.xls")
    students = xlrd.open_workbook(path)
    sheet = students.sheet_by_index(0)

    keys = ['id', 'name', 'scores']
    valueset = [1001, 'Kim', [100, 80, 70, 60]]
    valueset2 = [1002, 'Bill', [100, 80, 80, 60]]
    valueset3 = [1003, 'Mary', [90, 80, 70, 100]]
    valueset4 = [1004, 'Kurt', [100, 100, 100, 90]]
    valueset5 = [1005, 'Amy', [100, 80, 80, 90]]

    list = ((dict(zip(keys, valueset,))), (dict(zip(keys, valueset2))), (dict(zip(keys, valueset3)))), (dict(zip(keys, valueset4))), (dict(zip(keys, valueset5)))

    return list

    
def printList(list):
    print(makeList())
   

def scoresbySubject(students):

    keys = ['1st', '2nd', '3rd', '4th']
    score1 = [100, 100, 90,100,100]
    score2 = [80, 80,80,100, 80]
    score3 = [70, 80, 70, 100, 80]
    score4 = [60, 60, 100, 100, 90]
    
    scores = ((dict(zip(keys, score1,))), (dict(zip(keys, score2))), (dict(zip(keys, score3))), (dict(zip(keys, score4))))

    print(scores)


def findStudents(students):
    #I can't figure out how to do this one.
    return result


def getAvgList(students):
    avglist = mean(students.value())
    return avglist


print(printList(makeList()))
scoresbySubject(makeList())
findStudents(makeList())
print(getAvgList(scoresbySubject(makeList())))