# Write your solution here
name = input("Whom should I sign this to: ")
fileName = input("Where shall I save it: ")

with open(fileName,"w") as myfile:
    myfile.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")

 
with open(fileName, "a") as r:
    r.write("line 2")

with open(fileName) as r:
    for line in r:
        print(line)
        