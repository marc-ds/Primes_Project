#!/usr/bin/python3

import cgi
import cgitb
from blockbuster_controller import *

cgitb.enable()
form = cgi.FieldStorage()

print('Content-type: text/html\r\n\r')
print('<html>')
print('<head>')
print('<link rel="stylesheet" type="text/css" href="/styles/style.css">')
print('<title>Sequences table</title>')
print('</head>')
print('<body>')
print('<form action="/v2/blockbuster_view.py" method="post" id="sequence_seeker">')

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


    print('<div id="p_value">P1 value = <input type="text" name="p1a" value="{}" />'.format(p1a))
    print('P2 value &nbsp;= <input type="text" name="p2a" value="{}" />'.format(p2a))
    print('P3 value = <input type="text" name="p3a" value="{}" /></div>'.format(p3a))
    print('<div id="p_value">P1 value = <input type="text" name="p1b" value="{}" />'.format(p1b))
    print('P2 value &nbsp;= <input type="text" name="p2b" value="{}" />'.format(p2b))
    print('P3 value = <input type="text" name="p3b" value="{}" /></div>'.format(p3b))
    print('<div id="p_value">P1 value = <input type="text" name="p1c" value="{}" />'.format(p1c))
    print('P2 value &nbsp;= <input type="text" name="p2c" value="{}" />'.format(p2c))
    print('P3 value = <input type="text" name="p3c" value="{}" /></div>'.format(p3c))
    print('<div id="p_value">P1 value = <input type="text" name="p1d" value="{}" />'.format(p1d))
    print('P2 value &nbsp;= <input type="text" name="p2d" value="{}" />'.format(p2d))
    print('P3 value = <input type="text" name="p3d" value="{}" /></div>'.format(p3d))
    print('Y initial = <input type="text" name="y_start" value="{}" /></div>')
    print('Y final = <input type="text" name="y_end" value="{}" /></div>')
    print('<input type="submit" value="Generate" id="submit"/></div></form>')

    bbuster = Blockbuster(y_start, y_end)
    bbuster.add(p1a, p2a, p3a)
    bbuster.add(p1b, p2b, p3b)
    bbuster.add(p1c, p2c, p3c)
    bbuster.add(p1d, p2d, p3d)

    print('<table id="blockbuster">')

    print('<tr id="y_vertex">')
    print('<th id="y_vertex"> y_vertex </th>')
    for item in bbuster.y_vertex():
        print('<td class="{}" id="y_vertex">{}</td>'.format(item.yv_type(), item.y_vertex))
    print('</tr>')

    print('<tr id="offset">')
    print('<th id="offset"> offset </th>')
    for item in bbuster.offset():
        print('<td class="{}" id="offset">{}</td>'.format(item.f_type(), item.offset))
    print('</tr>')

    print('<tr id="delta">')
    print('<th id="delta"> &Delta; </th>')
    for item in bbuster.delta():
        print('<td class="{}" id="delta">{}</td>'.format(item.d_type(), item.delta))
    print('</tr>')

    print('<tr id="c_g">')
    print('<th id="c_g"> C.G. </th>')
    for item in bbuster.c_g():
        print('<td class="{}" id="c_g">{}</td>'.format(item.cg_type(), item.c_g))
    print('</tr>')

    print('<tr id="a" >')
    print('<th id="a"> a </th>')
    for item in bbuster.a():
        print('<td class="a" id="a">{}</td>'.format(item.a))
    print('</tr>')

    print('<tr id="b">')
    print('<th id="b"> b </th>')
    for item in bbuster.b():
        print('<td class="b" id="b">{}</td>'.format(item.b))
    print('</tr>')

    print('<tr id="c">')
    print('<th id="c"> c </th>')
    for item in bbuster.c():
        print('<td class="c" id="c">{}</td>'.format(item.c))
    print('</tr>')

    for y in bbuster.y_range:

        print('<tr id="y{}" class="y">'.format(y))
        print('<th class="y"> {} </th>'.format(y))

        for item in bbuster(y):
            print('<td class="{}" id="data">{}</td>'.format(item.type(), item()))

    print('</tr>')

    print('</table>')

    print('</body>')

print('</html>')