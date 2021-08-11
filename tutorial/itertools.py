# Advance tools for iterators
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby,\
    count, repeat, cycle

def run_product():
    a = [1, 2]
    b = [3, 4]

    prod = product(a, b)
    print(list(prod))

    prod = product(a, b, repeat=2)
    print(list(prod))


def run_permutations():
    a = [1, 2, 3]

    perm = permutations(a)
    print(list(perm))
    perm = permutations(a, 2)
    print(list(perm))


def run_combinations():
    a = [1, 2, 3, 4]

    comb = combinations(a, 2)
    print(list(comb))
    comb = combinations_with_replacement(a, 2)
    print(list(comb))


def run_accumulate():
    a = [1, 2, 5, 3, 4]
    accu = accumulate(a)
    print(list(accu))

    import operator
    accu = accumulate(a, operator.mul)
    print(list(accu))
    accu = accumulate(a, max)
    print(list(accu))
    accu = accumulate(a, lambda x, y: 2*(x + y) )
    print(list(accu))


def run_groupby():
    print('Attention, it brakes when a value changes, does not acumulate')
    a = [1, 2, 3, 4]
    grp_obj = groupby(a, key=lambda x: x < 3)
    for k, v in grp_obj:
        print(k, list(v))

    a = [{'name': 'Tim', 'age': 25},
         {'name': 'Tom', 'age': 25},
         {'name': 'Mary', 'age': 27},
         {'name': 'Tim', 'age': 28}]

    grp_obj = groupby(a, key=lambda x: x['name'])
    for k, v in grp_obj:
        print(k, list(v))

    grp_obj = groupby(a, key=lambda x: x['age'])
    for k, v in grp_obj:
        print(k, list(v))


def run_infinite():
    for i in count(4):
        print(i)
        if i == 10:
            break
    c = 0
    for i in cycle(['a', 'b', 'c']):
        print(i)
        c += 1
        if c == 5:
            break
    c = 0
    for i in repeat('aaa'):
        print(i)
        c += 1
        if c == 5:
            break
