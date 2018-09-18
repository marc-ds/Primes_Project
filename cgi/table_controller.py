from project_lib import *
import gmpy2
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
        self.p_range = range(0, (k*2)+1)

        self.p1_range = list()
        if p1_step is 0 :
            for i in self.p_range:
                self.p1_range.append(self.p1_low)
        else:
            for i in self.p_range:
                self.p1_range.append(self.p1_low + (self.p1_step * i))
        self.p2_range = list()
        if p2_step is 0 :
            for i in self.p_range:
                self.p2_range.append(self.p2_low)
        else:
            for i in self.p_range:
                self.p2_range.append(self.p2_low + (self.p2_step * i))
        self.p3_range = list()
        if p3_step is 0 :
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
            a,b,c = abc_set(p1, p2, p3)
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

    def yv_line(self, line): #return a list with (k*2)+1 size. list[0] = lower value
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
            pos_primes= int(0) #primes bigger than 0
            neg_primes= int(0) #primes smaller or equal 0
            total_primes = int(0)
            a, b, c = self.a_line[i], self.b_line[i], self.c_line[i]
            for y in range(yn, -yn, -1):
                if gmpy2.is_prime(abs(p1p2p3(a, b, c, y))):
                    total_primes += 1
                    if y > 0: pos_primes += 1
                    else: neg_primes += 1
            pos_primes_list.append(pos_primes)
            neg_primes_list.append(neg_primes)
            total_primes_list.append(total_primes)
        return pos_primes_list, neg_primes_list, total_primes_list

def fixed_generator(p1a, p2a, p3a, p1b, p2b, p3b, p1c, p2c, p3c, p1d, p2d, p3d, ya, yb):
    yv_line = list()
    f_line = list()
    a_line = list()
    b_line = list()
    c_line = list()
    full_table = list()
    aa,ba,ca = abc_set(p1a, p2a, p3a)
    ab,bb,cb = abc_set(p1b, p2b, p3b)
    ac,bc,cc = abc_set(p1c, p2c, p3c)
    ad,bd,cd = abc_set(p1d, p2d, p3d)
    a_line.append(aa)
    a_line.append(ab)
    a_line.append(ac)
    a_line.append(ad)
    b_line.append(ba)
    b_line.append(bb)
    b_line.append(bc)
    b_line.append(bd)
    c_line.append(ca)
    c_line.append(cb)
    c_line.append(cc)
    c_line.append(cd)
    yv_line.append(y_vertex(aa, ba, ca))
    yv_line.append(y_vertex(ab, bb, cb))
    yv_line.append(y_vertex(ac, bc, cc))
    yv_line.append(y_vertex(ad, bd, cd))
    f_line.append(offset(aa, ba, ca))
    f_line.append(offset(ab, bb, cb))
    f_line.append(offset(ac, bc, cc))
    f_line.append(offset(ad, bd, cd))
    for y in range(yb, ya-1, -1):
        table_line = list()
        table_line.append(p1p2p3(aa, ba, ca, y))
        table_line.append(p1p2p3(ab, bb, cb, y))
        table_line.append(p1p2p3(ac, bc, cc, y))
        table_line.append(p1p2p3(ad, bd, cd, y))
        full_table.append(table_line)
    return a_line, b_line, c_line, yv_line, f_line, full_table
