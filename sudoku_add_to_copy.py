# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    nwl = []
    nwl[:]=sudoku[::]
    for i in range(len(sudoku)):
        nwl[i]=sudoku[i].copy()
    nwl[row_no][column_no]=number
    return nwl
def print_sudoku(sudoku: list):
    row=[]
    for j in range(len(sudoku)):
        row = sudoku[j]
        if j %3 ==0 and j!=0:
            print()
        for i in range(len(row)):
            if i % 3==0 and i !=0:
                print(" ", end="")
            if row[i] == 0:
                print("_ ",end="")
            else:
                print(row[i],"",end="")
        print()
if __name__ == "__main__":

    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)