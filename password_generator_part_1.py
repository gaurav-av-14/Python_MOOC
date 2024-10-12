# Write your solution here
import string
import random

random.seed = 100
def generate_password(n):
    return "".join(random.sample(string.ascii_lowercase,n))

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))
