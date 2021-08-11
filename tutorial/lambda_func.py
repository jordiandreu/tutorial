# Using lambda function in different methods:

def run_lambda_sorted():

    points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
    print(points2D)

    points2D_sorted = sorted(points2D)
    print(points2D_sorted)

    points2D_sorted = sorted(points2D, key=lambda x: x[1])
    print(points2D_sorted)

    points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
    print(points2D_sorted)


def run_lambda_map():
    # map(func, seq)
    a = [1, 2, 3, 4]
    b = map(lambda x: 2 * x, a)
    print(a)
    print(list(b))


def run_lambda_filter():
    # filter(func, seq)
    a = [1, 2, 3, 4, 5, 6]
    b = filter(lambda x: x % 2 == 0, a)
    print(a)
    print(list(b))


def run_lambda_reduce():
    # reduce(func, seq) functools
    from functools import reduce

    a = [1, 2, 3, 4]
    b = reduce(lambda x, y: x * y, a)
    print(a)
    print(b)
