# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    checked=[]
    matrix =[]
    for i in range(3):
        row = sudoku[row_no]
        matrix.append(row[column_no:column_no+3])
        for item in matrix[i]:
            if item==0:
                continue
            elif item not in range(1,10) or item in checked:
                return False
            else:
                checked.append(item)
        row_no+=1
    return True


def main():
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(sudoku, 6, 3))
    #print(block_correct(sudoku, 1, 2))

if __name__ == "__main__":
    main()