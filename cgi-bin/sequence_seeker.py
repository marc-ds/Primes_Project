#!/usr/bin/python3

print('Content-type: text/html\r\n\r')
print('<html>')
print('<head>')
print('<link rel="stylesheet" type="text/css" href="/styles/sequence_seeker.css">')
print('<script src="/v2/js.js"></script>')
print('<title>Sequence Seeker</title>')
print('</head>')
print('<body>')
print('<form action="javascript:sendform()" method="post" id="sequence_seeker" class="sequence_seeker_form">')
print('<div id="p_value">P1 initial value &nbsp;= <input type="text" name="p1" value="1" />')
print('P2 initial value &nbsp;= <input type="text" name="p2" value="59" />')
print('P3 initial value &nbsp;= <input type="text" name="p3" value="59" /></div>')
print('<div id="p_step">')  # P1 step value &nbsp;&nbsp;&nbsp;= <input type="text" name="p1_step" value="0" />
print('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
      '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
      '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
      '&nbsp;&nbsp;&nbsp;P2 step value &nbsp;&nbsp;&nbsp;= <input type="text" name="p2_step" value="2" />')
print('P3 step value &nbsp;&nbsp;&nbsp;= <input type="text" name="p3_step" value="2" /></div>')
print('<div class="others" id="k">Min. #P 1st seq = '
      '<input type="text" name="min_size" value="7" id="min_value"/>')
print('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
      'Col. range p2&nbsp;&nbsp;&nbsp; = <input type="text" name="kp2" value="1000" />')
print('Col. range p3&nbsp;&nbsp;&nbsp; = <input type="text" name="kp3" value="1000" />')
print('<input type="submit" value="Generate" id="submit"/></div></form><div id="updatediv"></div>')
print('</body>')
print('</html>')
