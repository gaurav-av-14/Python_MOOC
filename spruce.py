# Write your solution here
def spruce(n):
    spaces = (2*n-1)//2
    t = spaces
    print("a spruce!")
    for i in range(n):
        print(" "*spaces + "*"*(2*(i+1)-1))
        spaces-=1
    print(" "*t + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)

""" def spruce(height):
    print("a spruce!")
    i = 1
    while i <= height:
        empty = height - i
        stars = 2 * i - 1
        print(" " * empty + "*" * stars)
        i += 1
    print(" " * (height - 1) + "*")
"""