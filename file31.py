# port - globalna promenliva
port = 1521
# 1. Definiciya na funkciyata
def sum_numbers(a, b, d = None):
    # c - lokalna promenliva
    c = a + b + d if d else a + b
    return c

if __name__ == "__main__":
    # 2. Izvikvame funkciyata
    res = sum_numbers(10, 22)
    print(f"sum = {res}")

    x, y, z = 10, 22, 15
    res = sum_numbers(x, y, z)
    print(f"{x} + {y} + {z} = {res}")

    print("--- --- --- ---")


