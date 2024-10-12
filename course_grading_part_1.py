# write your solution here

if True:
    
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
names = {}
#exercises ={}
with open(student_info) as nam:
    for line in nam:
        
        line = line.strip()
        parts = line.split(";")
        if parts[0]=="id":
            continue
        names[parts[0]]= parts[1]+" "+parts[2]
with open(exercise_data) as ex:
    exercisePts=[]

    for line in ex:
        line = line.strip()
        parts = line.split(";")
        if parts[0]== "id":
            continue
        exercisePts.append(sum(list(map(int, parts[1:]))))

#print(exercisePts)
exercises = {k:v for k,v in zip(names,exercisePts)}
#print(exercises)

for k in names:
    print(names[k], exercises[k])




        


