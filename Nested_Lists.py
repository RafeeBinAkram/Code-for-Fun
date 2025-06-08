#Given the names and grades for each student in a class of N students, store them in a nested list and print the names of any students having the second lowest grade.


if __name__ == '__main__':
    records = []
    scoreholder=[]
    second_lowest_grader_name=[]
    for _ in range(int(input("class students number: "))):
        name = input("Enter Name: ")
        score = float(input("Enter Score: "))
        templist = [name,score]
        records.append(templist)
        scoreholder.append(score)
        scoreholder.sort()
    second_lowest_grade = scoreholder[1]
    for i in range(len(records)):
        if records[i][1] == second_lowest_grade:
            second_lowest_grader_name.append(records[i][0])
        second_lowest_grader_name.sort(key=str.lower)
    
    for i in range(len(second_lowest_grader_name)):
        print(second_lowest_grader_name[i])
            
            
    
    
    
    
        
