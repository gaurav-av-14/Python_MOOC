# Write your solution here
arr = []
while True:
    inp = int(input("New Item: "))
    if inp == 0:
        print("Bye!")
        break
    arr.append(inp)
    
    print("The list now:",arr)
    print("The list in order:",sorted(arr))