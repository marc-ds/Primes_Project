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
    print('P3 initial value &nbsp;= <input type="text" name="p3" value="" /></div>')
    print('<div id="p_step">P1 step value &nbsp;&nbsp;&nbsp;= <input type="text" name="p1_step" value="0" />')
    print('P2 step value &nbsp;&nbsp;&nbsp;= <input type="text" name="p2_step" value="0" />')
    print('P3 step value &nbsp;&nbsp;&nbsp;= <input type="text" name="p3_step" value="1" /></div>')
    print('<div class="others" id="k">Columns range = <input type="text" name="k" value="100" />')
    print('Min. #P 1st seq &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= '
          '<input type="text" name="min_size" value="7" id="min_value"/>')
    print('<input type="submit" value="Generate" id="submit"/></div></form>')
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
    print('Min. #P 1st seq &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= '
          '<input type="text" name="min_size" value="{}" id="min_value"/>'.format(min_size))
    print('<input type="submit" value="Generate" id="submit"/></div></form>')

    calc = SequenceSeeker(p1,p2,p3,p1_step,p2_step,p3_step,k)
    big_seq = sorted(calc(min_size), reverse=True, key=len)

    print('<h1 id=sequence_seeker >{} sequences with {} primes or more elements found.</h1>'.format(len(big_seq), min_size))
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

        yv0 = x_obj.y_vertex0
        f0 = x_obj.offset0
        a0 = x_obj.a0
        b0 = x_obj.b0
        c0 = x_obj.c0
        delta0 = x_obj.delta0
        sqrtdelta0 = sqrt(abs(delta0))
        c_g0 = sqrtdelta - int(sqrtdelta0)
        x01 = x_obj.x01
        x02 = x_obj.x02
        x03 = x_obj.x03
        par_type = x_obj.par_type
        length = len(big_seq[i]) - big_seq[i].count(1) - big_seq[i].count(-1)

        p1_txt = '<td id="{}">p1={:g}</td>'
        p2_txt = '<td id="{}">p2={:g}</td>'
        p3_txt = '<td id="{}">p3={:g}</td>'
        poly_txt = '<td class="poly">x={:g}y^2{:+g}y{:+g}</td>'
        yv_txt = '<td class="y_vertex" id="{}" >yv={:1.4g}</td>'
        off_txt = '<td class="offset" id="{}" >f={:1.4g}</th>'
        delta_txt = '<td class="delta" id="{}" >&Delta;={:.0f}</th>'
        c_g_txt = '<td class="c_g" id="{}" >CG={:.4g}</th>'

        poly_txt0 = '<td class="poly0">x&ordm;={:g}y^2{:+g}y{:+g}</td>'
        yv_txt0 = '<td class="y_vertex" id="{}" >y&ordm;v={:1.4g}</td>'
        off_txt0 = '<td class="offset" id="{}" >f&ordm;={}</th>'
        delta_txt0 = '<td class="delta" id="{}" >&Delta;&ordm;={:.0f}</th>'
        c_g_txt0 = '<td class="c_g" id="{}" >CG&ordm;={:.4g}</th>'
        x01_txt = '<td id="{}">x&ordm;1={:g}</td>'
        x02_txt = '<td id="{}">x&ordm;2={:g}</td>'
        x03_txt = '<td id="{}">x&ordm;3={:g}</td>'
        len_txt = '<td class="qtd_primes" id="qtd_primes" >#P={}'
        par_type_txt = '<td class="{pt}" >{pt}</td>'

        print('<tr class="sequence_seeker_header">')
        print(p1_txt.format(data_type(int(x_obj.p1)), x_obj.p1))
        print(p2_txt.format(data_type(int(x_obj.p2)), x_obj.p2))
        print(p3_txt.format(data_type(int(x_obj.p3)), x_obj.p3))
        print(poly_txt.format(a,b,c))
        print(yv_txt.format(x_obj.yv_type(), yv))
        print(off_txt.format(header_type(f), f))
        print(delta_txt.format(header_type(delta), delta))
        print(c_g_txt.format(header_type(delta), c_g))
        print(poly_txt0.format(a0, b0, c0))
        print(yv_txt0.format(header_type(yv0), yv0))
        print(off_txt0.format(header_type(f0), f0))
        print(delta_txt0.format(header_type(delta0), delta0))
        print(c_g_txt0.format(header_type(delta0), c_g0))
        print(x01_txt.format(data_type(int(x01)), x01))
        print(x02_txt.format(data_type(int(x02)),x02))
        print(x03_txt.format(data_type(int(x03)),x03))
        print(par_type_txt.format(pt=par_type))
        print(len_txt.format(length))


        for value, exponent in first.items():
            print('<td class="first" id="composite">{:}^{}</td>'.format(value, exponent), end='')


        for result in sequence:
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
            print('<td class="last" id="composite">{:}^{}</td>'.format(value, exponent), end='')

        print('</tr>')

print('</body>')
print('</html>')