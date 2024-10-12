# write your solution here
def largest():
    #largest = 0
    with open("numbers.txt") as nums:
        """
            for i in nums:
                i = int(i)
                if i > largest:
                    largest =i
        return largest
        """
        sorted_nums = sorted(nums)
    return int(sorted_nums[-1])

if __name__ == "__main__":
    print(largest())



