from tkinter import *

c = 0

def exec_code():
    print("Running code...")
    global c
    c = c+1
    print(c)

root = Tk()
root.geometry("1400x700")

frame1 = Frame(root)
frame2 = Frame(root)
root.title("tkinter frame")

label = Label(frame1, text="Video", justify=LEFT)
label.pack(side=LEFT)

# hi_there = Button(frame2, text="say hi~", command=say_hi)
# hi_there.pack()
b1 = Button(root, text="Start", command=exec_code, pady=10).place(x=640, y=600)
b2 = Button(root, text="Stop", pady=10).place(x=710, y=600)

frame1.pack(padx=1, pady=1)
frame2.pack(padx=10, pady=10)

root.mainloop()
