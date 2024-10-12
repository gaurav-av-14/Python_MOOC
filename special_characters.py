import string 
  

def separate_characters(value): 
    nwstr=""
    punc=""
    oth=""
    for letter in value: 
        
        # If anything other than ascii 
        # letter is present, then return 
        # False, else return True 
        if letter in string.ascii_letters: 
            nwstr+=letter
        elif letter in string.punctuation:
            punc+=letter
        else:
            oth+=letter

    return [nwstr,punc,oth]
  
parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
print(parts[0])
print(parts[1])
print(parts[2])