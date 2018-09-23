import gmpy2
from math import floor
from sympy import primefactors


def roundz(f):
    if (f-floor(f)) <= 0.5:
        return int(floor(f))
    else:
        return int(floor(f))+1

def isprime(num):
    if abs(num) is 1: return 1
    return gmpy2.is_prime(abs(num))

def abc_set(p1,p2,p3):
    a = (p1-(2*p2)+p3)/2.
    b = (p3-p1)/2.
    c = p2
    return a, b, c

def y_vertex(a,b,c):
    if a!=0:
        y_vertex = float(-(b))/float(2*a)
    else:
        y_vertex = float(00)
    return y_vertex

def offset(a,b,c):
    if a!=0:
        return roundz(-b/float(2*a))
    else:
        return 00

def p1p2p3(a,b,c,y):
    return int((a*(y**2))+(b*y)+c)


class table_generator():

    def __init__(self, p1_init, p2_init, p3_init, p1_step, p2_step, p3_step, k):
        self.k = k
        self.p1_step = p1_step
        self.p2_step = p2_step
        self.p3_step = p3_step
        self.p1_low = p1_init - (p1_step * k)
        self.p2_low = p2_init - (p2_step * k)
        self.p3_low = p3_init - (p3_step * k)
        self.p3_high = p3_init + (p3_step * (k))
        self.p2_high = p2_init + (p2_step * (k))
        self.p1_high = p1_init + (p1_step * (k))
        self.p_range = range(0, (k * 2) + 1)

        self.p1_range = list()
        if p1_step is 0:
            for i in self.p_range:
                self.p1_range.append(self.p1_low)
        else:
            for i in self.p_range:
                self.p1_range.append(self.p1_low + (self.p1_step * i))
        self.p2_range = list()
        if p2_step is 0:
            for i in self.p_range:
                self.p2_range.append(self.p2_low)
        else:
            for i in self.p_range:
                self.p2_range.append(self.p2_low + (self.p2_step * i))
        self.p3_range = list()
        if p3_step is 0:
            for i in self.p_range:
                self.p3_range.append(self.p3_low)
        else:
            for i in self.p_range:
                self.p3_range.append(self.p3_low + (self.p3_step * i))

        self.a_line = list()
        self.b_line = list()
        self.c_line = list()

        for i in self.p_range:
            if self.p1_step is 0:
                p1 = self.p1_low
            else:
                p1 = self.p1_range[i]
            if self.p2_step is 0:
                p2 = self.p2_low
            else:
                p2 = self.p2_range[i]
            if self.p3_step is 0:
                p3 = self.p3_low
            else:
                p3 = self.p3_range[i]
            a, b, c = abc_set(p1, p2, p3)
            self.a_line.append(a)
            self.b_line.append(b)
            self.c_line.append(c)

    def p_range():
        return p_range

    def p1_range():
        return p1_range

    def p2_range():
        return p2_range

    def p3_range():
        return p3_range

    def yv_line(self, line):  # return a list with (k*2)+1 size. list[0] = lower value
        for i in self.p_range:
            line.append(y_vertex(self.a_line[i], self.b_line[i], self.c_line[i]))
        return line

    def f_line(self, line):
        for i in self.p_range:
            line.append(offset(self.a_line[i], self.b_line[i], self.c_line[i]))
        return line

    def a_line():
        return a_line

    def b_line():
        return b_line

    def c_line():
        return c_line

    def table_line(self, line, y):
        for i in self.p_range:
            line.append(p1p2p3(self.a_line[i], self.b_line[i], self.c_line[i], y))
        return line

    def density_line(self, yn):
        pos_primes_list = list()
        neg_primes_list = list()
        total_primes_list = list()
        for i in self.p_range:
            pos_primes = int(0)  # primes bigger than 0
            neg_primes = int(0)  # primes smaller or equal 0
            total_primes = int(0)
            a, b, c = self.a_line[i], self.b_line[i], self.c_line[i]
            for y in range(yn, -yn, -1):
                if isprime(abs(p1p2p3(a, b, c, y))):
                    total_primes += 1
                    if y > 0:
                        pos_primes += 1
                    else:
                        neg_primes += 1
            pos_primes_list.append(pos_primes)
            neg_primes_list.append(neg_primes)
            total_primes_list.append(total_primes)
        return pos_primes_list, neg_primes_list, total_primes_list

    def primes_sequences(self, min_size):
        big_seq = list()
        abc_seq = list()
        yv_seq = list()
        offset_seq = list()
        previous_prime = int()
        p_previous_prime = int()
        for i in self.p_range:
            primes_seq = list()
            a, b, c = self.a_line[i], self.b_line[i], self.c_line[i]
            yp = 1
            yn = 0
            possible_prime = p1p2p3(a, b, c, yp)
            while isprime(possible_prime):
                primes_seq.append(possible_prime)
                yp += 1
                p_previous_prime = previous_prime
                previous_prime = possible_prime
                if p_previous_prime == previous_prime and previous_prime == p1p2p3(a, b, c, yp):break
                possible_prime = p1p2p3(a, b, c, yp)
            primes_seq.append(possible_prime)
            primes_seq.reverse()
            possible_prime = p1p2p3(a, b, c, yn)
            while isprime(possible_prime):
                primes_seq.append(possible_prime)
                yn -= 1
                p_previous_prime = previous_prime
                previous_prime = possible_prime
                if p_previous_prime == previous_prime and previous_prime == p1p2p3(a, b, c, yn):break
                possible_prime = p1p2p3(a, b, c, yn)
            primes_seq.append(possible_prime)
            if len(primes_seq) > min_size:
                big_seq.append(primes_seq)
                abc_seq.append([a, b, c])
                offset_seq.append(offset(a,b,c))
                yv_seq.append(y_vertex(a,b,c))
        return yv_seq, offset_seq, abc_seq, big_seq


p1 = float(input('P1 value = ') or 1)
p2 = float(input('P2 value = ') or 1)
p3 = float(input('P3 value = ') or 1)
step1 = int(input('P1 Step (default: 0) = ') or 0)
step2 = int(input('P2 Step (default: 0) = ') or 0)
step3 = int(input('P3 Step (default: 1) = ') or 1)
k = int(input('K value (default: 10) = ') or 10)
min_size = int(input('Minimum size for sequence (default: 7) = ') or 7)
print()
"""p1, p2, p3, k = 1, 1, 1, 5
step1, step2, step3 = 0, 0, 1
a, b, c = abc_set(p1,p2,p3)
min_size = 5"""
calc = table_generator(p1,p2,int(p3),step1,step2,step3,k)
yv_seq, off_seq, abc_seq, big_seq = calc.primes_sequences(min_size)
for i in range(0, len(big_seq)):
    first = int(big_seq[i].pop(0))
    last = int(big_seq[i].pop())
    yv_txt = 'y_vertex: {:3.4g} | '.format(yv_seq[i])
    off_txt = 'offset: {:3} | '.format(off_seq[i])
    a_txt = 'a: {:3g} | '.format(abc_seq[i][0])
    b_txt = 'b: {:3g} | '.format(abc_seq[i][1])
    c_txt = 'c: {:3g} | '.format(abc_seq[i][2])
    length = len(big_seq[i]) - big_seq[i].count(1) - big_seq[i].count(-1)
    l_txt = 'Primes in the above sequence: {}.'.format(length)
    print(yv_txt + off_txt, a_txt + b_txt + c_txt + l_txt)
    print('({} {})'.format(first,primefactors(first)), end=' '); print(*big_seq[i], sep=' ', end=' '); print('({} {})'.format(last,primefactors(last)))
    print('\n----------------------------------------------------------------------------------------------\n')
