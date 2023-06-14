#!usr/bin/python3
def print_matrix_integer(zqmatrix=[[]]):
    """A function to Prints a matrix

    Arguments:
    - zqmatrix: A list of elements of the matrix
    (optional - this might be an empty array if no matrix)
    """
    for row in zqmatrix:
        for col in row:
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        print()
