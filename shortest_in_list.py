# Write your solution here
def shortest(list1):
    len_short = 100
    shortest = ''
    for item in list1:
        if len(item)< len_short:
            shortest = item
            len_short = len(item)
    return shortest
def main():
    my_list = ["firs", "sec", "fth", "eleventh"]
    shortest = shortest(my_list)
    print(shortest)
if __name__ == "__main__":
    main()