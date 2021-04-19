def foo(a):
    a = 10
    print(f"a = {a}")

def sort_values(values):
    values.sort()

def bar(a = [], b = {}):
    print(f"a = {a}")
    print(f"b = {b}")
    print("- " * 20)
    n = len(a)
    a.append(n)
    b[n] = n

if __name__ == "__main__":
    #1.
    #x = 100
    #foo(x)
    #print(f"x = {x}")

    #2.
    #arr = [9,8,6,5,3,2]
    #sort_values(arr)
    #print(f"arr = {arr}")

    #3.
    bar()
    bar([5,6,7], {"x":100})
    bar()
    bar()
    bar([5,6,7,3,6], {"x":100, "Z":2})
    bar()
    print("--- --- --- ---")