# Write your solution here
"""
def no_vowels(my_string: str):
    vowels = "aeiou"
    result = ""
 
    for letter in my_string:
        if letter not in vowels:
            result += letter
 
    return result
"""
def no_vowels(st):
    nwst=""
    for i in st:
        if i != "a" and i!="e" and i!= "i" and i!="o" and i!="u":
            nwst+=i
    return nwst

def main():
    my_string = "this is an example"
    print(no_vowels(my_string))

if __name__ == "__main__":
    main()

