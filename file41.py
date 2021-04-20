
def sum_numbers(n):
    print(f"n = {n}")
    if n > 1:
        return n + sum_numbers(n - 1)
    return 1

if __name__ == "__main__":
    res = sum_numbers(5)
    print(f"res = {res}")
    print("--- --- --- ---")