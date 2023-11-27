"""Given the names and grades for each student in a class of  students, 
store them in a nested list and print the name(s) of any student(s) having the lowest grade."""


result = [["Jisan", 80], ["Swoad", 60], ["Rafee", 70], ["Pranto", 50], ["Tam", 50]]
mks = []

for i in range(len(result)):
    num = result[i][1]
    mks.append(num)
    
mks.sort()
l_mks = mks[0]

for i in range(len(result)):
    if l_mks == result[i][1]:
        print(result[i][0])