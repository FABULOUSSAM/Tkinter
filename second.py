# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 10:38:52 2020

@author: Shubham
"""

from tkinter import *
root=Tk()

frame=Frame(root,width=3000,height=5000,bg="Black")
button1=Button(frame,text="button1",bg="Yellow")
button2=Button(frame,text="button2",bg="Blue")
button3=Button(frame,text="button3",bg="Green")
button1.pack(side="left")
button2.pack(side="left")
button3.pack(side="left")
frame.pack()

bottomframe=Frame(root,width=3000,height=5000,bg="Black")
button4=Button(bottomframe,text="submit",bg="RED",command=root.destroy)
button4.pack(side="bottom")
bottomframe.pack()
root.mainloop()