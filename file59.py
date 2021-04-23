#1. Definiciya na klas

class Point:
    # Konstruktur na klasa
    def __init__(self, x = 0, y = 0, *args, **kwargs):
        print('Point Ctor')
        # danni na klasa
        self.__x = x
        self.__y = y
    
    # Metodi na klasa
    def draw(self):
          print(f'draw point at: ({self.__x},{self.__y})')

    #def move_to(self, dx, dy):
     #   self.x += dx
     #   self.y += dy

if __name__ == "__main__":
    #2. Deklaraciya na promenliva ot tipa
    # class - tiput (Point) , obekt - predstavitel (p)
    p1 = Point()
    p2 = Point(6, 8)
    
    p2.label = 100
    p2.max_y = -400
    print(f'dot access: {p2.label}, {p2.max_y}')
    p2.draw()

    print("--- --- --- ---")