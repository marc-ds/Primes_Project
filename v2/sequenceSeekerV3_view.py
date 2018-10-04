#!/usr/bin/python3
import cgi
import cgitb
from sequenceSeeker_controller import *
from sympy import factorint
from main_controller import header_ctype

cgitb.enable()
form = cgi.FieldStorage()

print('Content-type: text/html\r\n\r')

if "p1" not in form:

    print('<html>')
    print('<head>')
    print('<link rel="stylesheet" type="text/css" href="/styles/sequence_seekerV2.css">')
    print('<script src="js.js"></script>')
    print('<title>Sequence Seeker</title>')
    print('</head>')
    print('<body>')
    print('<form action="javascript:sendformv3()" method="post" id="sequence_seeker" name="collect_data_form" >')
    print('<div id="p_value">P1 initial value &nbsp;= <input type="text" name="p1" value="1" />')
    print('Col. range p2 = <input type="text" name="kp2" value="1000" />')
    print('Col. range p3 = <input type="text" name="kp3" value="1000" /></div>')
    print('<div class="others" id="k">Min. #P 1st seq = '
          '<input type="text" name="min_size" value="20" id="min_value"/>')
    print('<input type="submit" value="Generate" id="submit"/></div></form>')
    print('<span id="loader">Loading...</span>')

    print('<table id="sequence_seeker" class="table_sequence_seeker" >')
else:

    p1 = float(form["p1"].value)
    kp2 = int(form["kp2"].value)
    kp3 = int(form["kp3"].value)
    min_size = int(form["min_size"].value)

    print('<form action="javascript:sendformv3()" method="post" id="sequence_seeker">')
    print('<div id="p_value">P1 initial value&nbsp; = <input type="text" name="p1" value="{:g}" />'.format(p1))
    print('P1 Col. range  = <input type="text" name="kp2" value="{}" />'.format(kp2))
    print('P2 Col. range  = <input type="text" name="kp3" value="{}" /></div>'.format(kp3))
    print('<div class="others" id="k">Min. #P 1st seq = '
          '<input type="text" name="min_size" value="{}" id="min_value"/>'.format(min_size))
    print('<input type="submit" value="Generate" id="submit"/></div></form>')
    print('<span id="loader">Loading...</span>')

    calc = SequenceSeekerV3(p1, kp2, kp3)

    big_seq = sorted(calc(min_size), key=get_obj)
    big_seq.sort(reverse=True, key=len)

    print('<table id="sequence_seeker" class="table_sequence_seeker" >')

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
        c_g = x_obj.c_g
        yv0 = x_obj.y_vertex0
        f0 = x_obj.offset0
        a0 = x_obj.a0
        b0 = x_obj.b0
        c0 = x_obj.c0
        delta0 = x_obj.delta0
        c_g0 = x_obj.c_g0
        x01 = x_obj.x01
        x02 = x_obj.x02
        x03 = x_obj.x03
        par_type = x_obj.par_type
        len_all = len(big_seq[i])
        len_primes = len(big_seq[i]) - big_seq[i].count(1) - big_seq[i].count(-1)

        p1_txt = '<td class="{}">P1={:g}</td>'
        p2_txt = '<td class="{}">P2={:g}</td>'
        p3_txt = '<td class="{}">P3={:g}</td>'
        poly_txt = '<td class="poly">x={:g}y^2{:+g}y{:+g}</td>'
        yv_txt = '<td class="{} y_vertex">yv={:1.4g}</td>'
        off_txt = '<td class="{} offset">f={:1.4g}</th>'
        delta_txt = '<td class="delta {}">&Delta;={:.0f}</th>'
        c_g_txt = '<td class="c_g {}" >CG={:.4g}</th>'

        poly_txt0 = '<td class="poly0">x&ordm;={:g}y^2{:+g}y{:+g}</td>'
        yv_txt0 = '<td class="y_vertex {}">y&ordm;v={:1.4g}</td>'
        off_txt0 = '<td class="offset {}">f&ordm;={}</th>'
        delta_txt0 = '<td class="delta {}">&Delta;&ordm;={:.0f}</th>'
        c_g_txt0 = '<td class="c_g {}">CG&ordm;={:.4g}</th>'
        x01_txt = '<td class="{}">x&ordm;1={:g}</td>'
        x02_txt = '<td class="{}">x&ordm;2={:g}</td>'
        x03_txt = '<td class="{}">x&ordm;3={:g}</td>'
        q_elements_txt = '<td class="qtd_elements">#E={}'
        q_prime_txt = '<td class="qtd_primes">#P={}'
        par_type_txt = '<td class="{pt}">{pt}</td>'

        print('<tr class="sequence_seeker_header">')
        print('<td class="line">{}</td>'.format(i + 1))
        print(p1_txt.format(data_ctype(int(x_obj.p1)), x_obj.p1))
        print(p2_txt.format(data_ctype(int(x_obj.p2)), x_obj.p2))
        print(p3_txt.format(data_ctype(int(x_obj.p3)), x_obj.p3))
        print(poly_txt.format(a, b, c))
        print(yv_txt.format(x_obj.yv_type(), yv))
        print(off_txt.format(header_ctype(f), f))
        print(x01_txt.format(data_ctype(int(x01)), x01))
        print(x02_txt.format(data_ctype(int(x02)), x02))
        print(x03_txt.format(data_ctype(int(x03)), x03))
        print(poly_txt0.format(a0, b0, c0))
        print(yv_txt0.format(header_ctype(yv0), yv0))
        print(off_txt0.format(header_ctype(f0), f0))
        print(delta_txt0.format(header_ctype(delta0), delta0))
        print(c_g_txt0.format(header_ctype(delta0), c_g0))
        print(q_elements_txt.format(len_all))
        print(q_prime_txt.format(len_primes))
        print(par_type_txt.format(pt=par_type))

        for value, exponent in first.items():
            print('<td class="first composite">{:}^{}</td>'.format(value, exponent), end='')

        for result in sequence:
            if abs(result) is 1:
                print('<td class="data one">{}</td>'.format(result))
            elif result == 0:
                print('<td class="data zero">{}</td>'.format(result))
            elif isprime(result):
                print('<td class="data prime">{}</td>'.format(result))
            elif not (sqrt(abs(result)) * 10) % 2:
                print('<td class="data sqrt_round">{}</td>'.format(result))
            else:
                print('<td class="data composite">{}</td>'.format(result))

        for value, exponent in last.items():
            print('<td class="last composite">{:}^{}</td>'.format(value, exponent), end='')
        print('</tr>')
print('</table>')
print('</body>')
print('</html>')
