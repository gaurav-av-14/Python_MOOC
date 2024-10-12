# Write your solution here
def list_sum(l1,l2):
    newl = []
    for i in range(len(l1)):
        newl.append(l1[i]+l2[i])
    return newl

def main():
    list1 = [1,2,3,4]
    list2 = [5,4,3,1]
    print(list_sum(list1,list2))

if __name__ == "__main__":
    main()
