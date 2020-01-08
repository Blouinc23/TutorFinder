import tkinter as tk


root=tk.Tk()

height=500
width=600

def test_function(entry):
    text='This is the entry:',entry
    label['text']=str('this is the entry ')+str(entry)

canvas=tk.Canvas(root,height=height,width=width)
canvas.pack()

background_image=tk.PhotoImage(file='landscape.png')
background_label=tk.Label(root,image=background_image)
background_label.place(relheigdht=1, relwidth=1)

frame=tk.Frame(root, bg='#42c2f5',bd='5')
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry=tk.Entry(frame, font='40')
entry.place(relwidth=0.65,relheight=1)

button=tk.Button(frame,text="Get Weather",font='40',command=lambda: test_function(entry.get()))
button.place(relx=0.7,relwidth=0.3,relheight=1)

lower_frame=tk.Frame(root,bg='#42c2f5',bd='10')
lower_frame.place(relx=0.5,rely=0.25,relheight=0.6,relwidth=0.75,anchor='n')

label=tk.Label(lower_frame,font='40')
label.place(relwidth=1,relheight=1)







root.mainloop()
