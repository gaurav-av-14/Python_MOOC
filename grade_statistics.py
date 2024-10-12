# Write your solution here
exampoints=[]
Nexercise=[]
exerpoints = []
points=[]
while True:

    inp = input("Exam points and exercises completed: ")
    if inp == "":
        break
    [exam,exercise] = inp.split()
    exampoints.append(int(exam))
    Nexercise.append(int(exercise))
for i in Nexercise:
    if i == 100:
        exerpoints.append(10)
    elif i >=90:
        exerpoints.append(9)
    elif i >=80:
        exerpoints.append(8)
    elif i >=70:
        exerpoints.append(7)
    elif i >=60:
        exerpoints.append(6)
    elif i >=50:
        exerpoints.append(5)
    elif i >=40:
        exerpoints.append(4)
    elif i >=30:
        exerpoints.append(3)
    elif i >=20:
        exerpoints.append(2)
    elif i >=10:
        exerpoints.append(1)
failCount=0
pointsavg=[]
for i in range(len(exampoints)):
    if exampoints[i]<10:
        failCount+=1
        pointsavg.append(exerpoints[i]+exampoints[i])
        continue
        
    pointsavg.append(exerpoints[i]+exampoints[i])
    points.append(exerpoints[i]+exampoints[i])

grades = []
for i in points:
    if 28<=i<=30:
        grades.append(5)
    elif i>=24:
        grades.append(4)
    elif i >=21:
        grades.append(3)
    elif i >=18:
        grades.append(2)
    elif i >=15:
        grades.append(1)
    else:
        grades.append(0)

grade = {
    "5": grades.count(5),
    "4": grades.count(4),
    "3": grades.count(3),
    "2": grades.count(2),
    "1": grades.count(1),
    "0": grades.count(0) + failCount
}
print("Statistics:")
print(f"Points average:{sum(pointsavg)/len(pointsavg):.1f}")
passcount = sum(grade.values())-grade.get("0")
passpercent = (passcount/sum(grade.values()))*100
print("Pass percentage:",passpercent)

