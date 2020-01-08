import tkinter as tk
import Objects as ob

root=tk.Tk()

height=600
width=800

#Setting up the main frame
canvas=tk.Canvas(root, height=height, width=width)
canvas.pack()

frame=tk.Frame(root,bd='5',bg='grey')
frame.place(relx=0,rely=0,relheight=1,relwidth=1)

#Setting up labels for everything

root.mainloop()