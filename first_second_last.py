# Write your solution here
def first_word(sent):
    index = sent.find(" ")
    word1 = sent[:index]
    return word1


def last_word(sent):
    index = sent.rfind(" ")
    word3 = sent[index+1 : ]
    return word3


def second_word(sent):
    index = sent.find(" ")
    if sent.find(" ",index+1) == -1:
        return last_word(sent)
    word2 = sent[index+1 : sent.find(" ",index+1)]
    return word2


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))

"""
    def find_word(str, whatth):
    index = 0
    word = ""
    counter = 0
    while index < len(str):
        if str[index] == " ":
            counter += 1
            if counter == whatth:
                break
            word = ""
        else:
            word += str[index]
        index += 1
    return word

def first_word(mjono):
    return find_word(mjono, 1)

def second_word(mjono):
    return find_word(mjono, 2)

def last_word(mjono):
    return find_word(mjono, 0)
"""