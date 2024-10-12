# Write your solution here
def transpose(matrix: list):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j>i:
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
if __name__ == "__main__":


    matrix = [
    [1,2,3,10],
    [4,5,6,11],
    [7,8,9,12],
    [13,14,15,16]
    ]
    print(f"Original: {matrix}")
    transpose(matrix)
    print(f"After transpose: {matrix}")
    
    