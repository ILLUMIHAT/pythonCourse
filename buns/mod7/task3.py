import time

def validate_args(func):
    def wrapped_func(*args, **kwargs):
        count = len(args)
        if count < 1:
            return "Not enough arguments"
        if count > 1:
            return "Too many arguments"
        if not isinstance(args[0], int):
            return "Wrong types"
        if args[0] < 0:
            return "Negative argument"
        return func(*args, **kwargs)
    return wrapped_func

def memoize(func):
    cache = {}

    def wrapped_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    wrapped_func.__name__ = func.__name__
    wrapped_func.__doc__ = func.__doc__
    return wrapped_func

class Timer:
    def __init__(self, func):
        self.func = func
        self.start_time = None
        self.end_time = None

    def __call__(self, *args, **kwargs):
        if self.start_time is None:
            self.start_time = time.time()
            result = self.func(*args, **kwargs)
            self.end_time = time.time()
            print(f"Функция {self.func.__name__} выполнилась за {self.end_time - self.start_time} секунд")
            self.start_time = None
            self.end_time = None
        else:
            result = self.func(*args, **kwargs)
        return result

@Timer
@memoize
@validate_args
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
