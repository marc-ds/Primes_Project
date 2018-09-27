#!/usr/bin/python3

import cgi
import cgitb
from blockbuster_controller import *
from views_helper import *

cgitb.enable()
form = cgi.FieldStorage()

print('Content-type: text/html\r\n\r')
print('<html>')
print('<head>')
print('<link rel="stylesheet" type="text/css" href="/styles/style.css">')
print('<title>Sequences table</title>')
print('</head>')
print('<body>')
print('<form action="/v2/blockbuster_view.py" method="post" id="blockbuster">')

if "p1a" not in form or "p2a" not in form or "p3a" not in form:


    print('<div id="p_value">P1 value = <input type="text" name="p1a" value="0" />')
    print('P2 value &nbsp;= <input type="text" name="p2a" value="0" />')
    print('P3 value = <input type="text" name="p3a" value="0" /></div>')
    print('<div id="p_value">P1 value = <input type="text" name="p1b" value="0" />')
    print('P2 value &nbsp;= <input type="text" name="p2b" value="0" />')
    print('P3 value = <input type="text" name="p3b" value="0" /></div>')
    print('<div id="p_value">P1 value = <input type="text" name="p1c" value="0" />')
    print('P2 value &nbsp;= <input type="text" name="p2c" value="0" />')
    print('P3 value = <input type="text" name="p3c" value="0" /></div>')
    print('<div id="p_value">P1 value = <input type="text" name="p1d" value="0" />')
    print('P2 value &nbsp;= <input type="text" name="p2d" value="0" />')
    print('P3 value = <input type="text" name="p3d" value="0" /></div>')
    print('y initial&nbsp;&nbsp; = <input type="text" name="y_start" value="-20" /></div>')
    print('y final &nbsp;&nbsp;&nbsp;&nbsp;= <input type="text" name="y_end" value="20" /></div>')
    print('<input type="submit" value="Generate" id="submit"/></div></form>')
    print('<h1 id="sequence_seeker">Please fill the fields</h1>')
    print('</body>')
    print('</html>')

else:

    p1a = float(form["p1a"].value)
    p2a = float(form["p2b"].value)
    p3a = float(form["p3c"].value)
    p1b = float(form["p1b"].value)
    p2b = float(form["p2b"].value)
    p3b = float(form["p3b"].value)
    p1c = float(form["p1c"].value)
    p2c = float(form["p2c"].value)
    p3c = float(form["p3c"].value)
    p1d = float(form["p1d"].value)
    p2d = float(form["p2d"].value)
    p3d = float(form["p3d"].value)
    y_start = int(form["y_start"].value)
    y_end = int(form["y_end"].value)


    print('<div id="p_value">P1 value = <input type="text" name="p1a" value="{:g}" />'.format(p1a))
    print('P2 value &nbsp;= <input type="text" name="p2a" value="{:g}" />'.format(p2a))
    print('P3 value = <input type="text" name="p3a" value="{:g}" /></div>'.format(p3a))
    print('<div id="p_value">P1 value = <input type="text" name="p1b" value="{:g}" />'.format(p1b))
    print('P2 value &nbsp;= <input type="text" name="p2b" value="{:g}" />'.format(p2b))
    print('P3 value = <input type="text" name="p3b" value="{:g}" /></div>'.format(p3b))
    print('<div id="p_value">P1 value = <input type="text" name="p1c" value="{:g}" />'.format(p1c))
    print('P2 value &nbsp;= <input type="text" name="p2c" value="{:g}" />'.format(p2c))
    print('P3 value = <input type="text" name="p3c" value="{:g}" /></div>'.format(p3c))
    print('<div id="p_value">P1 value = <input type="text" name="p1d" value="{:g}" />'.format(p1d))
    print('P2 value &nbsp;= <input type="text" name="p2d" value="{:g}" />'.format(p2d))
    print('P3 value = <input type="text" name="p3d" value="{:g}" /></div>'.format(p3d))
    print('Y initial&nbsp; = <input type="text" name="y_start" value="{}" /></div>'.format(y_start))
    print('Y final&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; = <input type="text" name="y_end" value="{}" /></div>'.format(y_end))
    print('<input type="submit" value="Generate" id="submit"/></div></form>')

    bbuster = Blockbuster(y_start, y_end)
    bbuster.add(p1a, p2a, p3a)
    bbuster.add(p1b, p2b, p3b)
    bbuster.add(p1c, p2c, p3c)
    bbuster.add(p1d, p2d, p3d)

    print('<div id="container_table">')
    show_table(bbuster,'blockbuster')
    show_table(bbuster,'blockbuster-inv', 'no', 'inv')
    print('</div>')

    print('<div id="container_table">')
    show_table(bbuster,'blockbuster0', 'f0')
    show_table(bbuster,'blockbuster0-inv', 'f0', 'inv')
    print('</div>')

    print('</body>')

print('</html>')