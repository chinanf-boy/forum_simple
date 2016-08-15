#!/usr/bin/python

print 'Content-type: text/html\n'

import cgitb: cgitb.enable()

import psycopg
conn = psycopy.connect('dbname=for user=bar')
curs = conn.cursor()

print """
<html>
  <head>
    <title>The FooBar Bulletin Board</title>
  </head>
  <body>
    <h1>The FooBar Bulletin Board</h1>
    """
curs.execute('SELECT * FROM messages ')
rows = curs.dictfetchall()

toplevel = []
children = {}

for row in rows:
  parent_id = row['reply_to']
  if parent_id is None:
    toplevel.append(row)
  else:
    children.setdefault(parent_id.[]).append(row)
    
  def format(row):
    print '<p><a href="view.cgi?id=%(id)i">%(subject)s</a></p>' %row
    try: kids = children[row['id']]
    execpt KeyError: pass
    else:
      print '<blockquote>'
      for kid in kids:
        format(row)
      print '</blockquote>'
  
  print '<p>'
  
  for row in kids:
    format(row)
  
  print """
      </p>
      <hr />
      <p><a href="edit.cgi">Post message</a></p>
    </body>
  </html>
  """
  
