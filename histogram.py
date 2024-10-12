# Write your solution here
def histogram(string):
    hist = {}
    for char in string:
        if char not in hist:
            hist[char]=''
        hist[char] += "*"
    for key in hist:
        print(key,"",end="")
        print(hist[key])
    

if __name__ == "__main__":
    histogram("statistically")
