# Copy here code of line function from previous exercise
def line(n,ch):
    if ch == "":
        print("*"*n)
    else:
        print(ch[0]*n)

def triangle(size):
    for i in range(size):
        line((i+1), "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
