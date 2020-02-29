from tkinter import *
root=Tk()
lab=Label(root,text="Nothing to do")
lab.pack()
w=Button(root,text="stop",width=13,bg="yellow",font="Times",command=root.destroy)
w.pack()
root.geometry('200x150')
root.mainloop()