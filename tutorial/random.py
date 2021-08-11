import random
import secrets
import numpy as np

def run_random():

    random.seed(1)  # Ensures reproducible ramdomization

    print(random.random())
    print(random.uniform(1, 10))
    print(random.randint(1, 10))
    print(random.randrange(1, 10))
    print(random.normalvariate(1, 0.5))
    print(random.choice(list("ABCDEFG")))
    print(random.choices(list("ABCDEFG"), k=3))
    print(random.sample(list("ABCDEFG"), 2))
    a = list("ABCDEFG")
    random.shuffle(a)
    print(a)


def run_secrets():
    a = secrets.randbelow(10)
    print(a)
    a = secrets.randbits(2)
    print(a)

    b = list("ABCDEFG")
    print(secrets.choice(b))


def run_numpy():
    a = np.random.rand(3, 4)
    print(a)
