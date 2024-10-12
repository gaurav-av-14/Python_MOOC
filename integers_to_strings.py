# Write your solution here
def formatted(lis):
    newl=[]
    for item in lis:
    #    item = f"{item:.2f}"
    #return lis
        """Python behind the scenes creates an iterator for your list, 
        and it is the iterator which moves through your list one entry at a time. 
        The iterator is evaluated once, which means that if you then modify your list, 
        the iterator could potentially get ‘lost’ - you also can’t use the item variable to modify your list, 
        since it is just a reference to the thing in your list.
        """
        newl.append(f"{item:.2f}")
    return newl
def main():
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)

if __name__ == "__main__":
    main()