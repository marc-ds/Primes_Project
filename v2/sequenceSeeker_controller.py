from main_controller import *
from sympy import sieve

class SequenceSeeker():
    """Seek first primes sequences of given P1, P2, P3, p_steps and columns range (k) greater than min_size"""
    def __init__(self, p1, p2, p3, p1_step=0, p2_step=0, p3_step=1, kp3=10, kp2=1000, kp1=0):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p1_step = int(p1_step)
        self.p2_step = int(p2_step)
        self.p3_step = int(p3_step)
        self.kp3_range = range(-(int(kp3*p3_step)), int(kp3*p3_step) + 1, int(p3_step) or 1)  # set the range of columns
        self.kp2_range = range(-(int(kp2*p2_step)), int(kp2*p2_step) + 1, int(p2_step) or 1)  # to -k*step >=0<= k*step
        #self.kp1_range = range(-(int(kp1*p1_step)), int(kp1*p1_step) + 1, p1_step or 1)  # and p step
        self.kp1_range = range(-101, 102, 1)

        """pos_primes = list(sieve.primerange(0, kp2+1))
        neg_primes = [i * -1 for i in pos_primes]
        neg_primes.reverse()
        neg_primes.append(-1)
        neg_primes.append(0)
        neg_primes.append(1) 
        self.kp2_range = neg_primes + pos_primes"""

    def __call__(self, min_size=3):
        """Return the 1st prime sequence with elements >= min_size,
        the first composite for y positive (index 0) and y negative(index -2) and the X obj (index -1)"""
        big_seq = list()

        for k1 in self.kp1_range:
            for k2 in self.kp2_range:
                #if not isprime(k2): continuesieve.primerange(0,100)
                for k3 in self.kp3_range:
                    primes_seq = list()
                    p1, p2, p3 = (self.p1 + k1, self.p2 + k2, self.p3 + k3)
                    if p1 == p2 and p2 == p3: continue;  # Prevent infinite loop checking if p1, p2 and p3 are the same
                    a = (p1 - (2 * (p2)) + p3) / 2.
                    b = (p3 - p1) / 2.
                    c = p2
                    possible_prime = p1p2p3(a, b, c, 0)
                    if isprime(possible_prime): primes_seq.append(possible_prime)
                    else: continue
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
                    primes_seq.append(P1P2P3(p1,p2,p3,0))  # Append the X object to return the sequence info

                    if len(primes_seq)-3 >= min_size:
                        big_seq.append(primes_seq)

        return big_seq
