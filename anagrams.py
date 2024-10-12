# Write your solution here
def anagrams(st1, st2)->bool:
    return sorted(st1)==sorted(st2)
    # Used .sort method first, but it doesnt work with strings as strings are not mutable
def main():
    inp1 = input("String 1: ")
    inp2 = input("String 2: ")
    print(anagrams(inp1,inp2))
if __name__ == "__main__":
    main()