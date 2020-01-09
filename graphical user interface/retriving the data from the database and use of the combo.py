#program for the retriving the user information with thehelp of combo gidget

from tkinter import *
from tkinter.ttk import *
import mysql.connector


cm=mysql.connector.connect(database='practice',user='root',passwd='root')
cur=cm.cursor()
print('The database connection is established successfully')

window=Tk()
window.geometry('500x500')

#creation label and entry field from the in user interface
lab=Label(window,text='rollno',font=('Arial',15))
lab1=Label(window,text='name of the student',font=('Arial',15))
lab2=Label(window,text='department',font=('Arial',15))
lab3=Label(window,text='address',font=('Arial',15))
lab4=Label(window,text='command line',font=('Arial',15))


cur.execute("select * from student")
list1=cur.fetchall()
li=[]
for i in range (len(list1)):
    li.append(list1[i][0])
t=tuple(li)    

com=Combobox(window)
com['value']=t
com.current(0)

rol=Entry(window,width=20)
name=Entry(window,width=20)
dept=Entry(window,width=20)
add=Entry(window,width=20)

def display():
    srol=com.get()
    cur.execute("select * from student where rollno=%s",params=(srol,))
    data=cur.fetchone()
    rol.insert(0,str(data[0]))
    name.insert(0,data[1])
    dept.insert(0,data[2])
    add.insert(0,str(data[3]))
    lab4.configure(text='The outpur of your input is shown')

btn=Button(window,text='register',command=display)



com.grid(column=0,row=0)
lab.grid(row=1,column=0)
lab1.grid(row=2,column=0)
lab2.grid(row=3,column=0)
lab3.grid(row=4,column=0)
lab4.grid(row=5,column=0)
rol.grid(row=1,column=1)
name.grid(row=2,column=1)
dept.grid(row=3,column=1)
add.grid(row=4,column=1)
btn.grid(row=6,column=1)

