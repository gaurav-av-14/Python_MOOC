# Write your solution here
from random import sample
def lottery_numbers(n: int, l: int, u: int):
    nums = list(range(l,u+1))
    draw = sample(nums,n)
    draw.sort()
    return draw

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)



