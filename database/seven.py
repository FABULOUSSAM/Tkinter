# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 13:21:37 2020

@author: Shubham
"""

import sqlite3 as sql
conn=sql.connect(".db")
c=conn.cursor()


def create_table():
        c.execute("create table if not exists employee(name text , id number)")
def data_delete():
    c.execute("DELETE FROM employee WHERE name='first'")
    conn.commit()
    c.close()
create_table()
data_delete()