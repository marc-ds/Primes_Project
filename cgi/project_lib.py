from math import floor, sqrt
import gmpy2


def roundz(f):
    if (f - floor(f)) <= 0.5:
        return int(floor(f))
    else:
        return int(floor(f)) + 1


def isprime(num):
    if abs(num) is 1: return 1
    return gmpy2.is_prime(abs(num))


def abc_set(p1, p2, p3):
    a = (p1 - (2 * p2) + p3) / 2.
    b = (p3 - p1) / 2.
    c = p2
    return a, b, c


def y_vertex(a, b, c):
    if a != 0:
        y_vertex = float(-(b)) / float(2 * a)
    else:
        y_vertex = 00
    return y_vertex


def offset(a, b, c):
    if a != 0:
        return roundz(y_vertex(a, b, c))
    else:
        return 00


def a0b0c0_set(p1, p2, px):
    a, b, c = abc_set(p1, p2, px)
    f = offset(a, b, c)
    _a0 = a
    _b0 = b + 2 * (a * f)
    _c0 = c + a * (f ** 2) + (b * f)
    a0 = abs(_a0)
    b0 = -abs(_b0)
    if _a0 <= 0:
        c0 = -(_c0)
    else:
        c0 = _c0
    return a0, b0, c0


def p1p2pn(a, b, c, y):
    return int((a * (y ** 2)) + (b * y) + c)


def p1p2p3(a, b, c, y):
    return int((a * (y ** 2)) + (b * y) + c)


def density(a, b, c, yn):
    number_of_primes = int(0)
    prime_y0 = int(0)
    if isprime(p1p2pn(a, b, c, 0)): prime_y0 += 1
    if yn > 0:
        for y in range(1, yn + 1):
            if isprime(p1p2pn(a, b, c, y)):
                number_of_primes += 1
    else:
        for y in range(-1, yn - 1, -1):
            if isprime((p1p2pn(a, b, c, y))):
                number_of_primes += 1
    return int(number_of_primes), int(prime_y0)
