#! /usr/bin/env python

import cgi
import os
import json
import sys

form = cgi.FieldStorage()
loggedinok = False

if form.getvalue('user') == 'bob' and form.getvalue('password') == 'hunter2':
	loggedinok=True


# http://localhost:8000/
# inside of cgi, print is send to the browser
print "Content-type: text/html"

if loggedinok:
	print "Set-Cookie: loggedin = true"

if 'loggedin=true' in os.environ['HTTP_COOKIE']:
	loggedinok = True

print
#print "<HTML><BODY><H1>Hello, World!</H1></BODY></HTML>"
print "<HTML><BODY><H1>Hello, World!</H1>"

# make a loin form in html
#print "<FORM method = 'GET'><INPUT name = 'user'/>"
# chane get to post then password won't show in url
print "<FORM method = 'POST'><INPUT name = 'user'/>"
# make the password as dot
print "<INPUT name= 'password' type = 'password'>"
print "<BUTTON type = 'submit'>Log in </BUTTON>"
print "</FORM>"

# http://localhost:8000/cgi_script.py?q=x
print "<P> Query strig was: " + os.environ['QUERY_STRING']+ "</P>"
print "<P> Your browser is: " + os.environ['HTTP_USER_AGENT']+ "</P>"


#if os.environ['CONTENT_LENGTH']:
#	print "<P> Standard Input is: " + sys.stdin.read(int(os.environ['CONTENT_LENGTH']))
#print "</P>"
print "<P>"
print "User name was: " + form.getvalue('user') +". "
print "Password was: " + form.getvalue('password') + ". "
print "</P>"
if loggedinok:
	print"<H2>login ok</H2>"

cgi.print_environ()

# http://localhost:8000/cgi_script.py
# import os an json to get variable directly
print json.dumps(dict(os.environ), indent=4)

print "</BODY><HTML>"
