# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:41:01 2020

@author: Shubham
"""

from tkinter import *
from tkinter import messagebox
def call_me():
    messagebox.showwarning("UnSuccessful","Installion complted")

root=Tk()
b=Button(root,text="Message",command=call_me,bg="red")
b.pack()

root.geometry("250x250")
root.mainloop()

