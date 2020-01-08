import tkinter as tk
import Objects


root=tk.Tk()

height=1000
width=1000
def get_days(list):
    for day in list.curselection():
        if day == 0:
            print('day 0')
        if day == 1:
            print('day 1')
        if day == 2:
            print('day 2')
        if day == 3:
            print('day 3')
        if day == 4:
            print('day 4')
        if day == 5:
            print('day 5')
        if day == 6:
            print('day 6')

def create_timeslots(Day,xloc,yloc):
    #Xlocs follow the following order 0.5, 0.63, 0.83, 0.73, 0.92
    #Yloc is a constant 0.35
    entryw=0.09
    lbw=0.15
    lb1_width=0.18
    lb1 = tk.Label(frame, text=Day, font=('Arial', 12), relief='sunken')
    lb1.place(relx=xloc, rely=yloc, relwidth=lb1_width, relheight=0.05)

    lb2= tk.Label(frame, text='Start:', font=('Arial', 12), relief='sunken')
    lb2.place(relx=xloc+lb1_width, rely=yloc, relwidth=lbw, relheight=0.05)

    en1 = tk.Entry(frame, font=('Arial', 10), bd='5', relief='sunken')
    en1.place(relx=xloc + 1*lbw+lb1_width, rely=yloc, relwidth=lbw, relheight=0.05)

    lb3 = tk.Label(frame, text='Stop:', font=('Arial', 12), relief='sunken')
    lb3.place(relx=xloc+2*lbw+lb1_width, rely=yloc, relwidth=lbw, relheight=0.05)

    en2 = tk.Entry(frame, font=('Arial', 10), bd='5', relief='sunken')
    en2.place(relx=xloc+3*lbw+lb1_width, rely=yloc, relwidth=lbw, relheight=0.05)


canvas=tk.Canvas(root,height=height,width=width)
canvas.pack()

frame=tk.Frame(root,bd='5')
frame.place(relx=0,rely=0,relheight=1,relwidth=1)

##Setting Up the Labels to Get the Tutors information inputted
lb_NewTutor=tk.Label(frame,text='Add Tutor',font=('Arial', 18),relief='sunken')
lb_NewTutor.place(relx=0.45,rely=0.1,relheight=0.05, relwidth=0.25,anchor='center')

lb_tutorname=tk.Label(frame,text='Tutor Name:',font=('Arial',12),anchor='center')
lb_tutorname.place(relx=0,rely=0.15,relheight=0.05,relwidth=0.20)

lb_tutorhours=tk.Label(frame,text='Preffered Hours:',font=('Arial',12),anchor='center')
lb_tutorhours.place(relx=0,rely=0.21,relheight=0.05,relwidth=0.25)

lb_avail=tk.Label(frame,text='Availability',font=('Arial',16),relief='sunken')
lb_avail.place(relx=0.32,rely=0.28,relheight=0.05,relwidth=0.25)

##Setting up entry box for the name
en_tutorname=tk.Entry(frame,font=('Arial',10),bd='5',relief='sunken')
en_tutorname.place(relx=0.2,rely=0.15,relheight=0.05,relwidth=0.45)

en_tutorhours=tk.Entry(frame,font=('Arial',10),bd='5',relief='sunken')
en_tutorhours.place(relx=0.25,rely=0.21,relheight=0.05,relwidth=0.4)

#Creating avail listbox button for testing purposes
bt_submit_avail=tk.Button(frame,text='Submit Availability Changes',command=lambda: get_days(list_avail))
bt_submit_avail.place(relx=0.25,rely=0.73)


#Creating the Listbox frame
avail_frame=tk.Frame(frame,bd='5',bg='white')
avail_frame.place(relx=0.25,rely=0.9,relheight=0.275,relwidth=0.35)

#Setting up the listbox of Subjects
subjects=['Geometry','Spanish','English','History','Math','Calculus','Writing']
list_subj=tk.Listbox(avail_frame,bg='grey',bd='6',selectmode='multiple',relief='sunken')
for item in range(7):
    list_subj.insert('end',subjects[item])
list_subj.place(relx=0,rely=0,relwidth=1,relheight=1)

avail_days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
for i in range(7):
    create_timeslots(avail_days[i],0.01,0.35+0.05*i)


print(Objects.FindTutor('Math','25/12/2019',1830))
root.mainloop()