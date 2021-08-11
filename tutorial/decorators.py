# Decorators usage: timer functions, count executions, debug call function info, register functions, chache return values,



# 1) Simple decorator
def start_end_decorator(func):

    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper


# Idea behind decorator
def foo():
    print("This function will be redefined as decorated")


foo = start_end_decorator(foo)
foo()


@start_end_decorator
def bar():
    print("This function has been decorated")

bar()


# 2) Decorate function which has arguments

def decorator_with_arguments(func):

    def wrapper(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("End")

    return wrapper

@decorator_with_arguments
def bar_no_return(x):
    print(f'The passed argument is {x}')

bar_no_return('my_argument')

# 3) Decorate function which has arguments and return

def decorator_with_arguments_and_return(func):

    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper


@decorator_with_arguments_and_return
def add5(x):
    return x + 5

print(add5(10))

# Beware about the identity of the decorated function

print(help(add5))
print(add5.__name__)

# 4) Use functools to preserve identity
import functools


def decorator_template(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper


@decorator_template
def add10(x):
    return x + 10


print(help(add10))
print(add10.__name__)


# 5) Decorator with arguments

def repeat(num_times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(num_times=3)
def greet(name):
    greeting = f'Hello {name}'
    print(greeting)
    return

greet('Alex')


# 6) Stack decorators

@repeat(3)
@decorator_template
def greet_again(name):
    greeting = f'Hello again {name}'
    print(greeting)
    return


greet_again('Alex')

# 7) class decorator: if you want to maintain an state


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This has been executed {self.num_calls} times')
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print('Hello')

@CountCalls
def say_bye():
    print('Bye')


say_hello()
say_hello()
say_bye()