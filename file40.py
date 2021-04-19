def bar(a = None, b = None):
    if not a: a = []
    if not b: b = {}

    print(f"a = {a}")
    print(f"b = {b}")
    print("- " * 20)
    n = len(a)
    a.append(n)
    b[n] = n

if __name__ == "__main__":
   
    bar()
    bar([5,6,7], {"x":100})
    bar()
    bar()
    bar([5,6,7,3,6], {"x":100, "Z":2})
    bar()
    print("--- --- --- ---")