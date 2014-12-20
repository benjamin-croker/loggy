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
```

The output of the above is

```
014-12-20 11:42:17,064 called foo with arguments:
a: 1
c: 4
b: 3
e: 6
d: 5
2014-12-20 11:42:17,064 result: 19
2014-12-20 11:42:17,064 called foo with arguments:
a: 1
c: 5
b: 3
e: 90
d: 5
2014-12-20 11:42:17,065 result: 104
```