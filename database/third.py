# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:55:21 2020

@author: Shubham
"""

import sqlite3 as sql
conn=sql.connect(".db")
c=conn.cursor()

def create_table():
    c.execute("create table if not exists emp(name text , id number)")
def data_drop():
    c.execute("drop table emp")
    conn.commit()
    c.close()
create_table()
data_drop()