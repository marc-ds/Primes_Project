import cgi
import cgitb
import sympy as sp

print('Content-type: text/html\r\n\r')

cgitb.enable()
form = cgi.FieldStorage()

p1 = int(form["p1"].value)
kp1 = int(form["kp1"].value)
kp2 = int(form["kp2"].value)
kp3 = int(form["kp3"].value)
min_size = int(form["min_size"].value)

print('<span id="nextp1">The P1 next sequence is {}</span>').format(sp.nextprime(p1, kp1+1))
