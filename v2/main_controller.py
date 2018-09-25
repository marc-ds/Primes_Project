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
    def __init__(self, p1, p2, p3):
        """set a, b and c"""
        self.p1 = int(p1)
        self.p2 = int(p2)
        self.p3 = int(p3)
        self.a_value = (self.p1-(2*self.p2)+self.p3)/2.
        self.b_value = (self.p3-self.p1)/2.
        self.c_value = self.p2
        self.y_vertex = y_vertex(self.a_value, self.b_value)
        self.offset = offset(self.a_value, self.b_value)

    def __call__(self, y):
        """return the value of the f(x) = ay^2 + by + c"""
        return int(self.a_value * y ** 2 + self.b_value * y + self.c_value)

class P10P20P30(P1P2P3):
    """define the result of function P1P2P3 when the offset is 0"""
    def __init__(self,  p1, p2, p3):
        super().__init__(p1, p2, p3)
        self.a0 = abs(self.a_value)
        self.b0 = -abs(self.b_value + 2 * self.a_value * self.offset)
        if self.a_value <= 0:
            self.c0 = -(self.c_value + self.a_value * self.offset)
        else:
            self.c0 = self.c_value + self.a_value * self.offset
        self.y_vertex = y_vertex(self.a0, self.b0)
        self.offset = offset(self.a0, self.b0)


class Paraboctys(P1P2P3):
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
        a_line = self.a()
        b_line = self.b()
        c_line = self.c()
        for i in self.p_range:
            yield int(a_line.__next__() * y ** 2 + b_line.__next__() * y + c_line.__next__()) # change to send an P1P2P3 object instead int

    def a(self):
        for i in self.p_range:
            a = ((self.p1 + (self.p1_step*i)) - 2 * (self.p2 + (self.p2_step*i)) + (self.p3 + (self.p3_step*i))) / 2.
            yield a

    def b(self):
        for i in self.p_range:
            b = ((self.p3 + (self.p3_step*i)) - (self.p1 + (self.p1_step*i))) / 2.
            yield b

    def c(self):
        for i in self.p_range:
            c = self.p2 + (self.p2_step*i)
            yield c

    def y_vertex(self):
        for i in self.p_range:
            a = self.a()
            b = self.b()
            yield y_vertex(a, b)

    def offset(self):
        for i in self.p_range:
            a = self.a()
            b = self.b()
            yield offset(a, b)


def column(obj, init, end):
    for y in range(end, init-1, -1):
        yield obj(y)


a = P1P2P3(41,43,47)
b = P10P20P30(41,43,47)
c = Paraboctys(41,43,45)
print('a:{:g}, b:{:g}, c:{:g}, yv:{:g}, f:{:g}, result at y=0: {}'.format(a.a, a.b, a.c, a.y_vertex, a.offset, a(0)))
print('a0:{}, b0:{}, c0:{}, yv0:{}, f0:{}, result at y=0: {}'.format(b.a, b.b, b.c, b.y_vertex, b.offset, b(0)))
print('Column a={}'.format(list(column(a, -3, 3))))
print('a:{}\nb:{}\nc:{}\nyv:{}\nf:{}\nresult at y=0: {}\nrange:{}'.format(list(c.a()), list(c.b()), list(c.c()), list(c.y_vertex()), list(c.offset()), 'qqq', c.p_range))
print('{}'.format(list(c(2))))