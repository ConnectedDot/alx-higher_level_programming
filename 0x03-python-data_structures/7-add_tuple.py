#!usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    A function to add multple tuple.

    Arguments:
    - tuple_a: a tuple containing two integers (default is an empty tuple)
    - tuple_b: a tuple containing two integers (default is an empty tuple)

    Return:
    - a tuple containing two integers where the first element is the sum of the
      first element in each tuple, and the second element is the sum of the
      second element in each tuple.
    """

    a = tuple_a[0] if len(tuple_a) >= 1 else 0
    b = tuple_a[1] if len(tuple_a) >= 2 else 0
    c = tuple_b[0] if len(tuple_b) >= 1 else 0
    d = tuple_b[1] if len(tuple_b) >= 2 else 0

    return (a + c, b + d)
