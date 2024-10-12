# write your solution here
def cast_list(test_list, data_type):
    return list(map(data_type, test_list))
def cast_matrix(test_matrix, data_type):
    return list(map(lambda sub: list(map(data_type, sub)), test_matrix))
def row_sums():
    with open("matrix.txt") as mat:
        listOfSums = []
        tempMatrix = [line.split(",") for line in mat]
        tempMatrix = cast_matrix(tempMatrix,int)
        for lis in tempMatrix:
            listOfSums.append(sum(lis))
    return listOfSums

def row_maxs():
    with open("matrix.txt") as mat:
        listOfmaxs = []
        tempMatrix = [line.split(",") for line in mat]
        tempMatrix = cast_matrix(tempMatrix,int)
        for lis in tempMatrix:
            listOfmaxs.append(max(lis))
    return listOfmaxs


def matrix_sum():
    return sum(row_sums())
def matrix_max():
    return max(row_maxs())

if __name__ == "__main__":


    print(row_sums())
    print(row_maxs())
    print(matrix_sum())
    print(matrix_max())

