# Write your solution here
def factorials(n: int):
    fact = {}
    for i in range(1,n+1):
        if i==1:
            fact[i]=1
            continue
        fact[i] = fact[i-1]*i
    return fact

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
