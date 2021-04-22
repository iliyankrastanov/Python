def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":

    num = float(input("Enter number: "))
print(f"n = {factorial(num)}")
