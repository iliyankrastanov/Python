# port - globalna promenliva
port = 1521
# 1. Definiciya na funkciyata
def sum_numbers(a, b):
    # c - lokalna promenliva
    c = a + b
    return c


if __name__ == "__main__":
    # 2. Izvikvame funkciyata
    res = sum_numbers(10, 22)
    print(f"sum = {res}")

    x, y = 10, 22
    res = sum_numbers(x, y)
    print(f"{x} + {y} = {res}")

    print("--- --- --- ---")

