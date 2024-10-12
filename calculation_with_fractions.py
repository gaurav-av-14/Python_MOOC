# Write your solution here
from fractions import Fraction as f
def fractionate(n: int):
    #res = f(1,n)
    # resLis=[]
    # for i in range(n):
    #     resLis.append(res)
    # return resLis
    result = [f(1,n)]*n
    return result
if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))




