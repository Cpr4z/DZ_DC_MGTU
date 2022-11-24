import datetime
from inspect import getcallargs

logger = []
def logging_decorator(logger):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger.append({'name': func.__name__,
                           'arguments':getcallargs(func, *args, **kwargs),
                           'call_time':datetime.datetime.now(),
                           'result':func(*args, **kwargs)})
            return func(*args, **kwargs)
        return wrapper
    return decorator

if __name__ == "__main__":
    @logging_decorator(logger)
    def test_simple(a, b=2):
        return 127
    test_simple(1)
    print(logger)