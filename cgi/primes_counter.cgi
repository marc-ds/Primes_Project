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
print('<link rel="stylesheet" type="text/css" href="/styles/primes_counter.css">')
print('<title>Sequences table</title>')
print('</head>')
print('<body>')

form = cgi.FieldStorage()

if "p1" not in form or "p2" not in form:
    print("<h1>Error!<h1>")
    print("<p>Please, fill the mandatory fields</p>")
else:
    p1 = float(form["p1"].value)
    p2 = float(form["p2"].value)
    p3 = float(form["p3"].value)
    p1_step = float(form["p1_step"].value)
    p2_step = float(form["p2_step"].value)
    p3_step = float(form["p3_step"].value)
    k = int(form["k"].value)
    calc = tb.table_generator(p1, p2, p3, p1_step, p2_step, p3_step, k)
    sequences = calc.primes_sequences()

    print('<h1 id="primes_sequences_header">Primes Counter</h1>')
    print('<button onclick="window.history.back()">Go Back</button><br /><br />')
    print('<table id="primes_sequences">') #Starting the table
    for sequence in sequences:
        print('<tr class="primes_sequences">')
        for item in sequence:
            print('<td class="primes_sequences">{}</td>'.format(item))
        print('</td>')
    print('</table>')
    print('<br /><button onclick="window.history.back()">Go Back</button><br />')
print('</body>')
print('</html>')
