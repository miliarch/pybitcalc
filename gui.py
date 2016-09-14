#!/usr/bin/env python3
import tkinter

def stop_prog(e):
    root.destroy()

root = tkinter.Tk()

button1 = tkinter.Button(root, text="Hello World! Click to close.")
button1.pack()
button1.bind('<Button-1>', stop_prog)

root.mainloop()