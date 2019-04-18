
import random

# from https://docs.python.org/3.1/library/itertools.html?highlight=combinations#itertools.product
def random_product(*args, repeat=10):
    "Random selection from itertools.product(*args, **kwds)"
    pools = [tuple(pool) for pool in args] * repeat
    return tuple(random.choice(pool) for pool in pools)

for i in range(10):
    print(random_product(["left", "right", "straight"]))
