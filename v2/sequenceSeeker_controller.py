from main_controller import *

class SequenceSeeker():
    """Seek first primes sequences of given P1, P2, P3, p_steps and columns range (k) greater than min_size"""
    def __init__(self, p1, p2, p3, p1_step=0, p2_step=0, p3_step=1, k=10):
        self.p1 = int(p1)
        self.p2 = int(p2)
        self.p3 = int(p3)
        self.p1_step = int(p1_step)
        self.p2_step = int(p2_step)
        self.p3_step = int(p3_step)
        self.k_range = range(-int(k)+1, int(k)+1)  # set the range of columns to -k >= 0 <= k

    def __call__(self, min_size=3):
        big_seq = list()

        for k in self.k_range:
            primes_seq = list()
            p1, p2, p3 =(self.p1 + (self.p1_step*k)), self.p2 + (self.p2_step*k), self.p3 + (self.p3_step*k)
            if p1 == p2 and p2 == p3: break;  # Prevent infinite loop checking if p1, p2 and p3 are the same
            a = (p1 - (2 * (p2)) + p3) / 2.
            b = (p3 - p1) / 2.
            c = p2
            yp = 1
            yn = 0

            possible_prime = p1p2p3(a, b, c, yp)
            while isprime(possible_prime):
                primes_seq.append(possible_prime)
                yp += 1
                possible_prime = p1p2p3(a, b, c, yp)

            primes_seq.append(possible_prime)  # Append the first composite after the prime sequence
            primes_seq.reverse()  # Make the composite first element and sort the list in Pn sequence

            possible_prime = p1p2p3(a, b, c, yn)
            while isprime(possible_prime):
                primes_seq.append(possible_prime)
                yn -= 1
                possible_prime = p1p2p3(a, b, c, yn)

            primes_seq.append(possible_prime)
            primes_seq.append(P1P2P3(p1,p2,p3,0))  # Append the X object to return the sequence info

            if len(primes_seq)-2 > min_size:
                big_seq.append(primes_seq)

        return big_seq
