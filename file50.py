
if __name__ == "__main__":
    pow2 = lambda a: a ** 2
    pown = lambda a,n: a ** n

    print(f" 3 ** 2 = {pow2(3)}")
    print(f" 3 ** 3 = {pown(3,3)}")

#lambda izraza trqbva da e na 1 red
#izraz koito vrushta stoinost bez "return"
#moje da ima cikli no trqbva da sa s ciklichen izraz(na 1 red)

    items = [('A', 5, 7),('D', 2, 6), ('B', 4, 5), ('D', 2, 5)]

    items.sort(key = lambda el: (el[1],el[0],el[2]))
    print(f"items: {items}")
    print("--- --- --- ---")


