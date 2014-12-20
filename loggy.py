import logging
import inspect

def log(fn):
    def decorated(*args, **kwargs):
        # get the names of all the args
        arguments = inspect.getcallargs(fn, *args, **kwargs)
        argstr = "\n".join(["{}: {}".format(a, arguments[a]) for a in arguments])

        logging.debug("called {} with arguments:\n{}".format(fn.__name__, argstr))
        result = fn(*args, **kwargs)
        logging.debug("result: {}".format(result))

    return decorated

