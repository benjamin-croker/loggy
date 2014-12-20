# example.py
import logging
import loggy

# set the logging configuration as desired
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

# use a decorator to indicate the function should be logged
# loggy will log at a DEBUG level
@loggy.log
def foo(a, b, c=4, d=5, e=6):
    return a+b+c+d+e

# each time foo is called, the input arguments and output is logged
foo(1, 3)
foo(1, 3, 5, e=90)