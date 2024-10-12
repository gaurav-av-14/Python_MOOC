# Write your solution here
def most_common_character(st):
    mcc = ""
    count = 0
    for i in st:
        if st.count(i)>count:
            mcc = i
            count = st.count(i)
    return mcc
def main():
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
if __name__ == "__main__":
    main()
