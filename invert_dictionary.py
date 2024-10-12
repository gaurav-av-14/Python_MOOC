# Write your solution here

# damn this question. its screwed up. It said to write an in-place solution
# in the question, wasted hours on it, apparent;y immpossible, tried a work around by using extra space
# with lists. Turns out the official sol used a copy dictionary. shame
def invert(dictionary : dict):
    keys=[]
    vals=[]
    for key,value in dictionary.items():
        keys.append(key)
        vals.append(value)
    dictionary.clear()
    for i in range(len(keys)):
        dictionary[vals[i]]=keys[i]
    
        
        


        
if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)