# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 10:51:21 2020

@author: Shubham
"""

from tkinter import *
root=Tk()

lab=Label(root,text="Here is the label ",bg="blue",fg="White")
lab.pack()
w=Button(root,text="Submit",command=root.destroy)
w.pack()
root.mainloop()