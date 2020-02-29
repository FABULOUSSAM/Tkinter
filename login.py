# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 10:57:30 2020

@author: Shubham
"""

from tkinter import *
root=Tk()
Label(root,text="First Name").grid(row=0)
Label(root,text="Password").grid(row=1)
e1=Entry(root)
e2=Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
var1
Checkbutton(root,text="male",variable=var1).grid(row=2,sticky=W)
submit=Button(text="Submit",command=root.destroy).grid(row=3)
mainloop()