# Write your solution here
# You can test your function by calling it within the following block
def line(n,ch):
    if ch == "":
        print("*"*n)
    else:
        print(ch[0]*n)

if __name__ == "__main__":
    line(5, "xo")