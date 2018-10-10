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
    print('<link rel="stylesheet" type="text/css" href="/styles/sequence_seekerV4a.css">')
    print('<script src="sequence_seekerV2.js"></script>')
    print('<title>SSE v.2</title>')
    print('</head>')
    print('<body>')

    print('<form action="javascript:sendform()" method="post" id="sequence_seeker_form" name="collect_data_form" >')

    print('<div id="abc">SSE v.2&nbsp;&nbsp;|&nbsp;&nbsp;'
          'P1=&nbsp;<input type="text" name="p1" value="" />&nbsp;&nbsp;'
          'P2=&nbsp;<input type="text" name="p2" value="" />&nbsp;&nbsp;'
          'P2&nbsp;(<input type="text" name="kp2" value="" />)&nbsp;&nbsp;'
          'P3=&nbsp;<input type="text" name="p3" value="" />&nbsp;&nbsp;'
          'P3&nbsp;(<input type="text" name="kp3" value="" />)&nbsp;&nbsp;'
          '#P>=&nbsp;<input type="text" name="min_size" value="" id="min_value"/>'
          '&nbsp;&nbsp;<input type="submit" value="GO" id="submit"/></form></div>')

    print('<div id="datasheet_info">'
          '<span id="init_field_full">Start time=<span id="init_field"></span></span>'
          '<span id="end_field_full">End time=<span id="end_field"></span></span>'
          '<span id="elapsed_field_full">Elapsed time=<span id="elapsed_field"></span></span>'
          '<span id="nextp1_field"></span>'
          '</div>')
    print('<span id="loader"></span><div id="content"></div>')

else:

    p1 = float(form["p1"].value)
    p2 = float(form["p2"].value)
    p3 = float(form["p3"].value)
    kp2 = int(form["kp2"].value)
    kp3 = int(form["kp3"].value)
    min_size = int(form["min_size"].value)

    calc = SequenceSeekerV2(p1, p2, p3, kp3, kp2)

    big_seq = calc(min_size)

    print('<span id="loader"></span><table id="sequence_seeker_table" class="w3-table-all" >')

    for i in range(0, len(big_seq)):
        sequence = big_seq[i]

        x_obj = sequence.pop()
        generation_order = sequence.pop()
        first = factorint(int(sequence.pop(0)))
        last = factorint(int(sequence.pop()))

        print('<tr class="sequence_seeker_header">')
        print('<td class="generation_line">{:.0f}</td>'.format(generation_order))
        print('<td class="print_line">{:g}</td>'.format(i + 1))

        indef = 'undefined'
        infin = '&infin;'

        print('<td class="{}">P1={:g}</td>'.format(data_ctype(int(x_obj.p1)), x_obj.p1))
        print('<td class="{}">P2={:g}</td>'.format(data_ctype(int(x_obj.p2)), x_obj.p2))
        print('<td class="{}">P3={:g}</td>'.format(data_ctype(int(x_obj.p3)), x_obj.p3))

        a = x_obj.a
        b = x_obj.b
        c = x_obj.c
        print('<td class="poly">x={:g}y^2{:+g}y{:+g}</td>'.format(a, b, c))

        yv = x_obj.y_vertex
        if a == 0:
            print('<td class="{} y_vertex">yv={}</td>'.format('infin', infin))
        else:
            print('<td class="{} y_vertex">yv={:.4g}</td>'.format(x_obj.yv_type(), yv))

        f = x_obj.offset
        if a == 0:
            print('<td class="{} offset">f={:}</td>'.format('infin', infin))
        else:
            print('<td class="{} offset">f={:}</td>'.format(header_ctype(f), f))

        x01 = x_obj.x01
        x02 = x_obj.x02
        x03 = x_obj.x03
        print('<td class="{}">x&ordm;1={:g}</td>'.format(data_ctype(int(x01)), x01))
        print('<td class="{}">x&ordm;2={:g}</td>'.format(data_ctype(int(x02)), x02))
        print('<td class="{}">x&ordm;3={:g}</td>'.format(data_ctype(int(x03)), x03))

        a0 = x_obj.a0
        b0 = x_obj.b0
        c0 = x_obj.c0
        print('<td class="poly0">x&ordm;={:g}y^2{:+g}y{:+g}</td>'.format(a0, b0, c0))

        y0v = x_obj.y0_vertex
        if a == 0:
            print('<td class="y_vertex {}">y&ordm;v={}</td>'.format('infin', infin))
        else:
            print('<td class="y_vertex {}">y&ordm;v={:.4g}</td>'.format(header_ctype(y0v), y0v))

        f0 = '{:.4g}'.format(x_obj.offset0)
        print('<td class="offset {}">f&ordm;={}</td>'.format(header_ctype(x_obj.offset0), f0))

        delta = x_obj.delta
        print('<td class="delta {}">&Delta;={:g}</td>'.format(header_ctype(x_obj.delta), delta))

        c_g = x_obj.c_g
        print('<td class="c_g {}" >CG={:.4g}</td>'.format(header_ctype(x_obj.delta), c_g))

        xv = x_obj.xv
        if a == 0:
            print('<td class="xv {}">xv={}</td>'.format(indef, indef))
        else:
            print('<td class="xv {}">xv={:.4g}</td>'.format(header_ctype(x_obj.xv), xv))

        lr = x_obj.lr
        if a == 0:
            print('<td class="lr {}">LR={}</td>'.format(indef, indef))
        else:
            print('<td class="lr {}">LR={:.3g}</td>'.format(header_ctype(x_obj.lr), lr))

        xvlr = x_obj.xvlr
        if a == 0:
            print('<td class="xvlr {}">-xv*LR={}</td>'.format(indef, indef))
        else:
            print('<td class="xvlr {}">-xv*LR={:.4g}</td>'.format(header_ctype(x_obj.xvlr, True), xvlr))

        y0vm_xv_lr = x_obj.y0vm_xv_lr
        if a == 0:
            print('<td class="y0vm_xv_lr {}">y&ordm;v-xv*LR={}</td>'.format(indef, indef))
        else:
            print('<td class="y0vm_xv_lr {}">y&ordm;v-xv*LR={:.4g}</td>'.format(header_ctype(x_obj.y0vm_xv_lr),
                                                                                y0vm_xv_lr))
        y0vp_xv_lr = x_obj.y0vp_xv_lr
        if a == 0:
            print('<td class="y0vp_xv_lr {}">y&ordm;v+xv*LR={}</td>'.format(indef, indef))
        else:
            print('<td class="y0vp_xv_lr {}">y&ordm;v+xv*LR={:.4g}</td>'.format(header_ctype(x_obj.y0vp_xv_lr),
                                                                                y0vp_xv_lr))
        y0v_2 = x_obj.y0v_2
        if a == 0:
            print('<td class="y0v_2 {}">(y&ordm;v)^2={}</td>'.format(indef, indef))
        else:
            print('<td class="y0v_2 {}">(y&ordm;v)^2={:.4g}</td>'.format(header_ctype(x_obj.y0v_2), y0v_2))

        c0_a = x_obj.c0_a
        if a == 0:
            print('<td class="c0_a {}">c&ordm;/a={}</td>'.format(indef, indef))
        else:
            print('<td class="c0_a {}">c&ordm;/a={:.0f}</td>'.format(header_ctype(x_obj.c0_a), c0_a))

        y0v_2c0a = x_obj.y0v_2c0a
        if a == 0:
            print('<td class="y0v_2c0a {}">(y&ordm;v)^2-c&ordm;/a={}</td>'.format(indef, indef))
        else:
            print('<td class="y0v_2c0a {}">(y&ordm;v)^2-c&ordm;/a={:.4g}'
                  '</td>'.format(header_ctype(x_obj.y0v_2c0a, True), y0v_2c0a))

        if x_obj.p1 == x_obj.p2 == x_obj.p3:
            len_all = 'N'
            print('<td class="qtd_elements">#E={}'.format(len_all))
        else:
            len_all = len(big_seq[i])
            print('<td class="qtd_elements">#E={:g}'.format(len_all))

        if x_obj.p1 == x_obj.p2 == x_obj.p3:
            len_primes = '*'
            print('<td class="qtd_primes">#P={}'.format(len_primes))
        else:
            len_primes = len(big_seq[i]) - big_seq[i].count(1) - big_seq[i].count(-1)
            print('<td class="qtd_primes">#P={:g}'.format(len_primes))

        par_type = x_obj.par_type
        print('<td class="{pt}">{pt}</td>'.format(pt=par_type))

        print('<td class="first composite">')
        flag = len(first)
        for value, exponent in first.items():
            flag -= 1
            if flag > 0:
                print('{}^{}*'.format(value, exponent), end='')
            else:
                print('{}^{}'.format(value, exponent), end='')
        print('</td>')

        for result in sequence:
            if abs(result) == 1:
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
