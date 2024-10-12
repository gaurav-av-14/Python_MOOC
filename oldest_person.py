# Write your solution here
def oldest_person(people: list):
    yr = people[0][1]
    name = people[0][0]
    for i in range(len(people)):
        if people[i][1]<yr:
            yr = people[i][1]
            name = people[i][0]
    return name

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))

