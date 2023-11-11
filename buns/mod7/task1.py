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

@validate_args
def pow_func(x):
    return x**2

func = pow_func()
print(func)


