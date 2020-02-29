# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:02:15 2020

@author: Shubham
"""

from tkinter import *
root=Tk()

c1=Checkbutton(root,text="Male").grid(row=0,sticky=E)

c2=Checkbutton(root,text="Female").grid(row=1,sticky=E)
root.mainloop()