#!/usr/bin/python3
import cgi
import cgitb
from math import sqrt
from sequenceSeeker_controller import *
from sympy import factorint
from main_controller import header_type

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
    print('P3 step value &nbsp;&nbsp;= <input type="text" name="p3_step" value="{:g}" /></div>'.format(p3_step))
    print('<div class="others" id="k">Columns range = <input type="text" name="k" value="{}" />'.format(k))
    print('#P 1st seq &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= <input type="text" name="min_size" value="{}" id="min_value"/>'.format(min_size))
    print('<input type="submit" value="Generate" id="submit"/></div></form>')


    calc = SequenceSeeker(p1,p2,p3,p1_step,p2_step,p3_step,k)
    big_seq = sorted(calc(min_size), reverse=True, key=len)
    print('<h1 id=sequence_seeker >{} sequences found.</h1>'.format(len(big_seq)))

    print('<table id=sequence_seeker>')

    for i in range(0, len(big_seq)):
        sequence = big_seq[i]
        x_obj = sequence.pop()
        first = factorint(int(sequence.pop(0)))
        last = factorint(int(sequence.pop()))

        yv = x_obj.y_vertex
        f = x_obj.offset
        a = x_obj.a
        b = x_obj.b
        c = x_obj.c
        delta = x_obj.delta
        sqrtdelta = sqrt(abs(delta))
        c_g = sqrtdelta - int(sqrtdelta)
        length = len(big_seq[i]) - big_seq[i].count(1) - big_seq[i].count(-1)
        par_type = x_obj.par_type

        yv0 = x_obj.y_vertex0
        f0 = x_obj.offset0
        a0 = x_obj.a0
        b0 = x_obj.b0
        c0 = x_obj.c0
        delta0 = x_obj.delta0
        sqrtdelta0 = sqrt(abs(delta0))
        c_g0 = sqrtdelta - int(sqrtdelta0)

        poly_txt = '<td class="poly">x={:g}y^2{:+g}y{:+g}</td>'
        yv_txt = '<td class="y_vertex" id="{}" >y_vertex&nbsp;&nbsp;{:1.4g}</td>'
        off_txt = '<td class="offset" id="{}" >offset&nbsp;&nbsp;{:1.4g}</th>'
        delta_txt = '<td class="delta" id="{}" >&Delta;&nbsp;&nbsp;{:d}</th>'
        c_g_txt = '<td class="c_g" id="{}" >CG&nbsp;&nbsp;{:.4g}</th>'
        len_txt = '<td class="qtd_primes" id="qtd_primes" >#P 1st Seq: {}'
        par_type_txt = '<td class="par_type" >Type={}</td>'

        poly_txt0 = '<td class="poly0">x&ordm;={:g}y^2{:+g}y{:+g}</td>'
        yv_txt0 = '<td class="y_vertex" id="{}" >y_vertex&ordm;&nbsp;{:1.4g}</td>'
        off_txt0 = '<td class="offset" id="{}" >offset&ordm;&nbsp;{:1.4g}</th>'
        delta_txt0 = '<td class="delta" id="{}" >&Delta;&ordm;&nbsp;{:d}</th>'
        c_g_txt0 = '<td class="c_g" id="{}" >CG&ordm;&nbsp;{:.4g}</th>'

        print('<tr class="sequence_seeker_header">')
        print(poly_txt.format(a,b,c))
        print(yv_txt.format(x_obj.yv_type(), yv))
        print(off_txt.format(header_type(f), f))
        print(delta_txt.format(header_type(delta), delta))
        print(c_g_txt.format(header_type(delta), c_g))
        print(len_txt.format(length))


        for value, exponent in first.items():
            print('<td class="first" id="composite">{:}&circ;{}</td>'.format(value, exponent), end='')


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

        for value, exponent in last.items():
            print('<td class="first" id="composite">{:}&circ;{}</td>'.format(value, exponent), end='')

        print('</tr>')

        print('<tr class="sequence_seeker_header">')
        print(poly_txt0.format(a0,b0,c0))
        print(yv_txt0.format(header_type(yv0), yv0))
        print(off_txt0.format(header_type(f0), f0))
        print(delta_txt0.format(header_type(delta0), delta0))
        print(c_g_txt0.format(header_type(c_g0), c_g0))
        print(par_type_txt.format(par_type))
        print('</tr>')

print('</body>')
print('</html>')