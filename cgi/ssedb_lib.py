from math import floor, sqrt
import sympy as sp


def roundz(f):
    """Round any number .5 to the next bigger int used in offset methods"""
    if (f - floor(f)) <= 0.5:
        return int(floor(f))
    else:
        return int(floor(f)) + 1


def isprime(num):
    """Return true to 1 , -1 and any prime, even the negatives."""
    if abs(num) == 1:
        return True
    return sp.isprime(abs(int(num)))


def nextprime(value):
    if value >= 1:
        return sp.nextprime(value)
    elif value == (0 or -1):
        return 1
    elif value == -2:
        return -1
    else:
        negative = sp.prevprime(-value)
        return negative * -1


def prevprime(value):
    if value > 2:
        return sp.prevprime(value)
    elif value == (0 or 1):
        return -1
    elif value == 2:
        return 1
    else:
        negative = sp.nextprime(abs(value))
        return negative * -1


def x_abc(a, b, c, y):
    return int((a * (y ** 2)) + (b * y) + c)


def x(p1, p2, p3, y):
    a = (p1 - (2 * p2) + p3) / 2.
    b = (p3 - p1) / 2.
    c = p2
    return (a * (y ** 2)) + (b * y) + c


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


def data_ctype(value):
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


def data_ctypey0(value):
    """Used to show the right colors at y=-1, y=0 and y=1"""
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


def header_ctype(value, dark=False):
    value = float(value)
    if not dark:
        if value < 0:
            return 'negative'
        elif value > 0:
            return 'positive'
        else:
            return 'zero'
    else:
        if value < 0:
            return 'negative_dark'
        elif value > 0:
            return 'positive_dark'
        else:
            return 'zero'


def rpdown_positive(value, k):
    if not isprime(value):
        value = prevprime(value)
    yield value
    i = 0
    while i < k - 1:
        value = prevprime(value)
        if value < 1:
            break
        i += 1
        yield value


def rpup_positive(value, k):
    if not isprime(value):
        value = nextprime(value)
    yield value
    i = 0
    while i < k - 1:
        value = nextprime(value)
        i += 1
        yield value


def range_ay2byc(a, b, c, y_init, y_end):
    for y in range(y_init, y_end + 1):
        yield x_abc(a, b, c, y)


def isinfinity(value):
    if value == 0:
        return '&infin;'
    else:
        return value


def density(a, b, c, y_range):
    primes = int(0)
    for y in y_range:
        if isprime(x_abc(a, b, c, y)): primes += 1
    return primes


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

        self.y0_vertex = y_vertex(self.a0, self.b0)
        self.offset0 = offset(self.a0, self.b0)

        self.x01 = self.a0 - self.b0 + self.c0
        self.x02 = self.c0
        self.x03 = self.a0 + self.b0 + self.c0

        self.x_y0 = x(p1, p2, p3, 0)
        self.y0v_2 = self.y0_vertex ** 2

        if self.a != 0:
            self.xv = (-1 * self.delta) / (4 * abs(self.a))
            self.lr = 1 / abs(self.a)
            self.c0_a = self.c0 / abs(self.a)
            self.y0v_2c0a = (self.y0v_2 - self.c0) / self.a
        else:
            self.xv = 00
            self.lr = 00
            self.c0_a = 00
            self.y0v_2c0a = 00

        self.xvlr = -self.xv * self.lr
        self.y0vm_xv_lr = self.y0_vertex - self.xv * self.lr
        self.y0vp_xv_lr = self.y0_vertex + self.xv * self.lr
        self.par_type = self.par_type()

    def __call__(self, y):
        """return the value of f(x) = ay^2 + by + c"""
        return x_abc(self.a, self.b, self.c, y)

    def when_f0(self, y):
        """return the value of f(x) = ay^2 + by + c when offset is 0"""
        return x_abc(self.a0, self.b0, self.c0, y)

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
            return data_ctypey0(self.x_y0)
        else:
            return data_ctype(self.x_y0)

    def type0(self, y0=False):
        """return if the number when f0 are
        abs(one), composite, prime or a perfect sqrt"""
        if y0:
            return data_ctypey0(self.x_y0)
        else:
            return data_ctype(self.x_y0)

    def yv_type(self):
        return header_ctype(self.y_vertex)

    def f_type(self):
        return header_ctype(self.offset)

    def d_type(self):
        return header_ctype(self.delta)

    def cg_type(self):
        return header_ctype(self.c_g)

    def yv_type0(self):
        return header_ctype(self.y0_vertex)

    def f_type0(self):
        return header_ctype(self.offset0)

    def par_type(self):
        if self.y0_vertex == 0:
            return 'SUB'
        elif self.y0_vertex < 0.5 > 0:
            return 'ACC'
        elif self.y0_vertex == 0.5:
            return 'DES'
        else:
            return 'none'


class SequenceSeekerV5:

    def __init__(self, p1, kp1, kp2, kp3):
        """The user set P1 and columns range (k) for P1 (kp1) P2 (kp2) and P3 (kp3)
        The initial value for P2 and P3 are P1"""

        self.p1_range = list(rpup_positive(p1, kp1))
        self.p2_k = kp2
        self.p3_k = kp3

    def __call__(self, min_size):
        """ Return an list with all sequences, each one with an x object,
        first positive and first negative composites and the 1st prime sequence in range
        P1 >= P2+p2_k >= P3+p3_k, where p2_k and p3_k are the P2 and p3 columns range"""
        big_seq = list()  # This list will archive all valid 1st sequences.
        flag = 0  # Flag to count how much interactions the program do to find that sequence.

        for p1_i in self.p1_range:
            p2_range = rpup_positive(int(p1_i), self.p2_k)
            for p2_i in p2_range:  # Start the first loop for p2, starting by P1 value.
                p3_range = rpdown_positive(int(p2_i), self.p3_k)

                for p3_i in p3_range:  # Start p3 loop out of actual p2 value, so:
                    primes_seq = list()  # P2 <= P3 <= P3+k
                    flag += 1
                    p1 = p1_i
                    p2 = p2_i
                    p3 = p3_i

                    if p1 == p2 and p2 == p3:  # Prevent infinite loop checking if p1, p2 and p3 are the same.
                        if min_size <= 1:
                            res = x(p1, p2, p3, 0)
                            primes_seq = [res, res, res, flag, X(p1, p2, p3)]
                            big_seq.append(primes_seq)
                            continue
                        else:
                            continue

                    possible_prime = x(p1, p2, p3, 0)
                    if isprime(
                            possible_prime):  # Append the value when in y=0 if is prime, if not, continue to next.
                        primes_seq.append(possible_prime)
                    else:
                        continue

                    yp = 1  # Set the first value to positives y checks and
                    yn = -1  # the first negative value to negative y check
                    y_step = 1  # and the steps that positives and negative loops.

                    possible_prime = x(p1, p2, p3, yp)
                    while isprime(possible_prime):  # While possible prime is true, keep appending
                        primes_seq.append(possible_prime)  # positives y possible_prime to prime sequence.
                        yp += y_step
                        possible_prime = x(p1, p2, p3, yp)

                    primes_seq.append(possible_prime)  # Append the first composite after the prime sequence.
                    primes_seq.reverse()  # Make the composite first element and sort the list in Pn sequence.

                    possible_prime = x(p1, p2, p3, yn)
                    while isprime(possible_prime):  # Start the loop for negative y values.
                        primes_seq.append(possible_prime)
                        yn -= y_step
                        possible_prime = x(p1, p2, p3, yn)

                    primes_seq.append(possible_prime)

                    if len(primes_seq) - 2 >= min_size:  # Check the actual sequence length excluding both
                        primes_seq.append(flag)  # composites and the object x with minimum sequence size.
                        primes_seq.append(X(p1, p2, p3))  # Append the x object to return the sequence info.
                        big_seq.append(primes_seq)

        return big_seq


class SequenceSeekerV6:

    def __init__(self, p1, kp1, kp2, kp3):
        """The user set P1 and columns range (k) for P1 (kp1) P2 (kp2) and P3 (kp3)
        The initial value for P2 and P3 are P1"""

        self.p1_range = list(rpup_positive(p1, kp1))
        self.p2_k = kp2
        self.p3_k = kp3

    def __call__(self, min_size):
        """ Return an list with all sequences, each one with an x object,
        first positive and first negative composites and the 1st prime sequence in range
        P1 >= P2+p2_k >= P3+p3_k, where p2_k and p3_k are the P2 and p3 columns range"""
        big_seq = list()  # This list will archive all valid 1st sequences.
        flag = 0  # Flag to count how much interactions the program do to find that sequence.

        for p1_i in self.p1_range:
            p2_range = rpdown_positive(int(p1_i), self.p2_k)
            for p2_i in p2_range:  # Start the first loop for p2, starting by P1 value.
                p3_range = rpup_positive(int(p2_i), self.p3_k)

                for p3_i in p3_range:  # Start p3 loop out of actual p2 value, so:
                    primes_seq = list()  # P2 <= P3 <= P3+k
                    flag += 1
                    p1 = p1_i
                    p2 = p2_i
                    p3 = p3_i

                    if p1 == p2 and p2 == p3:  # Prevent infinite loop checking if p1, p2 and p3 are the same.
                        if min_size <= 1:
                            res = x(p1, p2, p3, 0)
                            primes_seq = [res, res, res, flag, X(p1, p2, p3)]
                            big_seq.append(primes_seq)
                            continue
                        else:
                            continue

                    possible_prime = x(p1, p2, p3, 0)
                    if isprime(
                            possible_prime):  # Append the value when in y=0 if is prime, if not, continue to next.
                        primes_seq.append(possible_prime)
                    else:
                        continue

                    yp = 1  # Set the first value to positives y checks and
                    yn = -1  # the first negative value to negative y check
                    y_step = 1  # and the steps that positives and negative loops.

                    possible_prime = x(p1, p2, p3, yp)
                    while isprime(possible_prime):  # While possible prime is true, keep appending
                        primes_seq.append(possible_prime)  # positives y possible_prime to prime sequence.
                        yp += y_step
                        possible_prime = x(p1, p2, p3, yp)

                    primes_seq.append(possible_prime)  # Append the first composite after the prime sequence.
                    primes_seq.reverse()  # Make the composite first element and sort the list in Pn sequence.

                    possible_prime = x(p1, p2, p3, yn)
                    while isprime(possible_prime):  # Start the loop for negative y values.
                        primes_seq.append(possible_prime)
                        yn -= y_step
                        possible_prime = x(p1, p2, p3, yn)

                    primes_seq.append(possible_prime)

                    if len(primes_seq) - 2 >= min_size:  # Check the actual sequence length excluding both
                        primes_seq.append(flag)  # composites and the object x with minimum sequence size.
                        primes_seq.append(X(p1, p2, p3))  # Append the x object to return the sequence info.
                        big_seq.append(primes_seq)

        return big_seq
