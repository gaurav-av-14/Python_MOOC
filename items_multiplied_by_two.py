# Write your solution here  
def double_items(numbers: list):
    """
    nwl=[]
    for i in range(len(numbers)):
        nwl.append(numbers[i]*2)
    return nwl
    """
    nwl = []
    nwl = numbers[:]
    for i in range(len(nwl)):
        nwl[i]*=2
    return nwl
    
if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)
    