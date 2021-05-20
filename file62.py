from math import sqrt

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

    # Specialni metodi
    # function override
    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        if not isinstance(other, Point):
            raise TypeError('ro must be instance of Point')
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        if not isinstance(other, Point):
            raise TypeError('ro must be instance of Point')
        dx1 = self.x ** 2
        dy1 = self.y ** 2
        dist1 = sqrt(dx1 + dy1)
        dx2 = other.x ** 2
        dy2 = other.y ** 2
        dist2 = sqrt(dx2 + dy2)
        return dist1 > dist2

    def __add__(self, other):
        if isinstance(other, Point):
            new_x = self.x + other.x
            new_y = self.y + other.y
           
        elif isinstance(other, (int, float)):
            new_x = self.x + other
            new_y = self.y + other
        else:
            raise TypeError('ro must be instance of Point, int or float')
            
        return Point(new_x, new_y)

    @property
    def x(self):
        return self.__x # tuk trqbva da ostanat s __

    @x.setter
    def x(self, x):
        assert x >= 0, 'x must be positive'
        self.__x = x

    
    @property
    def y(self):
        return self.__y  

    @y.setter
    def y(self, y):
        assert y >= 0, 'x must be positive'
        self.__y = y

if __name__ == "__main__":
    #2. Deklaraciya na promenliva ot tipa
    # class - tiput (Point) , obekt - predstavitel (p)
    p1 = Point(16, 8)
    p2 = Point(6, 18)
    
    print(f'Point:{p2}')
    

    if p1 == p2:
        print(f'{p1} == {p2}')
    else:
        print(f'{p1} != {p2}')

    if p1 > p2:
        print(f'{p1} > {p2}')
    else:
        print(f'{p1} <= {p2}')

    p = p1 + p2
    print(f"Point: {p}")

    p = p1 + 4
    print(f"Point: {p}")

    print("--- --- --- ---")