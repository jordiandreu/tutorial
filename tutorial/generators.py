# Basic generator function

def basic_generator():
    yield 1
    yield 2
    yield 3

g = basic_generator()

def run_basic():
    for i in g:
        print(i)
