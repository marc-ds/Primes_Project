#!/usr/bin/python

import cgi
import cgitb
from math import floor, sqrt
from main_controller import *

print('Content-type: text/html\r\n\r')
print('<html>')
print('<head>')
print('<link rel="stylesheet" type="text/css" href="/styles/style.css">')
print('<title>Sequences table</title>')
print('</head>')
print('<body>')

form = cgi.FieldStorage()

p1 = float(form["p1"].value)
p2 = float(form["p2"].value)
p3 = float(form["p3"].value)
p1_step = float(form["p1_step"].value)
p2_step = float(form["p2_step"].value)
p3_step = float(form["p3_step"].value)
k = int(form["k"].value)

calc = SequenceSeeker(p1, p2, p3, p1_step, p2_step, p3_step, k)
yv_seq, off_seq, abc_seq, big_seq = calc(min_size)
print('<table id=sequence_seeker>')

for i in range(0, len(big_seq)):
    first = int(big_seq[i].pop(0))
    last = int(big_seq[i].pop())
    print('<tr class="sequence_seeker_header">')
    yv_txt = '<th class="sequence_seeker" id="{}" >y_vertex: {:1.4g}</th>'
    yv = yv_seq[i]
    if yv < 0:
        print(yv_txt.format(y_vertex_negative, yv))
    elif yv > 0:
        print(yv_txt.format(y_vertex_positive, yv))
    elif yv == 0:
        print(yv_txt.format(y_vertex_zero, yv))
    else:
        print(yv_txt.format(no_y_vertex, yv))
    off_txt = '<th class="sequence_seeker" id="{}" >offset: {:1.4g}</th>'
    f = off_seq[i]
    if f < 0:
        print(off_txt.format(offset_negative, f))
    elif f > 0:
        print(off_txt.format(offset_positive, f))
    elif f == 0:
        print(off_txt.format(offset_zero, f))
    else:
        print(off_txt.format(no_offset, f))
    abc = abc_seq[i]
    a = abc[0]
    print('<th class="sequence_seeker" id="a" >a: {:g.0}</th>'.format(a))
    b = abc[0]
    print('<th class="sequence_seeker" id="b" >b: {:g.0}</th>'.format(b))
    c = abc[0]
    print('<th class="sequence_seeker" id="c" >c: {:g.0}</th>'.format(c))
    length = len(big_seq[i]) - big_seq[i].count(1) - big_seq[i].count(-1)
    print('<th class="sequence_seeker" id="qtd_primes" >Primes in the above sequence: {}.').format(length)

print('</body>')
print('</html>')