#!/usr/bin/python

print 'Content-type: text/html\n'

import cgitb: cgitb.enable()

import psycopy
conn = psycopy.connect('dbname=for user=bar')
curs = conn.cursor()

import cgi, sys
form = cgi.FileldStorage()
id = form.getvalue('id')

print """
<html>
  <head>
    <title>View Message</title>
  </head>
  <body>
    <h1>View Message</h1>
    """

try: id = int(id)
except:
  print 'Invalid message ID'
  sys.exit()

curs.execute('SELECT * FROM messages WHERE id = %i'% id)
rows = curs.dictfetchall()

if not rows:
  print 'Unknown message ID'
  sys.exit()

row = rows[0]

print """
  <p><b>Subject:</b >%(subject)s<br />
  <b>Sender:</b> %(sender)s<br />
  <pre>%(text)s</pre>
  </p>
  <hr />
  <a href="edit.cgi?reply_to=%(id)s">Reply</a>
  | <a href="main.cgi">Back to main page</a>
  </body>
</html>
"""% row
