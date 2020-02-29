# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:14:21 2020

@author: Shubham
"""

from tkinter import *
root=Tk()
def call_me(event):
    print("I am called")
    
button=Button(root,text="click me")
button.bind("<Button-1>",call_me)
button.pack()
root.mainloop()