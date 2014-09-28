#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
from sqlite3 import dbapi2 as sqlite

# Create a database:
con = sqlite.connect('mydatabase.db3')
cur = con.cursor()

# Create a table:
cur.execute('create table clients (id INT PRIMARY KEY, name CHAR(60))')

# Insert a single line:
client = (5,"John Smith")
cur.execute("insert into clients (id, name) values (?, ?)", client )
con.commit()

# Insert several lines at once:
clients = [ (7,"Ella Fitzgerald"),
         (8,"Louis Armstrong"),
         (9,"Miles Davis")
       ]
cur.executemany("insert into clients (id, name) values (?, ?)", clients )
con.commit()

cur.close()
con.close()
