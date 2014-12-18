import logging
import inspect

def log(fn):
    def decorated(*args, **kwargs):
        logging.debug("called {}\nargs: {}\nkeyword Args: {}".format(fn.__name__, args, kwargs))        
        result = fn(*args, **kwargs)
        logging.debug("result: {}".format(result))
    return decorated

