def foo():
    print("Hello Python")

if __name__ == "__main__":
    num = float(input("Enter a number:"))
    res = ""

    if num > 0:
        res = "positive number"
    elif num < 0:
        res = "negative number"
    else:
        res = "result equal to 0 or invalid value"
    foo()
    print(f"{num} is a {res}")
    print("--- ---")