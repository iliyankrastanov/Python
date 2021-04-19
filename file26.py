
if __name__ == "__main__":
    arr = [ x ** 2 for x in range(10)]

    print(f"values = {arr}")

    arr = [ f"{x} {y}" for x in range(5) for y in range(5)]
    print(f"values = {arr}")

    txt = "Hello Python"

    letters = [f"*{t}*" for t in txt]
    print(f"letters = {letters}")
    print("--- --- --- ---")