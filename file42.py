def get_squares(n):
    return [ v ** 2 for v in range(n + 1)]

# 1. Definiciya
def generate_suqares(n):
    for v in range(n + 1):
        yield v ** 2

if __name__ == "__main__":
    values = get_squares(10)
    print(f"values = {values}")

    # 2. Prisvoyavane na promenliva
    n_sqr = generate_suqares(10)

    # 3. Vzimane na stoinostite
    print(f"1 => {next(n_sqr)}")
    print(f"2 => {next(n_sqr)}")
    print(f"3 => {next(n_sqr)}")
    print(f"4 => {next(n_sqr)}")
    print(f"5 => {next(n_sqr)}")

    arr = list(n_sqr)
    print(f"arr = {arr}")

    #print(f"5 => {next(n_sqr)}")
    sqr_5 = generate_suqares(5)
    for i in sqr_5:
        print(f"i = {i}")
    print("--- --- --- ---")