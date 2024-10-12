# Write your solution here
#val = 1
val = 0
arr = []
while True:
    

    print("The list is now", arr)
    key = input("a(d)d, (r)emove or e(x)it: ")
    match key:
        case "d":
            # if len(arr)==0:
            #     arr.append(1)

            # else:
            val+=1
            arr.append(val)
            
        case "r":
            if len(arr)!=0:
                arr.remove(val)
                val-=1
            else :
                print("List already empty")
        case "x":
            print("Bye!")
            break

