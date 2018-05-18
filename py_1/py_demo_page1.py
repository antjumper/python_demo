import functools
# 装饰器练习


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call %s:" % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print("2018-05-17")


now()


def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kv):
            print("%s %s():" %(text, func.__name__))
            return func(*args, **kv)
        return wrapper
    return decorator


@log2("带参数的装饰器")
def now2():
    print("2018")


now2()


def log3(text):
    def decorate(func):
        def wrapper(*args, **kv):
            print("** %s %s" % (text, func.__name__))
            return func(*args, **kv)
        return wrapper
    return decorate


def log4(text):
    def decorator(func):
        def wrapper(*args, **kv):
            print("%s %s" % (text, func.__name__))
            return func(*args, **kv)
        return wrapper

    return decorator


now = log3('execute')(now)

now()

def metric(fn):
    print()

