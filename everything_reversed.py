# Write your solution here
def everything_reversed(lis):
    nwl=[]
    for i in range(len(lis)-1,-1,-1):
        nwl.append(lis[i][::-1])
    return nwl
def main():
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
if __name__ == "__main__":
    main()
