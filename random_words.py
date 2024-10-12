# Write your solution from import
from random import sample

def words(n,beg):
    nwlist=[]
    with open("words.txt") as w:
        wordlist = w.readlines()
    for word in wordlist:
        if word.find(beg) == -1:
            continue
        elif word.find(beg)==0:
            nwlist.append(word)

    
    return sample(nwlist,n)

if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)
