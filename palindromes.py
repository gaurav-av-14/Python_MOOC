# Write your solution here
def palindromes(st):
    rev_st = st[::-1]
    return st == rev_st

while(True):
    st = input("Please type in a palindrome:")
    if palindromes(st):
        print(st,"is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
# Note, that at this time the main program should not be written inside
#if __name__ == "__main__":

