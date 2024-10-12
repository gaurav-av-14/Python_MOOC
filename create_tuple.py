# Write your solution here
def create_tuple(x: int, y: int, z: int):
    lis = [x,y,z] 
    lis.sort()
    my_tuple = (lis[0],lis[2],sum(lis))   
    return my_tuple

if __name__ == "__main__":
    tup = create_tuple(5, 3, -1)
    if tup[1]==3:
        print("true")
