from math import floor


def roundz(f):
    """round any number .5 to the next bigger int used in offset methods"""
    if (f-floor(f)) <= 0.5:
        return int(floor(f))
    else:
        return int(floor(f))+1


def y_vertex(a, b, c):
    if a is not 0:
        return -b / 2. * a
    else:
        return 00


def offset(a,b,c):
    if a is not 0:
        return roundz(y_vertex(a,b,c))
    else:
        return 00


class P1P2P3:
    """by P1, P2 and P3 set the values of a, b, c, y_vertex and offset, when called return f(x) = ay^2 + by + c"""
    def __init__(self, p1, p2, p3):
        """set a, b and c"""
        self.p1 = int(p1)
        self.p2 = int(p2)
        self.p3 = int(p3)
        self.a = (self.p1-(2*self.p2)+self.p3)/2.
        self.b = (self.p3-self.p1)/2.
        self.c = self.p2
        self.y_vertex = y_vertex(self.a, self.b, self.c)
        self.offset = offset(self.a, self.b, self.c)

    def __call__(self, y):
        """return the value of the f(x) = ay^2 + by + c"""
        return int(self.a * y ** 2 + self.b * y + self.c)

class P10P20P30(P1P2P3):
    """define the result of function P1P2P3 when the offset is 0"""
    def __init__(self,  p1, p2, p3):
        super().__init__(p1, p2, p3)
        self.a0 = abs(self.a)
        self.b0 = -abs(self.b + 2 * self.a * self.offset)
        if self.a <= 0:
            self.c0 = -(self.c + self.a * self.offset)
        else:
            self.c0 = self.c + self.a * self.offset
        self.y_vertex = y_vertex(self.a0, self.b0, self.c0)
        self.offset = offset(self.a0, self.b0, self.c0)


def line(obj, y, init, end):
    for x in range(init, end+1):
        yield obj(y, x)


def column(obj, x, init, end):
    for y in range(end, init-1, -1):
        yield obj(y, x)


a = P1P2P3(41,43,47)
print('a:{}, b:{}, c:{}, yv:{}, f:{}, result at y=0: {}'.format(a.a, a.b, a.c, a.y_vertex, a.offset, a(0)))
