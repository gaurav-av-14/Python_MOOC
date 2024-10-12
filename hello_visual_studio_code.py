# Write your solution here
while(True):
    editor = input("Which editor do you use? ")
    editor = editor.casefold()
    if editor == "visual studio code":
        print("an excellent choice!")
        break
    #elif editor== "word" or editor=="notepad": 
    elif editor in ["word", "notepad"]:
        print("awful")
    else:
        print("not good")

