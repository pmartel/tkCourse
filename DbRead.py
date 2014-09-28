#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
from sqlite3 import dbapi2 as sqlite

# Connect to an existing database
con = sqlite.connect('mydatabase.db3')
cur = con.cursor()

# Get row by row
print( "Row by row:")
cur.execute('select id, name from clients order by name;')
row = cur.fetchone()
while row:
 print( row)
 row = cur.fetchone()

# Get all rows at once:
print( "All rows at once:")
cur.execute('select id, name from clients order by name;')
print( cur.fetchall())

cur.close()
con.close()
