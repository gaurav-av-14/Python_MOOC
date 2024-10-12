# Write your solution here
def longest_series_of_neighbours(list1):
    length = 0
    Flen = []
    nwl=[]
    for i in range(len(list1)):
        if i==len(list1)-1:
            if len(nwl)==0:
                continue
            Flen.append(len(nwl)+1)
            nwl=[]
        elif list1[i+1] - list1[i] == 1 or list1[i+1] - list1[i] == -1:
            nwl.append(list1[i])
            
        else:
            if len(nwl)==0:
                continue
            Flen.append(len(nwl)+1)
            nwl=[]
    return max(Flen)

def main():
    my_list = [1, 2, 5, 7, 6, 5, 6,7,8,9,0]
    print(longest_series_of_neighbours(my_list))

if __name__ == "__main__":
    main()
        
