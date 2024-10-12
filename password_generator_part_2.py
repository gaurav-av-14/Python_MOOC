# Write your solution here

import string
from random import *

def generate_password(n,dg,sp):
    
    samplesp = list(string.ascii_lowercase) + list(string.digits) +["!","?","=","+","-","(",")","#"]
    dindex = samplesp.index("0")
    sindex = samplesp.index("!")

    # if dg==False and sp == False:
    #     return "".join(sample(string.ascii_lowercase,n))
    result= sample(string.ascii_lowercase,1)

    if dg == True:
        result += sample(string.digits,1)
    elif dg == False:
        del samplesp[dindex:sindex]
        sindex = samplesp.index("!")
        
    if sp ==True:
        result+= sample("!?=+-()#",1)
    elif sp==False:
        del samplesp[sindex:]
        


    st=result+sample(samplesp,n-len(result))
    shuffle(st)
    return "".join((st))

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(2,False,False))