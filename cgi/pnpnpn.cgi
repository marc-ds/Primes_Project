#!/usr/bin/python

import cgi
import cgitb
from project_lib import *
from math import floor, sqrt

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
    p2 = float(form['p2'].value)
    p3 = float(form['p3'].value)
    pn = int(form["pn"].value)
    ya = int(form["ya"].value)
    yb = int(form["yb"].value)
    k = int(form["k"].value)
    pna0 = int((-p1)+(2*p2)) #Pn(@a=0)
    pn_initial = pna0-(pn*k)
    pn_final = pna0+((pn+1)*k)
    pn_range = range(pn_initial, pn_final, k) #Pn range defnition

    #print('<h1 id="sequences_header">{0:g},{1:g},Pn TABLE. Black-Hole-Parabola at Pn={2}.</h1>'.format(p1,p2,pna0))
    print('<h1> We need a name here </h1>')
    print('<button onclick="window.history.back()">Go Back</button><br /><br />')
    print('<table id="sequences_table">') #Starting the table headers
    print('<tr class="sequences_table" id="y_vertex"><th class="sequences_table" id="y_vertex">y_vertex</th>') #y_vertex
    for px in pn_range: 
       a,b,c = abc_set(p1+px,p2+px,p3+px) 
       if a!=0:
           yv = y_vertex(a,b,c)
           if yv < 0:
               print('<td class="sequences_table" id="y_vertex_negative" >{:1.4g}</td>'.format(yv))
           elif yv > 0:
               print('<td class="sequences_table" id="y_vertex_positive" >{:1.4g}</td>'.format(yv))
           else:
               print('<td class="sequences_table" id="y_vertex_zero" >{:1.4g}</td>'.format(yv))

       else:
           print('<td class="sequences_table" id="no_y_vertex" > 00 </td>')

    print('</tr><tr class="sequences_table" id="offset"><th>offset</th>') #offset
    for px in pn_range:
       a,b,c = abc_set(p1+px,p2+px,p3+px) 
       if a!=0:
           f = offset(a,b,c)
           if f < 0:
               print('<td class="sequences_table" id="offset_negative" >{:0.6g}</td>'.format(f))
           elif f > 0:
               print('<td class="sequences_table" id="offset_positive" >{:0.6g}</td>'.format(f))
           else:
               print('<td class="sequences_table" id="offset_zero" >{:0.6g}</td>'.format(f))

       else:
           print('<td class="sequences_table" id="no_offset" > 00 </td>')

    print('</tr><tr class="sequences_table" id="a"><th>a</th>') #a
    for px in pn_range:
       a = ((p1+px)-(2*(p2+px))+(p3+px))/2
       print('<td class="sequences_table" id="a">{:1.6g}</td>'.format(a))

    print('</tr><tr class="sequences_table" id="b"><th>b</th>') #b
    for px in pn_range:
       b = ((p3+px)-(p1+px))/2
       print('<td class="sequences_table" id="b">{:1.6g}</td>'.format(b))

    print('</tr><tr class="sequences_table" id="c"><th>c</th>') #c
    for px in pn_range:
       c = p2+px
       print('<td class="sequences_table" id="c">{:1.6g}</td>'.format(c))

    print('</tr>')

#  Starting the table

    for y in range(yb, ya-1, -1):
        if y is 0:
            print('<tr class="sequences_table" id="y_zero"><th class="sequences_table" id="y_zero">{}</th>').format(y) #y
        elif abs(y) is 1:
            print('<tr class="sequences_table" id="y_one"><th class="sequences_table" id="y_one">{}</th>').format(y) #y
        else:
            print('<tr class="sequences_table" id="y"><th class="sequences_table" id="y">{}</th>').format(y) #y
        for px in pn_range:
            a,b,c = abc_set(p1+px,p2+px,p3+px)
            result = p1p2pn(a,b,c,y)
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
    
    den_pos=dict()
    den_neg=dict()
    den_sum=dict()
    den_y0=dict()
    pn_range_dneg = range(pn_initial, pn_final, k) #Pn range defnition

    print('<tr class="density" id="density_pos_abs"><th># Primes <br>y &ge; 1</th>')
    for px in pn_range:
        a,b,c=abc_set(p1+px,p2+px,p3+px)
        qtd = int(form["y_density"].value)
        den_pos[px],den_y0[px] = density(a,b,c,qtd)
        
        print('<td class="sequences_table" id="density_pos_abs">{}</td>'.format(den_pos[px]))
    print('</tr>')
    print('<tr class="density" id="density_pos_rel"><th>% Primes <br> y &ge; 1</th>')
    for px in pn_range:
        print('<td class="sequences_table" id="density_pos_rel">{:.2f}%</td>'.format((den_pos[px]/float(qtd))*100))
    print('</tr>')
    print('<tr class="density" id="density_neg_abs"><th># Primes <br> y &le; 0</th>')
    for px in pn_range_dneg:
        a,b,c=abc_set(p1+px,p2+px,p3+px)
        den_neg[px], den_y0[px] = density(a,b,c,-qtd)
        print('<td class="sequences_table" id="density_neg_abs">{}</td>'.format(den_neg[px]+den_y0[px]))
    print('</tr>')
    print('<tr class="density" id="density_neg_rel"><th>% Primes <br> y &le; 0</th>')
    for px in pn_range_dneg:
        print('<td class="sequences_table" id="density_neg_rel">{:.2f}%</td>'.format(((den_neg[px]+den_y0[px])/float(qtd))*100))
    print('</tr>')
    print('<tr class="density" id="density_total_abs"><th># Primes <br>total</th>')
    for px in pn_range:
        a,b,c=abc_set(p1+px,p2+px,p3+px)
        den_sum[px] = int((den_neg[px]) + int(den_pos[px])+int(den_y0[px]))
        print('<td class="sequences_table" id="density_total_abs">{}</td>'.format(den_sum[px]))
    print('</tr>')
    print('<tr class="density" id="density_total_rel"><th>% Primes <br>total </th>')
    for px in pn_range:
        print('<td class="sequences_table" id="density_total">{:.2f}%</td>'.format((den_sum[px]/(float(qtd*2)))*100))
    print('</tr>')

    print('</table>')
    print('<br />')
    
    print('<button onclick="window.history.back()">Go Back</button><br /><br />')

    del den_pos
    del den_neg
    del den_sum
    del den_y0

    print('</table>')
#    print('<br /><button onclick="window.history.back()">Go Back</button><br />')
print('</body>')
print('</html>')
