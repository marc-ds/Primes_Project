from math import floor, sqrt
from gmpy2 import is_prime

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

def isprime(num):
    if abs(num) is 1: return 1
    return is_prime(abs(num))

def p1p2p3(a,b,c,y):
    return int((a*(y**2))+(b*y)+c)

def data_type(value):
    if abs(value) is 1: return 'one'
    elif value is 0: return 'zero'
    elif isprime(value): return 'prime'
    elif not (sqrt(abs(value))*10)%2: return 'sqrt_round'
    else: return 'composite'

def header_type(value):
    if value == 0: return 'zero'
    elif value > 0: return 'positive'
    elif value < 0: return 'negative'

class P1P2P3:
    """by P1, P2 and P3 set the values of a, b, c, y_vertex and offset, when called return f(x) = ay^2 + by + c"""
    def __init__(self, p1, p2, p3, y):
        """initialize all attributes"""
        self.p1 = int(p1)
        self.p2 = int(p2)
        self.p3 = int(p3)
        self.y = int(y)
        self.a = (self.p1-(2*self.p2)+self.p3)/2.
        self.b = (self.p3-self.p1)/2.
        self.c = self.p2
        self.y_vertex = y_vertex(self.a, self.b)
        self.offset = offset(self.a, self.b)
        self.delta = int(self.b ** 2 - 4 * self.a * self.c)
        sqrtdelta = sqrt(abs(self.delta))
        self.c_g = sqrtdelta - int(sqrtdelta)
        self.a0 = abs(self.a)
        self.b0 = -abs(self.b + 2 * self.a * self.offset)
        if self.a <= 0:
            self.c0 = -(self.c + self.a * self.offset)
        else:
            self.c0 = self.c + self.a * self.offset
        self.y_vertex0 = y_vertex(self.a0, self.b0)
        self.offset0 = offset(self.a0, self.b0)
        self._result = p1p2p3(self.a, self.b, self.c, self.y)
        self._result0 = p1p2p3(self.a0, self.b0, self.c0, self.y)

    def __call__(self):
        """return the value of f(x) = ay^2 + by + c"""
        return self._result

    def when_f0(self):
        """return the value of f(x) = ay^2 + by + c when offset is 0"""
        return self._result0

    def type(self):
        """return if the number are abs(one), composite, prime or a perfect sqrt"""
        return data_type(self._result)

    def yv_type(self):
        return header_type(self._result)

    def f_type(self):
        return header_type(self._result)

    def d_type(self):
        return header_type(self._result)

    def cg_type(self):
        return header_type(self._result)
