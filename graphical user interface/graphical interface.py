#program for the graphical user interface for creation of window
import tkinter as tk

window=tk.Tk()
window.geometry('500x500')

l1=tk.Label(window,text='hello this is first tkinter programs',font=('times roman',20),fg='red',bg='yellow')
l1.grid(column=0,row=0)

l2=tk.Label(window,text='Pyhton is a programming language:')
l2.grid(column=1,row=1)


l3=tk.Label(window,text='Python is a scripting language::',font=('kalinga',20))
l3.grid(column=0,row=2)

#l4=tk.Label(window,image='first.JPEG')
#l4.grid(column=0,row=4)

text=tk.Entry(window,width=20)
text.grid(column=1,row=5)

lbl=tk.Label(window,text='hello' ,font=('Arial',20))
lbl.grid(column=3,row=5)


def display():
    lbl.configure(text='button clicked!!')


btn=tk.Button(window,text='click me',command=display)
btn.grid(column=3,row=4)



