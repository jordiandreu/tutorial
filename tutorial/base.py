import sys
import timeit

# Lists: ordered, mutable, allows duplicate elements
# Tuples: ordered, immutable, allows duplicate elements
# work with tuples can be faster since they are immutable objects
# Dictionary: Unordered, mutable, key-value pair
# Sets: Unordered, mutable, no duplicates
# Strings: ordered, immutable, text representation

def run_lists():
    # Creation
    mylist = ['banana', 'cherry', 'apple']
    mylists2 = list()
    print(mylist)

    # Access
    print(mylist[0])
    mylist.append('blueberry')
    print(mylist)
    mylist.pop(0)
    print(mylist)
    mylist.pop()
    print(mylist)

    # Operations
    mylist = [2, 1, 4, 3, 5]
    print(mylist)
    mylist.sort()
    new_list = sorted(mylist)
    print(new_list)
    new_list = mylist + mylist
    print(new_list)
    # Slicing
    a = mylist[::-1]
    print(a)

    # Copy
    b = a
    print(b)
    b.pop()
    print(a)
    b = mylist.copy()
    b.pop()
    print(mylist)


def run_tuples():
    # Creation
    a = (1,)
    b = tuple([2, 3, 4, 5])
    print(a)
    print(b)

    # Access
    print(b[1])

    # Slicing
    print(b[:2])

    # Operations
    c = tuple('apple')
    print(c)

    d = list(c)
    print(len(c))
    print(c.count('p'))
    print(c.index('e'))

    print(len(d))
    print(d.count('p'))
    print(d.index('e'))

    # unpack
    x, *y, z = b
    print(x)
    print(y)
    print(z)

    # Comparing lists and tuples in size
    l = [1, 4, 'hello', True]
    t = (1, 4, 'hello', True)
    print(sys.getsizeof(l), 'bytes')
    print(sys.getsizeof(t), 'bytes')

    # Iterate a tuple/list
    print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1_000_000))
    print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1_000_000))


def run_dictionaries():
    a = {'name': 'Max', 'age': 28, 'city': 'New York'}
    b = dict(name='Mary', age=27, city='Boston')
    print(a)
    print(b)
    a['email'] = 'max.xyz.com'
    print(a)
    del a['age']
    print(a)
    b.pop('age')
    print(b)

    if 'name' in a:
        print(a['name'])

    for k, v in a.items():
        print(k, v)

    c = b.copy() # or c = dict(b)
    b.popitem()
    print(b)
    print(c)

    # Merge disctionaries
    a = {'name': 'Max', 'age': 28, 'city': 'New York'}
    b = dict(name='Mary', age=27, city='Boston', email='x@y.z')

    a.update(b)
    print(a)


def run_sets():
    a = {1, 2, 3, 1, 3}
    b = set([1, 2, 3])
    c = set('Apple')
    d = {}
    e = set()

    print(a)
    print(b)
    print(c)
    print(type(d))
    print(type(e))

    b.add(4)
    print(b)
    b.remove(2)
    b.discard(2)
    b.discard(3)
    print(b)
    b.pop()
    print(b)
    b.add(1)
    b.add(2)
    b.add(3)
    print(b)

    for i in b:
        print(i)

    odd = {1, 3, 5, 7, 9}
    even = {2, 4, 6, 8}
    prime = {2, 3, 5, 7}
    print(odd.union(even))
    print(odd.intersection(even))
    print(odd.intersection(prime))

    print(even.difference(prime))
    print(prime.difference(even))
    print(even.symmetric_difference(prime))

    # Same method with update appended, will modify the set
    print(prime.issubset(odd))
    print(prime.issuperset(odd))
    print(even.isdisjoint(odd))

    a = {1, 2, 3, 4, 5, 6}
    b = a
    b.add(7)
    print(a)

    a = {1, 2, 3, 4, 5, 6}
    b = a.copy()
    b.add(7)
    print(a)

    a = frozenset([1, 2, 3, 4])
    print(type(a))


def run_strings():
    a = 'Hello World'
    print(a)
    print(a[3])
    b = a[1:5]
    print(b)

    for c in a:
        print(c)

    if 'e' in a:
        print('yes')

    if 'ell' in a:
        print('yes')

    a = '    Hello World     '
    a = a.strip()
    print(a)
    print(a.lower())
    print(a.startswith('Hel'))
    print(a.endswith('orld'))
    print(a.find('W'))
    print(a.find('Wor'))
    print(a.count('o'))
    print(a.replace('World', 'Universe'))

    s = 'Hey, how are you doing'
    print(s.split())
    print(s.split(","))

    a = s.split()
    print(a)

    print('.'.join(a))

    a = 3.5
    b = 4
    print("the values are %.2f and %d" % (a, b))
    print("the values are {:.2f} and {:d}".format(a, b))
    print(f"the values are {a:.2f} and {b*2:d}")