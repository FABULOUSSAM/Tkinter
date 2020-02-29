# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:06:18 2020

@author: Shubham
"""


from tkinter import *
from tkinter.ttk import Combobox 
root=Tk()
V=["SAM","Chirag","Shreyash"]
com=Combobox(root,values=V)
com.pack()
root.mainloop()