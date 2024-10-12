# Copy here code of line function from previous exercise and use it in your solution
def line(n,ch):
    if ch == "":
        print("*"*n)
    else:
        print(ch[0]*n)

def shape(n,ch1,h,ch2):
    for i in range(n):
        line((i+1),ch1)
    for i in range(h):
        line(n,ch2)
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")