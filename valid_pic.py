# Write your solution here
from datetime import datetime
def is_it_valid(pic):
    if len(pic) != 11:
        return False
    
    if pic[6] not in ["+","-","A"]:
        return False
    pre=""
    if pic[6]=="+":
        pre='18'
    if pic[6]=="-":
        pre='19'
    if pic[6]=="A":
        pre='20'

    
    dob = pic[:4] + pre + pic[4:6]

    try:
        bday = datetime.strptime(dob,'%d%m%Y')
    except ValueError:
        return False

    pc = pic[7:10]
    cc9= int(pic[:6]+pc)
    cci= cc9%31
    string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    cc = string[cci]
    if cc != pic[-1]:
        return False
    return True

if __name__ == "__main__":
    inp = input("input pic:")
    print(is_it_valid(inp))

