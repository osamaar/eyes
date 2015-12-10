import math

class Vect2d:
    '''2d vector class, supports basic vector operations'''

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vect2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vect2d(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if not isinstance(other, int) or isinstance(other, float):
            raise TypeError('Vector scalar multiplication works only with int or float')
        return Vect2d(self.x*other, self.y*other)

    def __pow__(self, other):
        return self.dot(other)

    def __len__(self):
        return 2

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y

    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def mag(self):
        return float(math.sqrt(self.x**2 + self.y**2))

    def unit(self):
        return Vect2d(self.x/self.mag(), self.y/self.mag())

