# write your solution here
def read_fruits():
    Fruits = {}
    with open("fruits.csv") as fruits:
        for line in fruits:
            #line = line.replace("\n", "")
            lis = line.split(";")
            Fruits[lis[0]] = float(lis[1])

    return Fruits

if __name__ == "__main__":
    print(read_fruits())


