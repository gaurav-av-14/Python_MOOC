# Copy here code of line function from previous exercise
def line(n,ch):
    if ch == "":
        print("*"*n)
    else:
        print(ch[0]*n)
def square(size, character):
    # You should call function line here with proper parameters
    temp=size
    for _ in range(size):
        line(size, character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")