from math import floor, sqrt
from gmpy2 import is_prime
import sympy as sp


def roundz(f):
    """round any number .5 to the next bigger int used in offset methods"""
    if (f - floor(f)) <= 0.5:
        return int(floor(f))
    else:
        return int(floor(f)) + 1


def y_vertex(a, b):
    if a != 0:
        return -b / (2. * a)
    else:
        return 00


def offset(a, b):
    if a != 0:
        return roundz(y_vertex(a, b))
    else:
        return 00


def isprime(num):
    if abs(num) is 1: return 1
    return is_prime(abs(num))


def p1p2p3(a, b, c, y):
    return int((a * (y ** 2)) + (b * y) + c)


def data_type(value):
    if abs(value) is 1:
        return 'one'
    elif value is 0:
        return 'zero'
    elif isprime(value):
        return 'prime'
    elif not (sqrt(abs(value)) * 10) % 2:
        return 'sqrt_round'
    else:
        return 'composite'


def data_typey0(value):
    """Used to show the right colors ate y=-1, y=0 and y=1"""
    if abs(value) is 1:
        return 'y0_one'
    elif value is 0:
        return 'zero'
    elif isprime(value):
        return 'y0_prime'
    elif not (sqrt(abs(value)) * 10) % 2:
        return 'y0_sqrt_round'
    else:
        return 'y0_composite'


def header_type(value):
    if value < 0:
        return 'negative'
    elif value > 0:
        return 'positive'
    else:
        return 'zero'


def density(a, b, c, y_range):
    primes = int(0)
    for y in y_range:
        if isprime(p1p2p3(a, b, c, y)): primes += 1
    return primes


class P1P2P3:
    """by P1, P2 and P3 set the values of a, b, c, delta, C.G.,
    y_vertex and offset, when called return f(x) = ay^2 + by + c"""

    def __init__(self, p1, p2, p3, y):
        """initialize all attributes"""
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.y = int(y)
        self.a = (self.p1 - (2 * self.p2) + self.p3) / 2.
        self.b = (self.p3 - self.p1) / 2.
        self.c = self.p2
        self.y_vertex = y_vertex(self.a, self.b)
        self.offset = offset(self.a, self.b)
        self.delta = (self.b ** 2 - (4 * self.a * self.c))
        sqrtdelta = sqrt(abs(int(self.delta)))
        self.c_g = sqrtdelta - int(sqrtdelta)

        self.a0 = abs(self.a)
        self.b0 = -abs(self.b + (2 * self.a * self.offset))
        if self.a <= 0:
            self.c0 = -(self.c + self.a * (self.offset ** 2) + (self.b * self.offset))
        elif self.a > 0:
            self.c0 = (self.c + self.a * (self.offset ** 2) + (self.b * self.offset))

        self.y_vertex0 = y_vertex(self.a0, self.b0)
        self.offset0 = offset(self.a0, self.b0)
        self.delta0 = (self.b0 ** 2 - (4 * self.a0 * self.c0))
        sqrtdelta0 = sqrt(abs(int(self.delta0)))
        self.c_g0 = sqrtdelta0 - int(sqrtdelta0)
        self.x01 = self.a0 - self.b0 + self.c0
        self.x02 = self.c0
        self.x03 = self.a0 + self.b0 + self.c0
        self.par_type = self.par_type()
        self._result = p1p2p3(self.a, self.b, self.c, self.y)
        self._result0 = p1p2p3(self.a0, self.b0, self.c0, self.y)

    def __call__(self):
        """return the value of f(x) = ay^2 + by + c"""
        return self._result

    def when_f0(self):
        """return the value of f(x) = ay^2 + by + c when offset is 0"""
        return self._result0

    def density_pos(self, yn):
        return density(self.a, self.b, self.c, range(1, yn + 1))

    def density_neg(self, yn):
        return density(self.a, self.b, self.c, range(-yn + 1, 1))

    def density_pos0(self, yn):
        return density(self.a0, self.b0, self.c0, range(1, yn + 1))

    def density_neg0(self, yn):
        return density(self.a0, self.b0, self.c0, range(-yn + 1, 1))

    def type(self, y0=False):
        """return if the number are abs(one), composite, prime or a perfect sqrt"""
        if y0:
            return data_typey0(self._result)
        else:
            return data_type(self._result)

    def type0(self, y0=False):
        """return if the number when f0 are
        abs(one), composite, prime or a perfect sqrt"""
        if y0:
            return data_typey0(self._result0)
        else:
            return data_type(self._result0)

    def yv_type(self):
        return header_type(self.y_vertex)

    def f_type(self):
        return header_type(self.offset)

    def d_type(self):
        return header_type(self.delta)

    def cg_type(self):
        return header_type(self.c_g)

    def yv_type0(self):
        return header_type(self.y_vertex0)

    def f_type0(self):
        return header_type(self.offset0)

    def d_type0(self):
        return header_type(self.delta0)

    def cg_type0(self):
        return header_type(self.c_g0)

    def par_type(self):
        if self.y_vertex0 == 0:
            return 'SUB'
        elif self.y_vertex0 < 0.5 > 0:
            return 'ACC'
        elif self.y_vertex0 == 0.5:
            return 'DES'
        else:
            return 'none'


class X:
    """by P1, P2 and P3 set the values of a, b, c, delta, C.G.,
    y_vertex and offset, when called return f(x) = ay^2 + by + c"""

    def __init__(self, p1, p2, p3):
        """initialize all attributes"""
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.a = (self.p1 - (2 * self.p2) + self.p3) / 2.
        self.b = (self.p3 - self.p1) / 2.
        self.c = self.p2
        self.y_vertex = y_vertex(self.a, self.b)
        self.offset = offset(self.a, self.b)
        self.delta = (self.b ** 2 - (4 * self.a * self.c))
        sqrtdelta = sqrt(abs(int(self.delta)))
        self.c_g = sqrtdelta - int(sqrtdelta)

        self.a0 = abs(self.a)
        self.b0 = -abs(self.b + (2 * self.a * self.offset))
        if self.a <= 0:
            self.c0 = -(self.c + self.a * (self.offset ** 2) + (self.b * self.offset))
        elif self.a > 0:
            self.c0 = (self.c + self.a * (self.offset ** 2) + (self.b * self.offset))

        self.y_vertex0 = y_vertex(self.a0, self.b0)
        self.offset0 = offset(self.a0, self.b0)
        self.delta0 = (self.b0 ** 2 - (4 * self.a0 * self.c0))
        sqrtdelta0 = sqrt(abs(int(self.delta0)))
        self.c_g0 = sqrtdelta0 - int(sqrtdelta0)
        self.x01 = self.a0 - self.b0 + self.c0
        self.x02 = self.c0
        self.x03 = self.a0 + self.b0 + self.c0
        self.par_type = self.par_type()
        #self.xv = -self.delta/(4 * abs(self.a))
        #self.lr = 1/abs(self.xv)

    def __call__(self, y):
        """return the value of f(x) = ay^2 + by + c"""
        return p1p2p3(self.a, self.b, self.c, y)

    def when_f0(self, y):
        """return the value of f(x) = ay^2 + by + c when offset is 0"""
        return p1p2p3(self.a0, self.b0, self.c0, y)

    def density_pos(self, yn):
        return density(self.a, self.b, self.c, range(1, yn + 1))

    def density_neg(self, yn):
        return density(self.a, self.b, self.c, range(-yn + 1, 1))

    def density_pos0(self, yn):
        return density(self.a0, self.b0, self.c0, range(1, yn + 1))

    def density_neg0(self, yn):
        return density(self.a0, self.b0, self.c0, range(-yn + 1, 1))

    def type(self, y0=False):
        """return if the number are abs(one), composite, prime or a perfect sqrt"""
        if y0:
            return data_typey0(self._result)
        else:
            return data_type(self._result)

    def type0(self, y0=False):
        """return if the number when f0 are
        abs(one), composite, prime or a perfect sqrt"""
        if y0:
            return data_typey0(self._result0)
        else:
            return data_type(self._result0)

    def yv_type(self):
        return header_type(self.y_vertex)

    def f_type(self):
        return header_type(self.offset)

    def d_type(self):
        return header_type(self.delta)

    def cg_type(self):
        return header_type(self.c_g)

    def yv_type0(self):
        return header_type(self.y_vertex0)

    def f_type0(self):
        return header_type(self.offset0)

    def d_type0(self):
        return header_type(self.delta0)

    def cg_type0(self):
        return header_type(self.c_g0)

    def par_type(self):
        if self.y_vertex0 == 0:
            return 'SUB'
        elif self.y_vertex0 < 0.5 > 0:
            return 'ACC'
        elif self.y_vertex0 == 0.5:
            return 'DES'
        else:
            return 'none'


def range_primes_above(value=-10, k=10):
    current = value
    end = value + k
    if value != 1:
        value -= 1

    while current <= end:
        if value > 2:
            value = sp.nextprime(value)
        elif value == 1:
            value = 1
        elif value < -2:
            value = -sp.prevprime(abs(value))
        elif value <= -1 < 0:
            value = -1
        elif value == -1:
            value = 1

        current += 1
        yield value


def range_primes_below(value=-10, k=10):
    current = value
    end = value + k -1

    yield value

    while current <= end:
        if value > 2:
            value = sp.prevprime(value)
        elif value <= -1:
            value = -sp.nextprime(abs(value))
        elif value == 2:
            value = 1
        elif value == 1:
            value = -1

        current += 1
        yield value

def range_primes(value, k):
    below_list = list(range_primes_below(value, k+1))
    above_list = list(range_primes_above(value, k))
    below_list.pop(0)
    below_list.reverse()
    return below_list + above_list