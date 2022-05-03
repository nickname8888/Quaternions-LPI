import tkinter
from tkinter import *

W = tkinter.Tk()
W.geometry("1280x720+0+0")
W.configure(background="lightblue")
c = 0


def exec_code():
    global c
    c = c+1
    label1["text"] = c


label1 = Label(W, text="Click the Start Button to update")
label1.place(relx=0.0,
             rely=1.0,
             anchor='sw')
frame = Frame(W, width=1260, height=620,
              highlightbackground="black", highlightthickness=1)
frame.place(x=10, y=10)
label = Label(frame, text="Video").pack()
frame.pack_propagate(False)
b1 = Button(W, text="Start", command=exec_code, pady=10).place(x=570, y=650)
b2 = Button(W, text="Stop", pady=10).place(x=650, y=650)

W.mainloop()
