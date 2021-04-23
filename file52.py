
if __name__ == "__main__":
    actions = {
        '+': lambda a,b: a + b
    }

    try:
        val1 = float(input('first number:'))
        op = input('action (+):')
        val2 = float(input('second number:'))
        result = actions[op](val1,val2)

    except (ValueError, KeyError) as e:
        print(f'invalid value or action ({e})')
    
    except Exception as e:
        print(f"unknown error!{e}")
    else:
        print(f"{val1} {op} {val2} = {result}")
        print("--- else block ---")
    finally:
        print("--- finally block---")

    print("--- --- --- ---")


