# Write your solution here
def who_won(game_board: list):
    one_count=0
    two_count=0

    for row in game_board:
        one_count+= row.count(1)
        two_count+= row.count(2)
    if one_count == two_count:
        return 0
    elif one_count>two_count:
        return 1
    else:
        return 2
def main():
    matrix = [[1,2,1],[0,0,2],[1,2,2],[1,1,2]]
    print(matrix)
    print(who_won(matrix))
if __name__ == "__main__":
    main()