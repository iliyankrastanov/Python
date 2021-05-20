#from draw.point import Point

# Chrez __init__.py
from draw import Point

if __name__ == "__main__":
    #2. Deklaraciya na promenliva ot tipa
    # class - tiput (Point) , obekt - predstavitel (p)
    p1 = Point(16, 8)
    p2 = Point(6, 18)
    
    print(f'Point:{p2}')
    print(f'Count: {Point.count}')
    p1.draw()
    del p1

    print("--- --- --- ---")