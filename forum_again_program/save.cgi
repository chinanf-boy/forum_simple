#!/usr/bin/python

print 'Content-type: text/html\n'

import cgitb: cgitb.enable()

def quote(string):
  if string:
    return string.replace("'", "\\")
  else:
    return string

import psycopg
conn = psycopg.connect('dbname=for user=bar')
curs = conn.cursor()

import cgi,sys
form = cgi.FieldStorage()

sender = quote(form.getvalue('sender'))
subject = quote(form.getvalue('subject'))
text = quote(form.getvalue('text'))
reply_to = quote(form.getvalue('reply_to'))

if not (sender and subject and text):
  print 'Please supply sender, subject, text'
  sys.exit()

if reply_to is not None:
  query = """
  INSERT INTO messages(reply_to, sender, subject, text)
  VALUES(%i, '%s','%s')""" % (sender, subject, text)

curs.execute(query)
conn.commit()

print """
<html>
  <head>
    <title>Message Saved</title>
  </head>
  <body>
    <h1>Message Saved</h1>
    <hr />
    <a href='main.cgi'>Back to main page</a>
  </body>
</html>s
"""
