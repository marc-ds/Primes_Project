#!/usr/bin/python3
import cgi
import cgitb
from math import sqrt
from sequenceSeeker_controller import *
from sympy import factorint
cgitb.enable()
form = cgi.FieldStorage()

print('Content-type: text/html\r\n\r')
print('<html>')
print('<head>')
print('<link rel="stylesheet" type="text/css" href="/styles/sequence_seeker.css">')
print('<title>Sequence Seeker</title>')
print('</head>')
print('<body>')




if "p1" not in form or "p2" not in form or "p3" not in form:

    print('<form action="/v2/sequenceSeeker_view.py" method="post" id="sequence_seeker">')
    print('<div id="p_value">P1 initial value = <input type="text" name="p1" value="" />')
    print('P2 initial value &nbsp;= <input type="text" name="p2" value="" />')
    print('P3 initial value = <input type="text" name="p3" value="" /></div>')
    print('<div id="p_step">P1 step value &nbsp;&nbsp;&nbsp;= <input type="text" name="p1_step" value="0" />')
    print('P2 step value &nbsp;&nbsp;&nbsp;= <input type="text" name="p2_step" value="0" />')
    print('P3 step value &nbsp;&nbsp;&nbsp;= <input type="text" name="p3_step" value="1" /></div>')
    print('<div class="others" id="k">Columns range = <input type="text" name="k" value="100" />')
    print('Minimum size of first sequences = <input type="text" name="min_size" value="7" id="min_value"/>')
    print('<input type="submit" value="Generate" id="submit"/></div></form>')
    print('<h1 id="sequence_seeker">Please fill the fields</h1>')
    print('</body>')
    print('</html>')

else:

    p1 = float(form["p1"].value)
    p2 = float(form["p2"].value)
    p3 = float(form["p3"].value)
    p1_step = float(form["p1_step"].value)
    p2_step = float(form["p2_step"].value)
    p3_step = float(form["p3_step"].value)
    k = int(form["k"].value)
    min_size = int(form["min_size"].value)

    print('<form action="/v2/sequenceSeeker_view.py" method="post" id="sequence_seeker">')
    print('<div id="p_value">P1 initial value = <input type="text" name="p1" value="{:g}" />'.format(p1))
    print('P2 initial value &nbsp;= <input type="text" name="p2" value="{:g}" />'.format(p2))
    print('P3 initial value = <input type="text" name="p3" value="{:g}" /></div>'.format(p3))
    print('<div id="p_step">P1 step value &nbsp;&nbsp;&nbsp;= <input type="text" name="p1_step" value="{:g}" />'.format(p1_step))
    print('P2 step value &nbsp;&nbsp;&nbsp;= <input type="text" name="p2_step" value="{:g}" />'.format(p2_step))
    print('P3 step value &nbsp;&nbsp;&nbsp;= <input type="text" name="p3_step" value="{:g}" /></div>'.format(p3_step))
    print('<div class="others" id="k">Columns range = <input type="text" name="k" value="{}" />'.format(k))
    print('Minimum size of first sequences = <input type="text" name="min_size" value="{}" id="min_value"/>'.format(min_size))
    print('<input type="submit" value="Generate" id="submit"/></div></form>')


    calc = SequenceSeeker(p1,p2,p3,p1_step,p2_step,p3_step,k)
    yv_seq, off_seq, abc_seq, big_seq = calc(min_size)
    yv0_seq, off0_seq, abc0_seq, big0_seq = calc.when_f0(min_size)
    print('<h1 id=sequence_seeker >{} sequences found.</h1>'.format(len(big_seq)))
    print('<table id=sequence_seeker>')

    for i in range(0, len(big_seq)):
        first = factorint(int(big_seq[i].pop(0)))
        last = factorint(int(big_seq[i].pop()))
        abc = abc_seq[i]
        a = int(abc[0])
        b = int(abc[1])
        c = int(abc[2])
        delta = int(b ** 2 - 4 * a * c)
        sqrtdelta = sqrt(abs(delta))
        c_g = sqrtdelta - int(sqrtdelta)

        delta_txt = '<td class="delta" id="{}" >&Delta;={:d}</th>'
        c_g_txt = '<td class="c_g" id="{}" >CG={:.4g}</th>'
        yv_txt = '<td class="y_vertex" id="{}" >yv={:1.4g}</td>'

        print('<tr class="sequence_seeker_header">')
        print('<td class="formula" id="x" >x={}y&circ;2{:+}y{:+}</th>'.format(a,b,c))

        yv = yv_seq[i]
        if yv < 0:
            print(yv_txt.format('negative', yv))
        elif yv > 0:
            print(yv_txt.format('positive', yv))
        elif yv == 0:
            print(yv_txt.format('zero', yv))
        else:
            print(yv_txt.format('vertex', yv))

        off_txt = '<td class="offset" id="{}" >f={:1.4g}</th>'
        f = off_seq[i]
        if f < 0:
            print(off_txt.format('negative', f))
        elif f > 0:
            print(off_txt.format('positive', f))
        elif f == 0:
            print(off_txt.format('zero', f))
        else:
            print(off_txt.format('no', f))

        if delta < 0:
            print(delta_txt.format('negative', delta))
        elif delta > 0:
            print(delta_txt.format('positive', delta))
        elif delta == 0:
            print(delta_txt.format('zero', delta))
        else:
            print(delta_txt.format('no', delta))

        if c_g < 0:
            print(c_g_txt.format('negative', c_g))
        elif c_g > 0:
            print(c_g_txt.format('positive', c_g))
        elif c_g == 0:
            print(c_g_txt.format('zero', c_g))
        else:
            print(c_g_txt.format('no', c_g))

        length = len(big_seq[i]) - big_seq[i].count(1) - big_seq[i].count(-1)
        print('<td class="qtd_primes" id="qtd_primes" >#P1st Seq={}'.format(length))

        for result in first.items():
            if abs(result[0]) is 1:
                print('<td class="first" id="one">', end='')
                print(*result, sep='*', end='')
                print('</td>')
            elif result[0] == 0:
                print('<td class="first" id="zero">', end='')
                print(*result, sep='*', end='')
                print('</td>')
            elif isprime(result[0]):
                print('<td class="first" id="prime">', end='')
                print(*result, sep='*', end='')
                print('</td>')
            elif not (sqrt(abs(result[0])) * 10) % 2:
                print('<td class="first" id="sqrt_round">', end='')
                print(*result, sep='*', end='')
                print('</td>')
            else:
                print('<td class="first" id="composite">', end='')
                print(*result, sep='*', end='')
                print('</td>')

        for result in big_seq[i]:
            if abs(result) is 1:
                print('<td class="data" id="one">{}</td>'.format(result))
            elif result == 0:
                print('<td class="data" id="zero">{}</td>'.format(result))
            elif isprime(result):
                print('<td class="data" id="prime">{}</td>'.format(result))
            elif not (sqrt(abs(result)) * 10) % 2:
                print('<td class="data" id="sqrt_round">{}</td>'.format(result))
            else:
                print('<td class="data" id="composite">{}</td>'.format(result))

        for result in last.items():
            if abs(result[0]) is 1:
                print('<td class="last" id="one">', end='')
                print(*result, sep='*', end='')
                print('</td>')
            elif result[0] == 0:
                print('<td class="last" id="zero">', end='')
                print(*result, sep='*', end='')
                print('</td>')
            elif isprime(result[0]):
                print('<td class="last" id="prime">', end='')
                print(*result, sep='*', end='')
                print('</td>')
            elif not (sqrt(abs(result[0])) * 10) % 2:
                print('<td class="last" id="sqrt_round">', end='')
                print(*result, sep='*', end='')
                print('</td>')
            else:
                print('<td class="last" id="composite">', end='')
                print(*result, sep='*', end='')
                print('</td>')

        print('</tr>')

print('</body>')
print('</html>')