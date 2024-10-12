# Write your solution 
"""
def all_the_longest(names: list):
    result = []
 
    for name in names:
        if result == [] or len(name) > len(result[0]):
            result = [name]
        elif len(name) == len(result[0]):
            result.append(name)
 
    return result
"""


def length_of_longest(list1):
    longest = 0
    for item in list1:
        if len(item)>longest:
            longest = len(item)
    return longest

def all_the_longest(list1):
    length = length_of_longest(list1)
    nw_list=[]
    for item in list1:
        if len(item)== length:
            nw_list.append(item)
    return nw_list
def main():
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    newl=all_the_longest(my_list)
    print(newl)
if __name__ == "__main__":
    main()