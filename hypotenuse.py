# Write your solution here
from math import sqrt as s

def main():
    print(hypotenuse(3,4)) # 5.0
    print(hypotenuse(5,12)) # 13.0
    print(hypotenuse(1,3)) # 1.4142135623730951

def hypotenuse(leg1: float, leg2: float)-> float:
    hyp = s(leg1**2 + leg2**2)
    return hyp

if __name__ == "__main__":
    main()


