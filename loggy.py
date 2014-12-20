import logging
import inspect

def log(fn):
    def decorated(*args, **kwargs):
        # get the names of all the args
        arguments = inspect.getcallargs(fn, *args, **kwargs)

        logging.debug("function '{}' called by '{}' with arguments:\n{}".format(
                      fn.__name__,
                      inspect.stack()[1][3],
                      arguments))
        result = fn(*args, **kwargs)
        logging.debug("result: {}\n".format(result))

    return decorated

