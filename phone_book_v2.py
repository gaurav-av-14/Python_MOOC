# Write your solution here
# Write your solution here
phonebook={}




while True:
    op=input("command (1 search, 2 add, 3 quit): ")
    op = int(op)
    if op ==2:
        
        name = input("name: ")
        if name not in phonebook:
            phonebook[name] = []
        phonebook[name].append(input("number: "))
        
        print("ok!")
    elif op == 1:
        name = input("name: ")
        if name not in phonebook:
            print("no number")
            continue
        #print(phonebook[name])
        for item in phonebook[name]:
            print(item)
    else:
        print("quitting...")
        break


