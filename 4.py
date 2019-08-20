import pymysql
from tkinter import *
import tkinter.messagebox
kint=Tk()
global kin1,kin2
my=pymysql.connect(host='localhost',user='root',password='karan',db='train')
con=my.cursor()
global e1,e2,e3,e4,e5
def fun6():
    global e1,e2
    if(e1.get()=='123456789' and e2.get()=='2/21'):
        tkinter.messagebox.showinfo("transaction complete ")
        kint2.quit()
        kint2.destroy()
    else:
        tkinter.messagebox.showinfo("transaction failed ")
def fun5():
    global e1,e2,e3,e4,e5,kint2,kint1
    kint1.quit()
    kint1.destroy()
    kint2=Tk()
    Label(kint2,text="enter credit card numder").grid(row=0)
    Label(kint2,text="enter credit card expiry date").grid(row=1)
    e1=Entry(kint2)
    e2=Entry(kint2)
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    Button(kint2,text='enter',command=fun6).grid(row=4,column=0)
def fun4():
    global e1,e2,e3,e4,e5,kint1,kint2
    a=e5.get()
    b=int(a)
    k=con.execute('select * from traininfo;')
    data=con.fetchall()
    l=[]
    for i in range(len(data)):
        if(data[i][1]==e1.get() and data[i][2]==e2.get() and data[i][3]==e3.get() and data[i][4]==e4.get() and data[i][5]>=b):
            l.append(data[i][0])
            c=i
    print(l)
         #tkinter.messagebox.showinfo("available trains ",data[i][0])
    y=tuple(l)
    var=StringVar(kint1)
    var.set(l[0])
    w=OptionMenu(kint1,var,*y)
    w.grid(row=6,column=6)
    Button(kint1,text='book',command=fun5).grid(row=5,column=0)
    u=con.execute("select slipper from traininfo where name='{}'".format(var.get()))
    a=con.fetchall()
    e=int(a[0][0])-int(b)
    u=con.execute("update traininfo set slipper={} where name= '{}'".format(e,var.get()))
def fun3():
    global kint1
    kint1=Tk()
    Label(kint1,text="Source").grid(row=0)
    Label(kint1,text="Destination").grid(row=1)
    Label(kint1,text="Date of arrival").grid(row=2)
    Label(kint1,text="time of arrival").grid(row=3)
    Label(kint1,text="Number of passenger").grid(row=4)
    global e1,e2,e3,e4,e5
    e1=Entry(kint1)
    e2=Entry(kint1)
    e3=Entry(kint1)
    e4=Entry(kint1)
    e5=Entry(kint1)
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    e3.grid(row=2,column=1)
    e4.grid(row=3,column=1)
    e5.grid(row=4,column=1)
    Button(kint1,text='enter',command=fun4).grid(row=5,column=0)
def fun2():
    kint.quit()
    kint.destroy()
    fun3()
def fun1():
    a=e1.get()
    b=e2.get()
    k=con.execute('select * from pinfo;')
    data=con.fetchall()
    f=0
    for i in range(len(data)):    
        if(data[i][0]==a and data[i][1]==b):
            f=1
    if f==1:
        tkinter.messagebox.showinfo("welcome ",a)
        #kint.destroy()
        fun2()
    else:
        tkinter.messagebox.showinfo("Information incorrect ")

Label(kint,text="ID").grid(row=0)
Label(kint,text="password").grid(row=1)
e1=Entry(kint)
e2=Entry(kint)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
Button(kint,text='enter',command=fun1).grid(row=3,column=0)
Button(kint,text='quit',command=fun2).grid(row=3,column=1)
