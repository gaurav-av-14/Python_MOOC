# Write your solution here
def length_of_longest(list1):
    longest = 0
    for item in list1:
        if len(item)>longest:
            longest = len(item)
    return longest
def main():
    my_list = ["first", "second", "fourth", "eleventh"]
    longest = length_of_longest(my_list)
    print(longest)
if __name__ == "__main__":
    main()