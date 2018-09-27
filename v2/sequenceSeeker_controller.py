from main_controller import *

class SequenceSeeker():
    """seek first primes sequences of given P1, P2, P3, p_steps and columns range (col_range)"""
    def __init__(self, p1, p2, p3, p1_step=0, p2_step=0, p3_step=1, col_range=10):
        self.p1 = int(p1)
        self.p2 = int(p2)
        self.p3 = int(p3)
        self.p1_step = int(p1_step)
        self.p2_step = int(p2_step)
        self.p3_step = int(p3_step)
        self.k_range = range(-int(col_range), int(col_range)+1)

    def __call__(self, min_size=3):
        big_seq = list()
        abc_seq = list()
        yv_seq = list()
        offset_seq = list()

        """ define-se primeira sequencia de numeros primos como sendo aquela que possui pelo menos um numero primo 
        em y=0.5 (ou seja, tem que ter primo em y=0 e/ou y=1).
        Assim, nesse comando (for statment), para um range dado por range(-int(col_range), int(col_range)+1), 
        seleciona-se apenas as equaçoes que geram as primeiras sequencias de numeros primos com a quantidade minima 
         de elementos determinada por (min_size) """
        for k in self.k_range:
            first_primes_seq = list()
            p1, p2, p3 = self.p1 + (self.p1_step*k), self.p2 + (self.p2_step*k), self.p3 + (self.p3_step*k)
            a = (p1 - 2.0 * p2 + p3) / 2.0
            b = (p3 - p1) / 2.0
            c = p2
            ypos = 1
            yneg = 0
            """favor mudar em todos os programas p1p2p3 por x """
            """encontra os elementos primos da primeira sequencia em 0>=y>=(até onde encontrar elemento composto)"""
            possible_prime = p1p2p3(a, b, c, yneg)
            while isprime(possible_prime):
                if p1 == p2 and p2 == p3: break;
                first_primes_seq.append(possible_prime)
                yneg -= 1
                possible_prime = p1p2p3(a, b, c, yneg)
            """aqui vamos acrescentar o primeiro elemento composto que limita a sequencia de primos em y negativo"""
            first_primes_seq.append(possible_prime)

            """coloca a sequencia em ordem crescente de indice y"""
            first_primes_seq.reverse()

            """encontra os elementos primos da primeira sequencia em 1<=y<=(até onde encontrar elemento composto)"""
            possible_prime = p1p2p3(a, b, c, ypos)
            while isprime(possible_prime):
                if p1 == p2 and p2 == p3: break;
                first_primes_seq.append(possible_prime)
                ypos += 1
                possible_prime = p1p2p3(a, b, c, ypos)
            """aqui vamos acrescentar o primeiro elemento composto que limita a sequencia de primos em y positivo"""
            first_primes_seq.append(possible_prime)

            if (len(first_primes_seq)-2) >= min_size:
                big_seq.append(first_primes_seq)
                abc_seq.append([a, b, c])
                offset_seq.append(offset(a, b))
                yv_seq.append(y_vertex(a, b))
        return yv_seq, offset_seq, abc_seq, big_seq
