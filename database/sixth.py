# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 13:16:22 2020

@author: Shubham
"""

import sqlite3 as sql
conn=sql.connect(".db")
c=conn.cursor()

def create_table():
        c.execute("create table if not exists employee(name text , id number)")

def data_entry():
    c.execute("insert into employee values ('first',5959)")
    c.execute("insert into employee values ('second',1234)")
    c.execute("insert into employee values ('third',6789)")
    conn.commit()
    c.close()
    
create_table()
data_entry()