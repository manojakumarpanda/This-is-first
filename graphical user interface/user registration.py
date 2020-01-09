#program for the usre registriation for  the employee:

from tkinter import *
import mysql.connector as mc

cm=mc.connect(database='practice',user='root',password='root')
cur=cm.cursor()
print('The database connection established')

window=Tk()
window.geometry('599x699')
window.title('user registration page')

#this field is for creatio of labels
lab=Label(window,text='User_id',font=('Arial',20))
lab1=Label(window,text='username',font=('Arial',20))
lab2=Label(window,text='password',font=('Arial',20))
lab3=Label(window,text='contact_number',font=('Arial',20))
lab4=Label(window,text='registration page',font=('Arial',20),bg='yellow')
text=Entry(window,width=20)
text1=Entry(window,width=20)
text2=Entry(window,width=20,show='*')
text3=Entry(window,width=11)


#registration of the student function
def register():
    user_id=text.get()
    username=text1.get()
    password=text2.get()
    contact=text3.get()
    cur.execute("insert into user_information values(%s,%s,%s,%s)",params=(user_id,username,password,contact))
    cm.commit()
    lab4.configure(text='User registration is success !!',font=('Arial',20),bg='red',fg='yellow')
    


#button creatio for the registration
btn=Button(window,text='register',font=('Arial',10),fg='blue',bg='yellow',command=register)


#defining position for the lable and buttons                
lab.grid(row=1,column=0)
lab1.grid(row=2,column=0)
lab2.grid(row=3,column=0)
lab3.grid(row=4,column=0)
lab4.grid(column=3,row=5)
text.grid(row=1,column=1)
text1.grid(row=2,column=1)
text2.grid(row=3,column=1)
text3.grid(row=4,column=1)
btn.grid(row=6,column=5)
