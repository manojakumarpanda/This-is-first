#progrmas for the input in the graphical user interfacae and perform addition operation

import tkinter as tk

window=tk.Tk()
window.geometry('500x500')


la=tk.Label(window,text='Enter the first value:',font=('times roman',10))
la.grid(column=0,row=5)
text=tk.Entry(window,width=30)
text.grid(column=21,row=5)


la1=tk.Label(window,text='Enter the second value:',font=('times roman',10))
la1.grid(column=0,row=7)
text1=tk.Entry(window,width=30)
text1.grid(column=10,row=7)

btn=tk.Button(window,text='+',bg='green',fg='red')
btn.grid(column=10,row=9)
