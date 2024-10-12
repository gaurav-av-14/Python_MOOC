# Write your solution here
"""
def distinct_numbers(my_list: list):
    results = []
    for item in my_list:
        if item not in results:
            results.append(item)
 
    results.sort()
    return results
"""
def distinct_numbers(lis : list) -> list:
    lis.sort()
    newLis=[]
    for i in range(len(lis)):
        if i == 0:
            newLis.append(lis[i])
            continue
        if lis[i]!=lis[i-1]:
            newLis.append(lis[i])
    return newLis
def main():
    list1 = [1,1,2,3,4,6,6,6,2,5,4,3]
    result = distinct_numbers(list1)
    print(result)
if __name__ == "__main__":
    main()
