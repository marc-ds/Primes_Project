from main_controller import *

class SequenceSeeker():
    """seek first primes sequences of given P1, P2, P3, p_steps and columns range (k)"""
    def __init__(self, p1, p2, p3, p1_step=0, p2_step=0, p3_step=1, kn=10):
        self.p1 = int(p1)
        self.p2 = int(p2)
        self.p3 = int(p3)
        self.p1_step = int(p1_step)
        self.p2_step = int(p2_step)
        self.p3_step = int(p3_step)
        self.k_range = range(-int(kn), int(kn)+1)

    def __call__(self, min_size=3):
        big_seq = list()
        abc_seq = list()
        yv_seq = list()
        offset_seq = list()
        previous_prime = int()
        for k in self.k_range:
            primes_seq = list()
            p1, p2, p3 =(self.p1 + (self.p1_step*k)), self.p2 + (self.p2_step*k), self.p3 + (self.p3_step*k)
            a = (p1 - 2.0 * p2 + p3) / 2.0
            b = (p3 - p1) / 2.0
            c = p2
            ypos = 1
            yneg = 0
            possible_prime = p1p2p3(a, b, c, ypos)
            while isprime(possible_prime):
                if a == b and b == c: break;
                primes_seq.append(possible_prime)
                ypos += 1
                possible_prime = p1p2p3(a, b, c, ypos)
            primes_seq.append(possible_prime)
            primes_seq.reverse()
            possible_prime = p1p2p3(a, b, c, yneg)
            while isprime(possible_prime):
                if a == b and b == c: break;
                primes_seq.append(possible_prime)
                yneg -= 1
                possible_prime = p1p2p3(a, b, c, yneg)
            primes_seq.append(possible_prime)
            if (len(primes_seq)-1) > min_size:
                big_seq.append(primes_seq)
                abc_seq.append([a, b, c])
                offset_seq.append(offset(a, b))
                yv_seq.append(y_vertex(a, b))
        return yv_seq, offset_seq, abc_seq, big_seq

    def when_f0(self, min_size):
        big_seq = list()
        abc_seq = list()
        yv_seq = list()
        offset_seq = list()
        previous_prime = int()
        for k in self.k_range:
            primes_seq = list()
            p1, p2, p3 = (self.p1 + (self.p1_step * k)), self.p2 + (self.p2_step * k), self.p3 + (self.p3_step * k)
            a = (p1 - (2 * (p2)) + p3) / 2.
            b = (p3 - p1) / 2.
            c = p2
            f = offset(a, b)
            a0 = abs(a)
            b0 = -abs(b + 2 * a * f)
            if a <= 0:
                c0 = -(c + a * f)
            else:
                c0 = c + a * f
            ypos = 1
            yneg = 0
            possible_prime = p1p2p3(a0, b0, c0, ypos)
            while isprime(possible_prime):
                primes_seq.append(possible_prime)
                ypos += 1
                p_previous_prime = previous_prime
                previous_prime = possible_prime
                if p_previous_prime == previous_prime and previous_prime == p1p2p3(a0, b0, c0, ypos): break
                possible_prime = p1p2p3(a0, b0, c0, ypos)
            primes_seq.append(possible_prime)
            primes_seq.reverse()
            possible_prime = p1p2p3(a0, b0, c0, yneg)
            while isprime(possible_prime):
                primes_seq.append(possible_prime)
                yneg -= 1
                p_previous_prime = previous_prime
                previous_prime = possible_prime
                if p_previous_prime == previous_prime and previous_prime == p1p2p3(a0, b0, c0, yneg): break
                possible_prime = p1p2p3(a0, b0, c0, yneg)
            primes_seq.append(possible_prime)
            if (len(primes_seq)-1) > min_size:
                big_seq.append(primes_seq)
                abc_seq.append([a0, b0, c0])
                offset_seq.append(offset(a0, b0))
                yv_seq.append(y_vertex(a0, b0))
        return yv_seq, offset_seq, abc_seq, big_seq
