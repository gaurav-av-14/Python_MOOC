# Copy here code of line function from previous exercise
def line(n,ch):
    if ch == "":
        print("*"*n)
    else:
        print(ch[0]*n)

def square_of_hashes(size):
    temp=size
    # You should call function line here with proper parameters
    while temp>0:
        line(size, "#")
        temp-=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
