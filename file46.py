from time import time, sleep
from functools import wraps

def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(f"doc:{func.__doc__}")
        print(f"{func.__name__}: {time() - t:.4f}")
    return wrapper

@measure
def foo(sleep_time = 0.3):
    '''function foo, sleeps sleep_time sec.'''
    sleep(sleep_time)

if __name__ == "__main__":

    foo()
    foo(0.5)
    print(f"{foo.__name__} doc:{foo.__doc__}")
    print("--- --- --- ---")