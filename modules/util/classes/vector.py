class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def toTuple(self):
        return (self.x, self.y)


    def unitize(self):
        length = self.length()
        if length == 0:
            return self
        return self.__class__(self.x/length, self.y/length)


    @classmethod
    def zero(cls):
        return cls(0, 0)


    def clone(self):
        return self.__class__(self.x, self.y)


    def __getitem__(self, arg):
        return [self.x, self.y][arg]


    def add(self, other):
        self.x += other[0]
        self.y += other[1]

    def __add__(self, other):
        return self.__class__(
            self.x+other[0], self.y+other[1]
        )


    def sub(self, other):
        self.x -= other[0]
        self.y -= other[1]

    def __sub__(self, other):
        return self.__class__(
            self.x-other[0], self.y-other[1]
        )


    def mul(self, n):
        self.x *= n
        self.y *= n

    def __mul__(self, n):
        return self.__class__(self.x*n, self.y*n)


    def length(self):
        return ((self.x**2)+(self.y**2)) ** (1/2)

    def __len__(self):
        return self.length()


    def __eq__(self, other):
        return self.x==other.x and self.y==other.y


    def __bool__(self):
        return self.x+self.y != 0
