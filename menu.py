# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:19:36 2020

@author: Shubham
"""

from tkinter import *
def nothing():
    print("I am Nothing")
root=Tk()

main_menu=Menu(root)
root.config(menu=main_menu)

filemenu=Menu(main_menu) 

main_menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)

helpmenu=Menu(main_menu)

main_menu.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="About",command=nothing)
root.mainloop()