# Write your solution here
def same_chars(string,i1,i2):
    if i1>i2:
        # swap them
        # wanted to write in separate func but realized python only allows pass by value so swap function wouldnt work unles return is used which makes it cumbersome
        # found out in python we can swap by just x,y = y,x :)

        # i1 = i1 + i2
        # i2 = i1 - i2
        # i1 = i1 - i2
        
        i1,i2 = i2,i1

    if len(string)-1<i2 or i1<0:
        print("out of scope")
        return False
    elif string[i1] == string[i2]:
        
        return True
    else:
        print("unequal")
        return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 3, 1))