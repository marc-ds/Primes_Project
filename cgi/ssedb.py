from ssedb_lib import X, isprime, nextprime, rpup_positive, x, rpdown_positive
import sqlite3

con = sqlite3.connect("database.db")
c = con.cursor()

density_range = 1

engine = input('Sequence Seeker Engine v5 or v6 (default: v5) = ') or 'v5'
p1_initial = int(input('P1 value (default: 1) = ') or 1)
rangep1 = int(input('P1 range (default: 10) = ') or 10)
rangep2 = int(input('P2 range (default: 10) = ') or 10)
rangep3 = int(input('P3 range (default: 10) = ') or 10)
min_size = int(input('Number of sequence minimum primes (default: 10) = ') or 10)

p1_range = rpup_positive(p1_initial, rangep1)

for p1 in p1_range:

    if engine == 'v5':
        p2_range = rpup_positive(int(p1), rangep2)
        print('---Using V5------------V5')
    elif engine == 'v6':
        p2_range = rpdown_positive(int(p1), rangep2)
        print('---Using V6------------V6')

    for p2 in p2_range:
        p3_range = rpup_positive(int(p2), rangep3)
        if engine == 'v6':
            p3_range = rpup_positive(int(p2), rangep3)
            print('---Using V6------------V6')
        elif engine == 'v5':
            p3_range = rpdown_positive(int(p2), rangep3)
            print('---Using V5------------V5')

        for p3 in p3_range:

            obj_x = X(p1, p2, p3)

            a0 = int(obj_x.a0)
            b0 = int(obj_x.b0)
            c0 = int(obj_x.c0)
            sequence_size = 0

            if p1 == p2 and p2 == p3:
                continue

            formula = '{:d}y^2{:+d}y{:+d}'.format(a0, b0, c0)

            c.execute('SELECT * FROM xzero WHERE formula = ?', (formula,))
            reg = c.fetchone()
            try:
                if type(reg[0]) is int:
                    print('--Já salvo: {}, P1={}, P2={}, P3={}--'.format(formula, obj_x.p1, obj_x.p2, obj_x.p3))
                    continue
            except:
                print('Nova formula: {}, P1={}, P2={}, P3={}'.format(formula, obj_x.p1, obj_x.p2, obj_x.p3))

            possible_prime = x(p1, p2, p3, 0)
            if isprime(possible_prime):
                sequence_size += 1
            else:
                continue

            yp = 1
            yn = -1
            density = float(0)

            if obj_x.par_type is 'ACC':

                possible_prime = x(p1, p2, p3, yp)

                while isprime(possible_prime):
                    sequence_size += 1
                    yp += 1
                    possible_prime = x(p1, p2, p3, yp)

                possible_prime = x(p1, p2, p3, yn)

                while isprime(possible_prime):
                    sequence_size += 1
                    yn -= 1
                    possible_prime = x(p1, p2, p3, yn)

                if sequence_size <= min_size:
                    print('DESCARTADO --- {} - Tam. seq. {}'.format(formula, sequence_size))
                    continue

                #density_pos = obj_x.density_pos(density_range)
                #density_neg = obj_x.density_neg(density_range)
                #density = (density_neg + density_pos) / (density_range * 2)

            elif obj_x.par_type is 'DES':

                possible_prime = x(p1, p2, p3, yp)
                while isprime(possible_prime):
                    sequence_size += 1
                    yp += 1
                    possible_prime = x(p1, p2, p3, yp)

                sequence_size = sequence_size * 2

                if sequence_size <= min_size:
                    print('DESCARTADO - DES --- {} - Tam. seq. {}'.format(formula, sequence_size))
                    continue

                #density_pos = obj_x.density_pos(density_range)
                #density = density_pos / density_range

            elif obj_x.par_type is 'SUB':

                possible_prime = x(p1, p2, p3, yp)
                while isprime(possible_prime):
                    sequence_size += 1
                    yp += 1
                    possible_prime = x(p1, p2, p3, yp)

                sequence_size = (sequence_size * 2) - 1

                if sequence_size <= min_size:
                    print('DESCARTADO - SUB --- {} - Tam. seq. {}'.format(formula, sequence_size))
                    continue

                #density_pos = obj_x.density_pos(density_range)
                #density = density_pos / density_range

            try:
                c.execute('INSERT INTO xzero (formula, sequence_size, density) VALUES (?,?,?)',
                          (formula, sequence_size, density))
                con.commit()

                print('SALVO --- {}'.format(formula))

            except:
                print('Erro ao salvar a formula, tamanho da sequencia ou densidade')

con.close()
