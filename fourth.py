# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:11:13 2020

@author: Shubham
"""

from tkinter import *
root=Tk()
def call_me():
        print("I am called")
        
button=Button(root,text="click me",command=call_me)
button.pack()
button1=Button(root,text="Submit",command=root.destroy)
button1.pack()
root.mainloop()