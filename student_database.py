# Write your solution here
def add_student(students : dict, name: str):

    students[name]= []

def avg(students,name):
    sum=0
    if len(students[name]) == 0:
        return 0
    for i in range(len(students[name])):
        sum+=students[name][i][1]
    return sum/len(students[name])


def print_student(students : dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
        return
    sum=0
    print(f"{name}: ")
    if len(students[name])!=0:
        print(f" {len(students[name])} completed courses:")
    else:
        print(" no completed courses")
        return
    for item in students[name]:
        sum+=item[1]
        print(" ", item[0],item[1])
    if sum==0:
        print(" average grade",0)
    else:
        print(" average grade", sum/len(students[name]))

    

def add_course(students : dict, name: str, course : tuple):
    
    if course[1]==0:
        return
    if len(students[name])==0:
        students[name].append(course)
        return

    for i in range(len(students[name])):
        if course[0] == students[name][i][0]:
            if course[1]> students[name][i][1]:
                students[name][i]=course
                return
        else:
            students[name].append(course)
            return

def summary(students : dict):
    print("students", len(students))
    max=0
    max_name=''
    best_avg=0
    avg_name=''
    for key in students:
        if len(students[key])>max:
            max = len(students[key])
            max_name= key
        mean = avg(students,key)
        if mean>best_avg:
            best_avg = mean
            avg_name=key
        
    print("most courses completed",max,max_name)
    print("best average grade", best_avg, avg_name)

if __name__ == "__main__":
    """
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")
    summary(students)
    """
    students = {}
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)
    summary(students)




        

