
def find_key(key, **kwargs):
    try:
        print(f'{key} => {kwargs[key]}')
    except KeyError as e:
        raise
        # pass
        # print(f'invalid key ({e})')
if __name__ == "__main__":

    conn = {
        'host': 'localhost',
        'port': 3306,
        'service': 'msqld'
    }

    try:
        find_key('host', **conn)

        find_key('ip', **conn)
    except KeyError:
        pass

    print("--- --- --- ---")


