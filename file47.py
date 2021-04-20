from functools import wraps

def to_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = [f"{v}" for v in args]
        return func(*args, **kwargs)
    return wrapper
@to_string       
def concat(*args, **kwargs):
    '''Concatenate list elements with separator'''
    sep = kwargs.get('sep', ';')
    return sep.join(args)

if __name__ == "__main__":
    users = ['anna', 'maria', 'markus', 'jane']

    print(concat(*users))
    print(concat(*users, sep = ' # '))

    values = [1,2,3,4,5]
    print(concat(*values, sep = ' | '))
    print(f"{concat.__name__} doc:{concat.__doc__}")
    print("--- --- --- ---")