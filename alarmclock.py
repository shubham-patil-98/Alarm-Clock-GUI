from tkinter import *
import time
import datetime
from tkinter import messagebox
from playsound import playsound

root=Tk()
root.geometry("500x300")
root.title("alarm clock")

def alarm():
    global hours_label,minutes_label
    h=hours_label.get()
    m=minutes_label.get()
    while(1):
        if (int(h)==datetime.datetime.now().hour and int(m)==datetime.datetime.now().minute):
            playsound("alarm.mp3")
            messagebox.showinfo("ALARM","Hurry up .... It's time!!!!")
            break

label=Label(root,text="ALARM CLOCK",fg="black",font="vandetta 18 bold",relief=GROOVE,bg="yellow").pack()
hours=Label(root,text="At what hour do you want alarm?",font="vandetta 10 bold",relief=GROOVE,fg="black",bg="light green").place(x=30,y=50)
minutes=Label(root,text="At what minute do you want alarm?",font="vandetta 10 bold",relief=GROOVE,fg="black",bg="light green").place(x=30,y=100)
label1=Label(root,text="TKINTER",fg="black",font="vandetta 18 bold",relief=GROOVE,bg="yellow").pack(side=BOTTOM)

hours_label=IntVar()
minutes_label=IntVar()

entry1=Entry(root,textvariable=hours_label,font="vandetta 10 bold",relief=GROOVE,borderwidth=3).place(x=300,y=50)
entry2=Entry(root,textvariable=minutes_label,font="vandetta 10 bold",relief=GROOVE,borderwidth=3).place(x=300,y=100)

button=Button(root,text="Click here to set the alarm",command=alarm,bg="yellow",fg="black",font="vandetta 10 bold",relief=GROOVE).place(x=200,y=150)

root.mainloop()