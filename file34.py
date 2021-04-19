# Globalna promenliva
c = 1521
# 1. Definiciya na funkciyata
def show():
    global c
    c = 20
    print(f"c = {c}")

if __name__ == "__main__":

    #2. Izvikvame funkciyata
    print(f"before show c = {c}")
    show()
    print(f"after show c = {c}")


    print("--- --- --- ---")