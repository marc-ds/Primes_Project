#!/usr/bin/python

import cgi
import cgitb
from math import floor, sqrt
import table_controller as tb
from project_lib import isprime

cgitb.enable()

print('Content-type: text/html\r\n\r')
print('<html>')
print('<head>')
print('<link rel="stylesheet" type="text/css" href="/styles/style.css">')
print('<title>Sequences table</title>')
print('</head>')
print('<body>')

form = cgi.FieldStorage()

if "p1" not in form or "p2" not in form:
    print("<h1>Error!<h1>")
    print("<p>Please, fill the mandatory fields</p>")
else:
    #Defining P1, P2, Pn, y and k from user input.
    p1 = float(form["p1"].value)
    p2 = float(form["p2"].value)
    p3 = float(form["p3"].value)
    p1_step = float(form["p1_step"].value)
    p2_step = float(form["p2_step"].value)
    p3_step = float(form["p3_step"].value)
    k = int(form["k"].value)
    calc = tb.table_generator(p1, p2, p3, p1_step, p2_step, p3_step, k)
    calc = tb.table_generator(p1, p2, p3, p1_step, p2_step, p3_step, k)

#    print('<h1 id="sequences_header">{0:g},{1:g},Pn TABLE. Black-Hole-Parabola at Pn={2}.</h1>'.format(p1,p2,pna0))
    print('<button onclick="window.history.back()">Go Back</button><br /><br />')
    print('<table id="sequences_table">') #Starting the table headers
    print('<tr class="sequences_table" id="y_vertex"><th class="sequences_table" id="y_vertex">y_vertex</th>') #y_vertex
    for yv in calc.yv_line(list()): 
        if yv < 0:
            print('<td class="sequences_table" id="y_vertex_negative" >{:1.4g}</td>'.format(yv))
        elif yv > 0:
            print('<td class="sequences_table" id="y_vertex_positive" >{:1.4g}</td>'.format(yv))
        elif yv == 0:
            print('<td class="sequences_table" id="y_vertex_zero" >{:1.4g}</td>'.format(yv))
        else:
            print('<td class="sequences_table" id="no_y_vertex" > 00 </td>')

    print('</tr><tr class="sequences_table" id="offset"><th>offset</th>') #offset
    for f in calc.f_line(list()):
        if f < 0:
            print('<td class="sequences_table" id="offset_negative" >{:0.6g}</td>'.format(f))
        elif f > 0:
            print('<td class="sequences_table" id="offset_positive" >{:0.6g}</td>'.format(f))
        elif f == 0:
            print('<td class="sequences_table" id="offset_zero" >{:0.6g}</td>'.format(f))
        else:
            print('<td class="sequences_table" id="no_offset" > 00 </td>')

    print('</tr><tr class="sequences_table" id="a"><th>a</th>') #a
    for a in calc.a_line:
       print('<td class="sequences_table" id="a">{:1.6g}</td>'.format(a))

    print('</tr><tr class="sequences_table" id="b"><th>b</th>') #b
    for b in calc.b_line:
       print('<td class="sequences_table" id="b">{:1.6g}</td>'.format(b))

    print('</tr><tr class="sequences_table" id="c"><th>c</th>') #c
    for c in calc.c_line:
       print('<td class="sequences_table" id="c">{:1.6g}</td>'.format(c))

    print('</tr>')

#  Starting the table data

    for y in range(yb, ya-1, -1):
        if y is 0:
            print('<tr class="sequences_table" id="y_zero"><th class="sequences_table" id="y_zero">{}</th>').format(y) #y
        elif abs(y) is 1:
            print('<tr class="sequences_table" id="y_one"><th class="sequences_table" id="y_one">{}</th>').format(y) #y
        else:
            print('<tr class="sequences_table" id="y"><th class="sequences_table" id="y">{}</th>').format(y) #y
        for result in calc.table_line(list(), y):
            if y > 1 or y < -1:
                if abs(result) is 1:
                    print('<td class="sequences_table" id="one">{}</td>'.format(result))
                elif result == 0:
                    print('<td class="sequences_table" id="zero">{}</td>'.format(result))
                elif isprime(result):
                    print('<td class="sequences_table" id="prime">{}</td>'.format(result))
                elif not (sqrt(abs(result))*10)%2:
                    print('<td class="sequences_table" id="sqrt_round">{}</td>'.format(result))
                else:
                    print('<td class="sequences_table" id="composite">{}</td>'.format(result))
            else:
                if abs(result) is 1:
                    print('<td class="sequences_table" id="y0_one">{}</td>'.format(result))
                elif result == 0:
                    print('<td class="sequences_table" id="zero">{}</td>'.format(result))
                elif isprime(result):
                    print('<td class="sequences_table" id="y0_prime">{}</td>'.format(result))
                elif not (sqrt(abs(result))*10)%2:
                    print('<td class="sequences_table" id="y0_sqrt_round">{}</td>'.format(result))
                else:
                    print('<td class="sequences_table" id="y0_composite">{}</td>'.format(result))
        print('</tr>') 

#### Density starts here, baby.

    if den_yn:
        print('<tr class="density" id="density_pos_abs"><th># Primes <br>y &ge; 1</th>')
        den_pos_list, den_neg_list, den_total_list = calc.density_line(den_yn)
        for value in den_pos_list:
            print('<td class="sequences_table" id="density_pos_abs">{}</td>'.format(value))
        print('</tr>')
        print('<tr class="density" id="density_pos_rel"><th>% Primes <br> y &ge; 1</th>')
        for value in den_pos_list:
            print('<td class="sequences_table" id="density_pos_rel">{:.2f}%</td>'.format((value/float(den_yn))*100))
        print('</tr>')
        print('<tr class="density" id="density_neg_abs"><th># Primes <br> y &le; 0</th>')
        for value in den_neg_list:
            print('<td class="sequences_table" id="density_neg_abs">{}</td>'.format(value))
        print('</tr>')
        print('<tr class="density" id="density_neg_rel"><th>% Primes <br> y &le; 0</th>')
        for value in den_neg_list:
            print('<td class="sequences_table" id="density_neg_rel">{:.2f}%</td>'.format((value/float(den_yn))*100))
        print('</tr>')
        print('<tr class="density" id="density_total_abs"><th># Primes <br>total</th>')
        for value in den_total_list:
            print('<td class="sequences_table" id="density_total_abs">{}</td>'.format(value))
        print('</tr>')
        print('<tr class="density" id="density_total_rel"><th>% Primes <br>total </th>')
        for value in den_total_list:
            print('<td class="sequences_table" id="density_total_rel">{:.2f}%</td>'.format((value/float(den_yn))*100))
        print('</tr>')
    print('</table>')
    print('<br />')
    print('<br /><button onclick="window.history.back()">Go Back</button><br />')
print('</body>')
print('</html>')
