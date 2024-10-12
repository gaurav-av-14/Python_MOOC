# Write your solution here
def dict_of_numbers():
    num2words = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
    6: 'six', 7: 'seven', 8: 'eight', 9: 'Nine', 10: 'Ten', \
    11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
    15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
    19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
    50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
    90: 'Ninety', 0: 'Zero'}

    my_dict={}

    for i in range(21):
        my_dict[i]=num2words[i].casefold()
    for i in range(21,100):
        if i%10!=0:
            my_dict[i]= num2words[(i//10)*10].casefold() + "-" + num2words[i%10].casefold()
            continue
        my_dict[i]=num2words[i].casefold()
    return my_dict

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[8])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])

