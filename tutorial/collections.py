from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter: receives an iterable, returns a dictionary


def run_counter():
    counter = Counter(['a', 'bb', 'ac'])
    print(counter)
    a = 'aaaaabbbbcc'
    counter = Counter(a)
    print(counter)
    print(counter.items())
    print(list(counter.elements()))
    print(counter.most_common(2))


def run_named_tuple():

    Point = namedtuple('Point', 'x, y')
    point = Point(1, -4)
    print(point)
    print(point.x, point.y)


def run_ordered_dict():
    print('Dictionaries are ordered by default from python 3.7')


# Returns defaul value is key does not exists.
def run_defaultdict():
    d = defaultdict(int)
    d['a'] = 1
    d['b'] = 2
    print(d['a'])
    print(d['c'])


def run_deque():
    a = deque([1, 2, 3, 4, 5])
    print(a)
    a.append(6)
    print(a)
    a.appendleft(0)
    print(a)
    a.pop()
    print(a)
    a.popleft()
    print(a)
    a.reverse()
    print(a)
    a.rotate(1)
    print(a)
    a.rotate(-2)
    print(a)
