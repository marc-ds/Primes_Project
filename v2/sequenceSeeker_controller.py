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
                if p1 == p2 and p2 == p3:
                    continue  # Prevent infinite loop checking if p1, p2 and p3 are the same.
                a = (p1 - (2 * p2) + p3) / 2.
                b = (p3 - p1) / 2.
                c = p2
                possible_prime = x_abc(a, b, c, 0)
                if isprime(possible_prime):
                    primes_seq.append(possible_prime)
                else:
                    continue
                yp = 1
                yn = -1
                y_step = 1

                possible_prime = x_abc(a, b, c, yp)
                while isprime(possible_prime):
                    primes_seq.append(possible_prime)
                    yp += y_step
                    possible_prime = x_abc(a, b, c, yp)

                primes_seq.append(possible_prime)  # Append the first composite after the prime sequence.
                primes_seq.reverse()  # Make the composite first element and sort the list in Pn sequence.

                possible_prime = x_abc(a, b, c, yn)
                while isprime(possible_prime):
                    primes_seq.append(possible_prime)
                    yn -= y_step
                    possible_prime = x_abc(a, b, c, yn)

                primes_seq.append(possible_prime)
                primes_seq.append(XPn(p1, p2, p3, 0))  # Append the X object to return the sequence info.

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
        self.kp3_range = range(-(int(kp3 * p3_step)), int(kp3 * p3_step) + 1,  # Set the range of columns to
                               int(p3_step) or 1)                              # -k * step >= 0 <= k * step
        self.kp2_range = range(-(int(kp2 * p2_step)), int(kp2 * p2_step) + 1,  # using p*_step as step.
                               int(p2_step) or 1)
        self.kp1_range = range(-(int(kp1 * p1_step)), int(kp1 * p1_step) + 1, p1_step or 1)

    def __call__(self, min_size=3):
        """Return the 1st prime sequence with elements >= min_size,
        the first composite for y positive (index 0) and y negative(index -2) and the X obj (index -1)"""
        big_seq = list()

        for k1 in self.kp1_range:
            for k2 in self.kp2_range:
                for k3 in self.kp3_range:
                    primes_seq = list()
                    p1, p2, p3 = (self.p1 + k1, self.p2 + k2, self.p3 + k3)
                    if p1 == p2 and p2 == p3: continue;  # Prevent infinite loop checking if p1, p2 and p3 are the same.
                    a = (p1 - (2 * p2) + p3) / 2.
                    b = (p3 - p1) / 2.
                    c = p2
                    possible_prime = x_abc(a, b, c, 0)
                    if isprime(possible_prime):
                        primes_seq.append(possible_prime)
                    else:
                        continue
                    yp = 1
                    yn = -1
                    y_step = 1

                    possible_prime = x_abc(a, b, c, yp)
                    while isprime(possible_prime):
                        primes_seq.append(possible_prime)
                        yp += y_step
                        possible_prime = x_abc(a, b, c, yp)

                    primes_seq.append(possible_prime)  # Append the first composite after the prime sequence.
                    primes_seq.reverse()  # Make the composite first element and sort the list in Pn sequence.

                    possible_prime = x_abc(a, b, c, yn)
                    while isprime(possible_prime):
                        primes_seq.append(possible_prime)
                        yn -= y_step
                        possible_prime = x_abc(a, b, c, yn)

                    primes_seq.append(possible_prime)
                    primes_seq.append(XPn(p1, p2, p3, 0))  # Append the X object to return the sequence info.

                    if len(primes_seq) - 3 >= min_size:
                        big_seq.append(primes_seq)

        return big_seq


class SequenceSeekerV3:

    def __init__(self, p1, p2_k, p3_k):
        """The user set P1 and columns range (k) for P2 (p2_k) and P3 (p3_k)
        The initial value for P2 and P3 are P1"""
        self.p1 = p1
        self.p2_range = list(rpup_positive(abs(p1), p2_k))  # P2 range: P1 <= P2 <= P2 + p2_k (P2 columns range)
        self.p3_k = p3_k

    def __call__(self, min_size):
        """ Return an list with all sequences, each one with an x object,
        first positive and first negative composites and the 1st prime sequence in range
        P1 >= P2+p2_k >= P3+p3_k, where p2_k and p3_k are the P2 and p3 columns range"""
        big_seq = list()  # This list will archive all valid 1st sequences.
        flag = 0  # Flag to count how much interactions the program do to find that sequence.

        for p2_i in self.p2_range:  # Start the first loop for p2, starting by P1 value.
            p3_range = rpup_positive(int(p2_i), self.p3_k)

            for p3_i in p3_range:  # Start p3 loop out of actual p2 value, so:
                primes_seq = list()                         # P2 <= P3 <= P3+k
                flag += 1
                p1 = self.p1
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
                if isprime(possible_prime):  # Append the value when in y=0 if is prime, if not, continue to next.
                    primes_seq.append(possible_prime)
                else:
                    continue

                yp = 1      # Set the first value to positives y checks and
                yn = -1     # the first negative value to negative y check
                y_step = 1  # and the steps that positives and negative loops.

                possible_prime = x(p1, p2, p3, yp)
                while isprime(possible_prime):          # While possible prime is true, keep appending
                    primes_seq.append(possible_prime)   # positives y possible_prime to prime sequence.
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

                if len(primes_seq) - 2 >= min_size:   # Check the actual sequence length excluding both
                    primes_seq.append(flag)           # composites and the object x with minimum sequence size.
                    primes_seq.append(X(p1, p2, p3))  # Append the x object to return the sequence info.
                    big_seq.append(primes_seq)

        return big_seq


class SequenceSeekerV4:

    def __init__(self, p1, p1_k, p2_k, p3_k):
        """The user set P1 and columns range (k) for P2 (p2_k) and P3 (p3_k)
        The initial value for P2 and P3 are P1"""
        self.p1 = p1
        self.p1_range = list(rpup_positive(abs(p1), p1_k))  # P1 range: P1 <= P1 + p2_k (P1 columns range)
        self.p2_k = p2_k                                    # P2 range: P1 <= P2 <= P2 + p2_k (P2 columns range)
        self.p3_k = p3_k                                    # P3 range: P2 <= P3 <= P3 + p2_k (P3 columns range)

    def __call__(self, min_size):
        """ Return an list with all sequences, each one with an x object,
        first positive and first negative composites and the 1st prime sequence in range
        P1 >= P2+p2_k >= P3+p3_k, where p2_k and p3_k are the P2 and p3 columns range"""
        big_seq = list()  # This list will archive all valid 1st sequences.
        flag = 0  # Flag to count how much interactions the program do to find that sequence.

        for p1_i in self.p1_range:
            p2_range = rpup_positive(int(p1_i), self.p2_k)
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
                    if isprime(possible_prime):  # Append the value when in y=0 if is prime, if not, continue to next.
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


class SequenceSeekerV4a:

    def __init__(self, a, b, c, y_init, y_end, p2_k, p3_k):
        """The user set P1 and columns range (k) for P2 (p2_k) and P3 (p3_k)
        The initial value for P2 and P3 are P1"""

        self.p1_range = list(range_ay2byc(a,b,c,y_init,y_end))  # P1 range: P1 <= P1 + p2_k (P1 columns range)
        self.p2_k = p2_k                                  # P2 range: P1 <= P2 <= P2 + p2_k (P2 columns range)
        self.p3_k = p3_k                                  # P3 range: P2 <= P3 <= P3 + p2_k (P3 columns range)

    def __call__(self, min_size):
        """ Return an list with all sequences, each one with an x object,
        first positive and first negative composites and the 1st prime sequence in range
        P1 >= P2+p2_k >= P3+p3_k, where p2_k and p3_k are the P2 and p3 columns range"""
        big_seq = list()  # This list will archive all valid 1st sequences.
        flag = 0  # Flag to count how much interactions the program do to find that sequence.

        for p1_i in self.p1_range:
            p2_range = rpup_positive(int(p1_i), self.p2_k)
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

        self.p1_range = list(rpdown_positive(p1, kp1))
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
