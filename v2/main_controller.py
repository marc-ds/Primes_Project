from math import floor


def roundz(f):
    """round any number .5 to the next bigger int used in offset methods"""
    if (f-floor(f)) <= 0.5:
        return int(floor(f))
    else:
        return int(floor(f))+1


def y_vertex(a, b):
    if a != 0:
        return -b / (2.*a)
    else:
        return 00


def offset(a,b):
    if a != 0:
        return roundz(y_vertex(a,b))
    else:
        return 00


class P1P2P3:
    """by P1, P2 and P3 set the values of a, b, c, y_vertex and offset, when called return f(x) = ay^2 + by + c"""
    def __init__(self, p1, p2, p3, y):
        """set a, b and c"""
        self.p1 = int(p1)
        self.p2 = int(p2)
        self.p3 = int(p3)
        self.y = int(y)
        self.a = (self.p1-(2*self.p2)+self.p3)/2.
        self.b = (self.p3-self.p1)/2.
        self.c = self.p2
        self.y_vertex = y_vertex(self.a, self.b)
        self.offset = offset(self.a, self.b)
        self.a0 = abs(self.a)
        self.b0 = -abs(self.b + 2 * self.a * self.offset)
        if self.a <= 0:
            self.c0 = -(self.c + self.a * self.offset)
        else:
            self.c0 = self.c + self.a * self.offset
        self.y_vertex0 = y_vertex(self.a0, self.b0)
        self.offset0 = offset(self.a0, self.b0)

    def __call__(self):
        """return the value of f(x) = ay^2 + by + c"""
        return int(self.a * self.y ** 2 + self.b * self.y + self.c)

    def when_f0(self):
        """return the value of f(x) = ay^2 + by + c when offset is 0"""
        return int(self.a0 * self.y ** 2 + self.b0 * self.y + self.c0)


class Paraboctys():
    """return an iterable with a line in a given range """
    def __init__(self, p1, p2, p3, p1_step=0, p2_step=0, p3_step=1, init=-20, end=20):
        self.p1 = int(p1)
        self.p2 = int(p2)
        self.p3 = int(p3)
        self.init = int(init)
        self.end = int(end)
        self.p1_step = int(p1_step)
        self.p2_step = int(p2_step)
        self.p3_step = int(p3_step)
        self.p_range = range(self.init, self.end+1)

    def __call__(self, y):
        for i in self.p_range:
            p1 = self.p1 + (self.p1_step*i)
            p2 = self.p2 + self.p2_step*i
            p3 = self.p3 + (self.p3_step*i)
            yield P1P2P3(p1, p2, p3, y)


c = Paraboctys(41,43,45)
for i in c(3):
    print(i())
