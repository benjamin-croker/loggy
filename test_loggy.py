import logging
import loggy

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

@loggy.log
def foo(a, b):
    return a+b


foo(1, 3)