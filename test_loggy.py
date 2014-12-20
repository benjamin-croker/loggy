import logging
import loggy

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

@loggy.log
def foo(a, b, c=4, d=5, e=6):
    return a+b+c+d+e

foo(1, 3)
foo(1, 3, 5, e=90)