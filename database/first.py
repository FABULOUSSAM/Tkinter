# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:24:26 2020

@author: Shubham
"""

import sqlite3 as sql
conn=sql.connect(".db")
c=conn.cursor()
def create_table():
    c.execute("create table if not exists emp(name text , id number)")

def data_entry():
    c.execute("insert into emp values ('SAM',5959)")
    c.execute("insert into emp values ('Chirag',1234)")
    c.execute("insert into emp values ('Shreyash',6789)")
    conn.commit()
    c.close()
    
create_table()
data_entry()
