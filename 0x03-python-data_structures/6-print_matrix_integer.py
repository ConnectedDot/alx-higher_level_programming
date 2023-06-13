#!usr/bin/python3
def print_matrix_integer(zqmatrix=[[]]):
    """A function to Prints a matrix

    Arguments:
    - zqmatrix: A list of elements of the matrix
    (optional - this might be an empty array if no matrix)
    """

    for row in zqmatrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                print("{:d}".format(row[i]), end="")
        else:
            print("{:d}".format(row[i]), end=" ")
    print()
