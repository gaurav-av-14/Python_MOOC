# write your solution here
txt = input("Write text: ")
words = txt.strip().split(" ")

with open("wordlist.txt") as dictt:
    wordlis=[]
    for line in dictt:

        wordlis.append(line.rstrip()) 

for i in range(len(words)):
    if words[i].casefold() not in wordlis:
        words[i]= f"*{words[i]}*"

print(" ".join(words))


