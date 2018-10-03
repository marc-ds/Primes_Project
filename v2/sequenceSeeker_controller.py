from main_controller import *
import sympy as sp


def get_obj(item):
    return item[-1].a0


def kp_range(p_value, x_range):
    if p_value > 2:
        high_limit = sp.nextprime(p_value, x_range + 1)
        asc_range = list(sp.primerange(p_value, high_limit))
        actual_pos = sp.primepi(p_value)
        count_range = x_range - actual_pos
        if count_range <= 1:
            tmp_count = x_range
            tmp_value = p_value
            des_range = list()
            while tmp_count > 0:
                prev_prime = sp.prevprime(tmp_value)
                des_range.append(prev_prime)
                tmp_value = prev_prime
                tmp_count -= 1
            des_range.reverse()
            return des_range + asc_range

        des_range = list(sp.primerange(2, p_value))
        des_range.reverse()
        if count_range > 0:
            des_range.append(1)
            count_range -= 1
        if count_range > 0:
            des_range.append(-1)
            count_range -= 1
        low_limit = sp.nextprime(2, count_range + 1)
        tmp_list = list(sp.primerange(2, low_limit + 1))
        new_list = [i * -1 for i in tmp_list]
        des_range.reverse()
        new_list.reverse()
        d_range = new_list + des_range
        final_range = d_range + asc_range
        return final_range


class SequenceSeekerV3:

    def __init__(self, p1, p2, p3, kp2, kp3):

        self.p1 = p1
        self.p2_range = list(range_primes_above(p2, kp2))
        self.p3_range = list(range_primes_above(p3, kp3))

    def __call__(self, min_size):
        big_seq = list()

        for kp2 in self.p2_range:

            for kp3 in self.p3_range:
                primes_seq = list()
                p1 = self.p1
                p2 = kp2
                p3 = kp3
                if p1 == p2 and p2 == p3: continue;  # Prevent infinite loop checking if p1, p2 and p3 are the same
                a = (p1 - (2 * p2) + p3) / 2.
                b = (p3 - p1) / 2.
                c = p2
                possible_prime = p1p2p3(a, b, c, 0)
                if isprime(possible_prime):
                    primes_seq.append(possible_prime)
                else:
                    continue
                yp = 1
                yn = -1
                y_step = 1

                possible_prime = p1p2p3(a, b, c, yp)
                while isprime(possible_prime):
                    primes_seq.append(possible_prime)
                    yp += y_step
                    possible_prime = p1p2p3(a, b, c, yp)

                primes_seq.append(possible_prime)  # Append the first composite after the prime sequence
                primes_seq.reverse()  # Make the composite first element and sort the list in Pn sequence

                possible_prime = p1p2p3(a, b, c, yn)
                while isprime(possible_prime):
                    primes_seq.append(possible_prime)
                    yn -= y_step
                    possible_prime = p1p2p3(a, b, c, yn)

                primes_seq.append(possible_prime)
                primes_seq.append(X(p1, p2, p3))  # Append the X object to return the sequence info

                if len(primes_seq) - 3 >= min_size:
                    big_seq.append(primes_seq)

        return big_seq


class SequenceSeekerV2:
    """Seek first primes sequences of given P1, P2, P3, and columns range p2 (kp2) and p3 (kp3) greater than min_size.
    The P2 and P3 range will run only by the prime"""

    def __init__(self, p1, p2, p3, kp3=10, kp2=1000):
        self.p1 = p1
        self.p2_initial = p2
        self.p3_initial = p3
        self.kp3_range = kp_range(p3, kp3)
        self.kp2_range = kp_range(p2, kp2)

    def __call__(self, min_size=3):
        """Return the 1st prime sequence with elements >= min_size,
        the first composite for y positive (index 0) and y negative(index -2) and the X obj (index -1)"""
        big_seq = list()

        for k2 in self.kp2_range:

            for k3 in self.kp3_range:
                primes_seq = list()
                p1, p2, p3 = (self.p1, k2, k3)
                if p1 == p2 and p2 == p3: continue;  # Prevent infinite loop checking if p1, p2 and p3 are the same
                a = (p1 - (2 * (p2)) + p3) / 2.
                b = (p3 - p1) / 2.
                c = p2
                possible_prime = p1p2p3(a, b, c, 0)
                if isprime(possible_prime):
                    primes_seq.append(possible_prime)
                else:
                    continue
                yp = 1
                yn = -1
                y_step = 1

                possible_prime = p1p2p3(a, b, c, yp)
                while isprime(possible_prime):
                    primes_seq.append(possible_prime)
                    yp += y_step
                    possible_prime = p1p2p3(a, b, c, yp)

                primes_seq.append(possible_prime)  # Append the first composite after the prime sequence
                primes_seq.reverse()  # Make the composite first element and sort the list in Pn sequence

                possible_prime = p1p2p3(a, b, c, yn)
                while isprime(possible_prime):
                    primes_seq.append(possible_prime)
                    yn -= y_step
                    possible_prime = p1p2p3(a, b, c, yn)

                primes_seq.append(possible_prime)
                primes_seq.append(P1P2P3(p1, p2, p3, 0))  # Append the X object to return the sequence info

                if len(primes_seq) - 3 >= min_size:
                    big_seq.append(primes_seq)

        return big_seq


class SequenceSeeker:
    """Seek first primes sequences of given P1, P2, P3, p_steps and columns range (k) greater than min_size"""

    def __init__(self, p1, p2, p3, p1_step=0, p2_step=0, p3_step=1, kp3=10, kp2=1000, kp1=0):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p1_step = int(p1_step)
        self.p2_step = int(p2_step)
        self.p3_step = int(p3_step)
        self.kp3_range = range(-(int(kp3 * p3_step)), int(kp3 * p3_step) + 1,
                               int(p3_step) or 1)  # set the range of columns
        self.kp2_range = range(-(int(kp2 * p2_step)), int(kp2 * p2_step) + 1,
                               int(p2_step) or 1)  # to -k*step >=0<= k*step
        self.kp1_range = range(-(int(kp1 * p1_step)), int(kp1 * p1_step) + 1, p1_step or 1)  # and p step

    def __call__(self, min_size=3):
        """Return the 1st prime sequence with elements >= min_size,
        the first composite for y positive (index 0) and y negative(index -2) and the X obj (index -1)"""
        big_seq = list()

        for k1 in self.kp1_range:
            for k2 in self.kp2_range:
                for k3 in self.kp3_range:
                    primes_seq = list()
                    p1, p2, p3 = (self.p1 + k1, self.p2 + k2, self.p3 + k3)
                    if p1 == p2 and p2 == p3: continue;  # Prevent infinite loop checking if p1, p2 and p3 are the same
                    a = (p1 - (2 * (p2)) + p3) / 2.
                    b = (p3 - p1) / 2.
                    c = p2
                    possible_prime = p1p2p3(a, b, c, 0)
                    if isprime(possible_prime):
                        primes_seq.append(possible_prime)
                    else:
                        continue
                    yp = 1
                    yn = -1
                    y_step = 1

                    possible_prime = p1p2p3(a, b, c, yp)
                    while isprime(possible_prime):
                        primes_seq.append(possible_prime)
                        yp += y_step
                        possible_prime = p1p2p3(a, b, c, yp)

                    primes_seq.append(possible_prime)  # Append the first composite after the prime sequence
                    primes_seq.reverse()  # Make the composite first element and sort the list in Pn sequence

                    possible_prime = p1p2p3(a, b, c, yn)
                    while isprime(possible_prime):
                        primes_seq.append(possible_prime)
                        yn -= y_step
                        possible_prime = p1p2p3(a, b, c, yn)

                    primes_seq.append(possible_prime)
                    primes_seq.append(P1P2P3(p1, p2, p3, 0))  # Append the X object to return the sequence info

                    if len(primes_seq) - 3 >= min_size:
                        big_seq.append(primes_seq)

        return big_seq
