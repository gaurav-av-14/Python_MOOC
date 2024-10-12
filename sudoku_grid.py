# Write your solution here
#from sudoku_row import row_correct as row
#from sudoku_column import column_correct as column
#from sudoku_block import block_correct as block
def row_correct(sudoku: list, row_no: int):
    checked=[]
    row = sudoku[row_no]
    for i in range(len(row)):
        if row[i]==0:
            continue
        elif row[i] in checked or row[i] not in range(1,10):
            return False
        else:
            checked.append(row[i])
    return True

def column_correct(sudoku: list, column_no: int):
    checked=[]
    for row in sudoku:

    
        if row[column_no]==0:
            continue
        elif row[column_no] in checked or row[column_no] not in range(1,10):
            return False
        else:
            checked.append(row[column_no])
    return True

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

def sudoku_grid_correct(sudoku: list):
    for i in range(7):
        if row_correct(sudoku,i):
            continue
        else:
            return False
    for i in range(7):
        if column_correct(sudoku,i):
            continue
        else:
            return False
    test = [0,3,6]
    for i in test:
        for j in test:
            if not block_correct(sudoku,i,j):
                return False
    return True

def main():
    sudoku1 = [
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

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))

if __name__ == "__main__":
    main()

