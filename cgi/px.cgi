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

#Defining P1, P2, Pn, y and k from user input.
p1a = float(form["p1a"].value)
p2a = float(form["p2a"].value)
p3a = float(form["p3a"].value)
p1b = float(form["p1b"].value)
p2b = float(form["p2b"].value)
p3b = float(form["p3b"].value)
p1c = float(form["p1c"].value)
p2c = float(form["p2c"].value)
p3c = float(form["p3c"].value)
p1d = float(form["p1d"].value)
p2d = float(form["p2d"].value)
p3d = float(form["p3d"].value)
ya = int(form["ya"].value)
yb = int(form["yb"].value)
a_line, b_line, c_line, yv_line, f_line, table_line = tb.fixed_generator(p1a, p2a, p3a, p1b, p2b, p3b, p1c, p2c, p3c, p1d, p2d, p3d, ya, yb)

#print('<h1 id="sequences_header">{0:g},{1:g},Pn TABLE. Black-Hole-Parabola at Pn={2}.</h1>'.format(p1,p2,pna0))
print('<button onclick="window.history.back()">Go Back</button><br /><br />')
print('<table id="sequences_table">') #Starting the table headers
print('<tr class="sequences_table" id="y_vertex"><th class="sequences_table" id="y_vertex">y_vertex</th>') #y_vertex
for yv in yv_line: 
    if yv < 0:
        print('<td class="sequences_table" id="y_vertex_negative" >{:1.4g}</td>'.format(yv))
    elif yv > 0:
        print('<td class="sequences_table" id="y_vertex_positive" >{:1.4g}</td>'.format(yv))
    elif yv == 0:
        print('<td class="sequences_table" id="y_vertex_zero" >{:1.4g}</td>'.format(yv))
    else:
        print('<td class="sequences_table" id="no_y_vertex" > 00 </td>')

print('</tr><tr class="sequences_table" id="offset"><th>offset</th>') #offset
for f in f_line:
    if f < 0:
        print('<td class="sequences_table" id="offset_negative" >{:0.6g}</td>'.format(f))
    elif f > 0:
        print('<td class="sequences_table" id="offset_positive" >{:0.6g}</td>'.format(f))
    elif f == 0:
        print('<td class="sequences_table" id="offset_zero" >{:0.6g}</td>'.format(f))
    else:
        print('<td class="sequences_table" id="no_offset" > 00 </td>')

print('</tr><tr class="sequences_table" id="a"><th>a</th>') #a
for a in a_line:
   print('<td class="sequences_table" id="a">{:1.6g}</td>'.format(a))

print('</tr><tr class="sequences_table" id="b"><th>b</th>') #b
for b in b_line:
   print('<td class="sequences_table" id="b">{:1.6g}</td>'.format(b))

print('</tr><tr class="sequences_table" id="c"><th>c</th>') #c
for c in c_line:
   print('<td class="sequences_table" id="c">{:1.6g}</td>'.format(c))

print('</tr>')

#Starting the table data

for y in range(yb, ya-1, -1):
    if y is 0:
        print('<tr class="sequences_table" id="y_zero"><th class="sequences_table" id="y_zero">{}</th>').format(y) #y
    elif abs(y) is 1:
        print('<tr class="sequences_table" id="y_one"><th class="sequences_table" id="y_one">{}</th>').format(y) #y
    else:
        print('<tr class="sequences_table" id="y"><th class="sequences_table" id="y">{}</th>').format(y) #y

    remendo = ya - y-1
    for result in table_line[remendo]:
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

print('</table>')
print('<br />')
print('<br /><button onclick="window.history.back()">Go Back</button><br />')
print('</body>')
print('</html>')
