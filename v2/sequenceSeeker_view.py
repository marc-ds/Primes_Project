#!/usr/bin/python3

import cgi
import cgitb
from math import sqrt
from main_controller import *
cgitb.enable()
form = cgi.FieldStorage()



if "p1" not in form or "p2" not in form or "p3" not in form:

    print('Content-type: text/html\r\n\r')
    print('<html>')
    print('<head>')
    print('<link rel="stylesheet" type="text/css" href="/styles/style.css">')
    print('<title>Sequences table</title>')
    print('</head>')
    print('<body>')
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

    print('Content-type: text/html\r\n\r')
    print('<html>')
    print('<head>')
    print('<link rel="stylesheet" type="text/css" href="/styles/style.css">')
    print('<title>Sequences table</title>')
    print('</head>')
    print('<body>')
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


    calc = SequenceSeeker(p1, p2, p3, p1_step, p2_step, p3_step, k)
    yv_seq, off_seq, abc_seq, big_seq = calc(min_size)
    yv0_seq, off0_seq, abc0_seq, big0_seq = calc.when_f0(min_size)
    print('<h1 id=sequence_seeker >{} sequences found.</h1>'.format(len(big_seq)))
    print('<table id=sequence_seeker>')

    for i in range(0, len(big_seq)):
        first = int(big_seq[i].pop(0))
        last = int(big_seq[i].pop())
        print('<tr class="sequence_seeker_header">')
        yv_txt = '<td class="sequence_seeker" id="{}" >y_vertex: {:1.4g}</td>'
        yv = yv_seq[i]
        if yv < 0:
            print(yv_txt.format('y_vertex_negative', yv))
        elif yv > 0:
            print(yv_txt.format('y_vertex_positive', yv))
        elif yv == 0:
            print(yv_txt.format('y_vertex_zero', yv))
        else:
            print(yv_txt.format('no_y_vertex', yv))
        off_txt = '<td class="sequence_seeker" id="{}" >offset: {:1.4g}</th>'
        f = off_seq[i]
        if f < 0:
            print(off_txt.format('offset_negative', f))
        elif f > 0:
            print(off_txt.format('offset_positive', f))
        elif f == 0:
            print(off_txt.format('offset_zero', f))
        else:
            print(off_txt.format('no_offset', f))
        abc = abc_seq[i]
        a = abc[0]
        b = abc[1]
        c = abc[2]
        delta = int(b ** 2 - 4 * a * c)
        sqrtdelta = sqrt(abs(delta))
        c_g = sqrtdelta - int(sqrtdelta)

        if abs(delta) is 1:
            print('<td class="sequences_table" id="delta_one">&Delta; {:.4g}</td>'.format(delta))
        elif delta == 0:
            print('<td class="sequences_table" id="delta_zero">&Delta; {:.4g}</td>'.format(delta))
        elif isprime(delta):
            print('<td class="sequences_table" id="delta_prime">&Delta; {:.4g}</td>'.format(delta))
        elif not (sqrt(abs(delta)) * 10) % 2:
            print('<td class="sequences_table" id="delta_sqrt">&Delta; {:.4g}</td>'.format(delta))
        else:
            print('<td class="sequences_table" id="delta_composite">&Delta; {:.4g}</td>'.format(delta))
        if abs(delta) is 1:
            print('<td class="sequences_table" id="c_g_one">C.G. {:.4g}</td>'.format(c_g))
        elif delta == 0:
            print('<td class="sequences_table" id="c_g_zero">C.G. {:.4g}</td>'.format(c_g))
        elif isprime(delta):
            print('<td class="sequences_table" id="c_g_prime">C.G. {:.4g}</td>'.format(c_g))
        elif not (sqrt(abs(delta)) * 10) % 2:
            print('<td class="sequences_table" id="c_g_sqrt_round">C.G. {:.4g}</td>'.format(c_g))
        else:
            print('<td class="sequences_table" id="c_g_composite">C.G. {:.4g}</td>'.format(c_g))

        print('<td class="sequence_seeker" id="a" >a: {:g}</th>'.format(a))
        print('<td class="sequence_seeker" id="b" >b: {:g}</th>'.format(b))
        print('<td class="sequence_seeker" id="c" >c: {:g}</th>'.format(c))
        length = len(big_seq[i]) - big_seq[i].count(1) - big_seq[i].count(-1)
        print('<td class="sequence_seeker" id="qtd_primes" >#P 1st Seq: {}.'.format(length))
        for result in big_seq[i]:
            if abs(result) is 1:
                print('<td class="sequences_table" id="one">{}</td>'.format(result))
            elif result == 0:
                print('<td class="sequences_table" id="zero">{}</td>'.format(result))
            elif isprime(result):
                print('<td class="sequences_table" id="prime">{}</td>'.format(result))
            elif not (sqrt(abs(result)) * 10) % 2:
                print('<td class="sequences_table" id="sqrt_round">{}</td>'.format(result))
            else:
                print('<td class="sequences_table" id="composite">{}</td>'.format(result))
        print('</tr>')

    for i in range(0, len(big0_seq)):
        first = int(big0_seq[i].pop(0))
        last = int(big0_seq[i].pop())
        print('<tr class="sequence_seeker_header">')
        yv_txt = '<td class="sequence_seeker" id="{}" >y_vertex&ordm: {:1.4g}</td>'
        yv = yv0_seq[i]
        if yv < 0:
            print(yv_txt.format('y_vertex_negative', yv))
        elif yv > 0:
            print(yv_txt.format('y_vertex_positive', yv))
        elif yv == 0:
            print(yv_txt.format('y_vertex_zero', yv))
        else:
            print(yv_txt.format('no_y_vertex', yv))
        off_txt = '<td class="sequence_seeker" id="{}" >offset&ordm: {:1.4g}</th>'
        f = off0_seq[i]
        if f < 0:
            print(off_txt.format('offset_negative', f))
        elif f > 0:
            print(off_txt.format('offset_positive', f))
        elif f == 0:
            print(off_txt.format('offset_zero', f))
        else:
            print(off_txt.format('no_offset', f))
        abc = abc0_seq[i]
        a = abc[0]
        b = abc[1]
        c = abc[2]
        delta = int(b**2-4*a*c)
        sqrtdelta = sqrt(abs(delta))
        c_g = sqrtdelta - int(sqrtdelta)

        if abs(delta) is 1:
            print('<td class="sequences_table" id="one">&Delta;&ordm {:.4g}</td>'.format(delta))
        elif delta == 0:
            print('<td class="sequences_table" id="zero">&Delta;&ordm {:.4g}</td>'.format(delta))
        elif isprime(delta):
            print('<td class="sequences_table" id="prime">&Delta;&ordm {:.4g}</td>'.format(delta))
        elif not (sqrt(abs(delta)) * 10) % 2:
            print('<td class="sequences_table" id="sqrt_round">&Delta;&ordm {:.4g}</td>'.format(delta))
        else:
            print('<td class="sequences_table" id="composite">&Delta;&ordm {:.4g}</td>'.format(delta))
        if abs(delta) is 1:
            print('<td class="sequences_table" id="one">C.G. {:.4g}</td>'.format(c_g))
        elif delta == 0:
            print('<td class="sequences_table" id="zero">C.G. {:.4g}</td>'.format(c_g))
        elif isprime(delta):
            print('<td class="sequences_table" id="prime">C.G. {:.4g}</td>'.format(c_g))
        elif not (sqrt(abs(delta)) * 10) % 2:
            print('<td class="sequences_table" id="sqrt_round">C.G. {:.4g}</td>'.format(c_g))
        else:
            print('<td class="sequences_table" id="composite">C.G. {:.4g}</td>'.format(c_g))

        print('<td class="sequence_seeker" id="a" >a&ordm: {:g}</th>'.format(a))
        print('<td class="sequence_seeker" id="b" >b&ordm: {:g}</th>'.format(b))
        print('<td class="sequence_seeker" id="c" >c&ordm: {:g}</th>'.format(c))
        length = len(big0_seq[i]) - big0_seq[i].count(1) - big0_seq[i].count(-1)
        print('<td class="sequence_seeker" id="qtd_primes" >#P 1st Seq: {}.'.format(length))
        for result in big0_seq[i]:
            if abs(result) is 1:
                print('<td class="sequences_table" id="one">{}</td>'.format(result))
            elif result == 0:
                print('<td class="sequences_table" id="zero">{}</td>'.format(result))
            elif isprime(result):
                print('<td class="sequences_table" id="prime">{}</td>'.format(result))
            elif not (sqrt(abs(result)) * 10) % 2:
                print('<td class="sequences_table" id="sqrt_round">{}</td>'.format(result))
            else:
                print('<td class="sequences_table" id="composite">{}</td>'.format(result))
        print('</tr>')

print('</body>')
print('</html>')