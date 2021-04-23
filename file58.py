#1. Definiciya na klas

class Point:
    # Konstruktur na klasa
    def __init__(self, x = 0, y = 0, *args, **kwargs):
        print('Point Ctor')
        # danni na klasa
        self.x = x
        self.y = y
    
    # Metodi na klasa
    def draw(self):
        print(f'draw point at: ({self.x},{self.y})')

    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy

if __name__ == "__main__":
    #2. Deklaraciya na promenliva ot tipa
    # class - tiput (Point) , obekt - predstavitel (p)
    p = Point()
    p1 = Point(6, 8)


    print(f'Point:({p.x}, {p.y})')
    print(f'Point 1:({p1.x}, {p1.y})')
    
    p.draw()
    p1.draw()
    p1.move_to(30, -3)
    p1.draw()
    
    print("--- --- --- ---")