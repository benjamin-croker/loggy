loggy
=====

## About
Use a Python decorator to automatically log function calls.


## Usage

The file `example.py` shows how loggy can be used

```python
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

# loggy will print the calling function too
def bar():
    return foo(1, 3)

bar()
```

The output of the above is

```
2014-12-20 19:35:11,982 function 'foo' called by '<module>' with arguments:
{'b': 3, 'd': 5, 'a': 1, 'e': 6, 'c': 4}
2014-12-20 19:35:11,982 result: 19

2014-12-20 19:35:11,982 function 'foo' called by '<module>' with arguments:
{'b': 3, 'd': 5, 'a': 1, 'e': 90, 'c': 5}
2014-12-20 19:35:11,982 result: 104

2014-12-20 19:35:11,983 function 'foo' called by 'bar' with arguments:
{'b': 3, 'd': 5, 'a': 1, 'e': 6, 'c': 4}
2014-12-20 19:35:11,983 result: 19
```
