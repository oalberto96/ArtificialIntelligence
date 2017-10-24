from tkinter import *

root = Tk()

def key(event):
    print("pressed" + repr(event.char))

def callback(event):
    print("clicked at" + str(event.x)+ " " + str(event.y))

canvas= Canvas(root, width=100, height=100)

x = canvas.create_rectangle(50, 25, 150, 75, fill="blue")

canvas.tag_bind(x,"<ButtonPress-1>", callback)
canvas.pack()
root.mainloop()
