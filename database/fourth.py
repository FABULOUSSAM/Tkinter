# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 13:01:06 2020

@author: Shubham
"""

import sqlite3 as sql
conn=sql.connect(".db")
c=conn.cursor()

def create_table():
    c.execute("create table if not exists emp(name text , id number, email text)")
def data_update():
    c.execute("UPDATE emp SET name='xxxx' where id=5959")
    conn.commit()
    c.close()

create_table()
data_update()