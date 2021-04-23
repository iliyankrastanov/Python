
#class KeyNotFoundError(Exception):
   # pass

def find_key(key, **kwargs):
    
    if key not in kwargs:
        raise KeyError(f'key {key} not found')

    print(f'{key} => {kwargs[key]}')

    
if __name__ == "__main__":

    conn = {
        'host': 'localhost',
        'port': 3306,
        'service': 'msqld'
    }

    try:
        find_key('host', **conn)

        find_key('ip', **conn)
    except KeyError as e:
        print(e)

    print("--- --- --- ---")


