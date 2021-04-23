#1. Definiciya na klas

class Point:
    # Konstruktur na klasa
    def __init__(self):
        print('Point Ctor')
        # danni na klasa
        self.x = 20
        self.y = 30
    
    # Metodi na klasa
    def draw(self):
        print(f'draw point at: ({self.x},{self.y})')

if __name__ == "__main__":
    #2. Deklaraciya na promenliva ot tipa
    # class - tiput (Point) , obekt - predstavitel (p)
    p = Point()
    p1 = Point()

    p1.x = 2
    p1.y = 4

    print(f'Point:({p.x}, {p.y})')
    print(f'Point 2:({p1.x}, {p1.y})')
    
    p.draw()
    p1.draw()
    
    print("--- --- --- ---")