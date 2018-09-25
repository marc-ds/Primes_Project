from math import floor
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

def p1p2p3(a,b,c,y):
    return int((a*(y**2))+(b*y)+c)

def isprime(num):
    if abs(num) is 1: return 1
    return is_prime(abs(num))

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
    """return an iterable with a line in a given range"""
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

class Blockbuster():
    """return an iterable with n P1P2P3 objects where n is the number of P1P2P3 asked (**kwarg) on given y"""
    def __init__(self, y_start, y_stop, **kwargs):
        pass

    def __call__(self):
        pass

class SequenceSeeker():
    """seek first primes sequences of given P1, P2, P3, p_steps and columns range (k)"""
    def __init__(self, p1, p2, p3, p1_step=0, p2_step=0, p3_step=1, k=10):
        self.p1 = int(p1)
        self.p2 = int(p2)
        self.p3 = int(p3)
        self.p1_step = int(p1_step)
        self.p2_step = int(p2_step)
        self.p3_step = int(p3_step)
        self.k_range = range(-int(k)+1, int(k)+1)

    def __call__(self, min_size=3):
        big_seq = list()
        abc_seq = list()
        yv_seq = list()
        offset_seq = list()
        previous_prime = int()
        for k in self.k_range:
            primes_seq = list()
            p1, p2, p3 =(self.p1 + (self.p1_step*k)), self.p2 + (self.p2_step*k), self.p3 + (self.p3_step*k)
            a = (p1 - (2 * (p2)) + p3) / 2.
            b = (p3 - p1) / 2.
            c = p2
            yp = 1
            yn = 0
            possible_prime = p1p2p3(a, b, c, yp)
            while isprime(possible_prime):
                primes_seq.append(possible_prime)
                yp += 1
                p_previous_prime = previous_prime
                previous_prime = possible_prime
                if p_previous_prime == previous_prime and previous_prime == p1p2p3(a, b, c, yp): break
                possible_prime = p1p2p3(a, b, c, yp)
            primes_seq.append(possible_prime)
            primes_seq.reverse()
            possible_prime = p1p2p3(a, b, c, yn)
            while isprime(possible_prime):
                primes_seq.append(possible_prime)
                yn -= 1
                p_previous_prime = previous_prime
                previous_prime = possible_prime
                if p_previous_prime == previous_prime and previous_prime == p1p2p3(a, b, c, yn): break
                possible_prime = p1p2p3(a, b, c, yn)
            primes_seq.append(possible_prime)
            if len(primes_seq) > min_size:
                big_seq.append(primes_seq)
                abc_seq.append([a, b, c])
                offset_seq.append(offset(a, b))
                yv_seq.append(y_vertex(a, b))
        return yv_seq, offset_seq, abc_seq, big_seq

"""
c = Paraboctys(41,43,45)
for i in c(3):
    print(i())
s = SequenceSeeker(41,43,45)
yv_list, f_list, abc_list, pr_list = s()
print('yv: {}\nf: {}\nabc: {}\nsequence: {}'.format(yv_list, f_list, abc_list, pr_list))
s = SequenceSeeker(1,1,1)
yv_list, f_list, abc_list, pr_list = s(4)
print('yv: {}\nf: {}\nabc: {}\nsequence: {}'.format(yv_list, f_list, abc_list, pr_list))
m = pr_list[0]
n = len(pr_list[0])
print(m)
print(n)"""
