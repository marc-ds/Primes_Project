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
    print('<div id="p_value">P1=<input type="text" name="p1" value="2" />')
    print('P1<=P2<=P<input type="text" name="kp2" value="1000" />')
    print('P2<=P3<=P<input type="text" name="kp3" value="1000" />')
    print('#P>=<input type="text" name="min_size" value="20" id="min_value"/>')
    print('<span id="loader">Loading...</span>')
    print('<input type="submit" value="Generate" id="submit"/></form></div>')

    print('<table id="sequence_seeker" class="table_sequence_seeker" >')
else:

    p1 = float(form["p1"].value)
    kp2 = int(form["kp2"].value)
    kp3 = int(form["kp3"].value)
    min_size = int(form["min_size"].value)

    print('<form action="javascript:sendformv3()" method="post" id="sequence_seeker">')
    print('<div id="p_value">P1=<input type="text" name="p1" value="{:g}" />'.format(p1))
    print('P1<=P2<=P<input type="text" name="kp2" value="{}" />'.format(kp2))
    print('P2<=P3<=P<input type="text" name="kp3" value="{}" />'.format(kp3))
    print('#P>=<input type="text" name="min_size" value="{}" id="min_value"/>'.format(min_size))
    print('<span id="loader">Loading...</span>')
    print('<input type="submit" value="Generate" id="submit"/></form></div>')

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
        yv0 = x_obj.y0_vertex
        f0 = x_obj.offset0
        a0 = x_obj.a0
        b0 = x_obj.b0
        c0 = x_obj.c0
        x01 = x_obj.x01
        x02 = x_obj.x02
        x03 = x_obj.x03
        y0v_2 = x_obj.y0v_2
        xv = x_obj.xv
        lr = x_obj.lr
        c0_a = x_obj.c0_a
        y0v_2c0a = x_obj.y0v_2c0a
        xvlr = x_obj.xvlr
        y0vp_xv_lr = x_obj.y0vp_xv_lr
        y0vm_xv_lr = x_obj.y0vm_xv_lr
        par_type = x_obj.par_type
        len_all = len(big_seq[i])
        len_primes = len(big_seq[i]) - big_seq[i].count(1) - big_seq[i].count(-1)

        p1_txt = '<td class="{}">P1={:g}</td>'
        p2_txt = '<td class="{}">P2={:g}</td>'
        p3_txt = '<td class="{}">P3={:g}</td>'
        poly_txt = '<td class="poly">x={:g}y^2{:+g}y{:+g}</td>'
        yv_txt = '<td class="{} y_vertex">yv={:1.4g}</td>'
        f_txt = '<td class="{} offset">f={:1.4g}</td>'
        poly0_txt = '<td class="poly0">x&ordm;={:g}y^2{:+g}y{:+g}</td>'
        y0v_txt = '<td class="y_vertex {}">y&ordm;v={:1.4g}</td>'
        f0_txt = '<td class="offset {}">f&ordm;={}</td>'
        delta_txt = '<td class="delta {}">&Delta;={:.0f}</td>'
        c_g_txt = '<td class="c_g {}" >CG={:.4g}</td>'
        x01_txt = '<td class="{}">x&ordm;1={:g}</td>'
        x02_txt = '<td class="{}">x&ordm;2={:g}</td>'
        x03_txt = '<td class="{}">x&ordm;3={:g}</td>'
        xv_txt = '<td class="xv {}">xv={:.4g}</td>'
        lr_txt = '<td class="lr {}">LR={:.4g}</td>'
        xvlr_txt = '<td class="xvlr {}">-xv*LR={:.4g}</td>'
        y0vp_xv_lr_txt = '<td class="y0vp_xv_lr {}">y&ordm;v+xv*LR={:.4g}</td>'
        y0vm_xv_lr_txt = '<td class="y0vm_xv_lr {}">y&ordm;v-xv*LR={:.4g}</td>'
        y0v_2_txt = '<td class="y0v_2 {}">(y&ordm;v)^2={:.4g}</td>'
        c0_a_txt = '<td class="c0_a {}">c&ordm;/a={:.0f}</td>'
        y0v_2c0a_txt = '<td class="y0v_2c0a {}">(y&ordm;v)^2-c&ordm;/a={:.4g}</td>'
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
        print(f_txt.format(header_ctype(f), f))

        print(x01_txt.format(data_ctype(int(x01)), x01))
        print(x02_txt.format(data_ctype(int(x02)), x02))
        print(x03_txt.format(data_ctype(int(x03)), x03))

        print(poly0_txt.format(a0, b0, c0))
        print(y0v_txt.format(header_ctype(yv0), yv0))
        print(f0_txt.format(header_ctype(f0), f0))
        print(delta_txt.format(header_ctype(delta), delta))
        print(c_g_txt.format(header_ctype(delta), c_g))

        print(xv_txt.format(header_ctype(xv), xv))
        print(lr_txt.format(header_ctype(lr), lr))
        print(xvlr_txt.format(header_ctype(xvlr, True), xvlr))
        print(y0vp_xv_lr_txt.format(header_ctype(y0vp_xv_lr), y0vp_xv_lr))
        print(y0vm_xv_lr_txt.format(header_ctype(y0vm_xv_lr), y0vm_xv_lr))
        print(y0v_2_txt.format(header_ctype(y0v_2), y0v_2))
        print(c0_a_txt.format(header_ctype(c0_a), c0_a))
        print(y0v_2c0a_txt.format(header_ctype(y0v_2c0a, True), y0v_2c0a))
        print(q_elements_txt.format(len_all))
        print(q_prime_txt.format(len_primes))
        print(par_type_txt.format(pt=par_type))

        print('<td class="first composite">')
        flag = len(first)
        for value, exponent in first.items():
            flag-=1
            if flag > 0:
                print('{:}^{}*'.format(value, exponent), end='')
            else:
                print('{:}^{}'.format(value, exponent), end='')
        print('</td>')

        for result in sequence:
            if abs(result) is 1:
                print('<td class="data one">{:g}</td>'.format(result))
            elif result == 0:
                print('<td class="data zero">{:0g}</td>'.format(result))
            elif isprime(result):
                print('<td class="data prime">{:0g}</td>'.format(result))
            elif not (sqrt(abs(result)) * 10) % 2:
                print('<td class="data sqrt_round">{:0g}</td>'.format(result))
            else:
                print('<td class="data composite">{:2g}</td>'.format(result))

        print('<td class="last composite">')
        flag = len(last)
        for value, exponent in last.items():
            flag -= 1
            if flag > 0:
                print('{:}^{}*'.format(value, exponent), end='')
            else:
                print('{:}^{}'.format(value, exponent), end='')
        print('</td>')

        print('</tr>')
print('</table>')
print('</body>')
print('</html>')
