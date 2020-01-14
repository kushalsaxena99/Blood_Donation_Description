from tkinter import*
from PIL import ImageTk,Image
import tkinter.messagebox
#import ttkcalendar
import tkSimpleDialog
import sqlite3

#from  CalendarDialog import CalendarDialog,CalendarFrame

from scrollingarea import *
root = Tk()
root.geometry("1366x768+0+0")
root.config(bg="powder blue")
root.title("Blood group")
root.resizable(0, 0)
class CalendarDialog(tkSimpleDialog.Dialog):
    """Dialog box that displays a calendar and returns the selected date"""
    def body(self, m):
        self.calendar = ttkcalendar.Calendar(m)
        self.calendar.pack()

    def apply(self):
        self.result = self.calendar.selection
def home():
    frame1 = Frame(root, width=1366, height=900, bg="cyan")
    frame1.place(x=0, y=0)
    img = ImageTk.PhotoImage(Image.open('project6_800.jpg'))
    Label(frame1, image=img, width="1366", height="768").place(x=0, y=100)
    b1 = Button(frame1, text="ADD", bg="brown", height="2", width="10", bd="5", command=lambda: add(frame1, root))
    b1.place(x=400, y=20)
    b2 = Button(frame1, text="SHOW", bg="brown", height="2", width="10", bd="5", command=lambda: show(frame1, root))
    b2.place(x=900, y=20)


    frame1.mainloop()
def add(frame1,root):
    frame1.destroy()
    frame2=Frame(root,width=1366,height=900,bg="powder blue")

    img = ImageTk.PhotoImage(Image.open('donation.jpg'))
    Label(frame2, image=img, width="1366", height="768").place(x=0, y=5)
    frame2.place(x=0,y=0)

    l2 = Label(frame2, text="Name", font=('arial', 12, 'bold'), width=10)
    l2.place(x=20, y=30)
    l3 = Label(frame2, text="Blood_Group", font=('arial', 12, 'bold'), width=10)
    l3.place(x=20, y=90)
    l4 = Label(frame2, text="Date", font=('arial', 12, 'bold'), width=10)
    l4.place(x=20, y=150)
    l5 = Label(frame2, text="DOB", font=('arial', 12, 'bold'), width=10)
    l5.place(x=20, y=210)
    l6 = Label(frame2, text="Age", font=('arial', 12, 'bold'), width=10)
    l6.place(x=20, y=270)
    l7 = Label(frame2, text="Address", font=('arial', 12, 'bold'), width=10)
    l7.place(x=20, y=330)
    e1 = Entry(frame2, bd=10, font=2, textvariable=StringVar())
    e1.place(x=200, y=20)
    variable = StringVar(frame2)
    variable.set("A+")
    e2 = OptionMenu(frame2, variable, "A+", "A-", "B+", "B-", "AB+", "AB-","O+","O-")
    e2.config(width="30", bd=10)
    e2.place(x=200, y=80)
    #variable=StringVar(frame2)


    e3 =Entry(frame2, bd=10, font=2, textvariable=IntVar())


    e3.place(x=200, y=140)
    global selected_date
    selected_date = StringVar()
    global date
    date = StringVar()

    """en=Entry(screen2,textvariable=selected_date, width="4").place(x=200,y=250)
    Button(screen2,text="Choose a date", command=getdate(screen2,selected_date)).place(x=210,y=250)
"""
    e4 = Entry(frame2, textvariable=selected_date, width=20,font=5,bd=10)
    e4.place(x=200, y=201)
    bn = Button(frame2, text='Choose a date', command=lambda: getdate(frame2), width=10,height=1)
    bn.place(x=357, y=210)
    e5 = Entry(frame2, bd=10, font=2, textvariable=IntVar())
    e5.place(x=200, y=260)
    e6 = Entry(frame2, bd=10, font=2, textvariable=StringVar())
    e6.insert(0, "")
    e6.place(x=200, y=320)
    b2 = Button(frame2, text="SUBMIT", bg="brown", height="2", width="10", bd="5", command=lambda: submit(frame2,root,e1,variable,e3,e4,e5,e6))
    b2.place(x=20, y=400)
    b3 = Button(frame2, text="BACK", bg="brown", height="2", width="10", bd="5", command=lambda: back(frame2, root))
    b3.place(x=195, y=400)
    b4 = Button(frame2, text="RESET", bg="brown", height="2", width="10", bd="5", command=lambda: add(frame1, root))
    b4.place(x=360, y=400)

    frame2.mainloop()
def show(frame1,root):
    a = IntVar()
    b = IntVar()
    c = IntVar()
    d = IntVar()
    e = IntVar()
    f = IntVar()
    g = IntVar()
    h=IntVar()
    frame1.destroy()
    frame3=Frame(root,width=1366,height=768,bg="powder blue")
    frame3.place(x=0,y=0)
    l1=Label(frame3,text="select the blood group",font=("arial",15,'bold'))
    l1.place(x=500,y=0)
    img=ImageTk.PhotoImage(Image.open('project8.jpg'))
    Label(frame3, image=img, width="1366", height="768").place(x=0, y=30)

    c1 = Checkbutton(frame3, text="A+                                           ",variable=a, width=20, height=1, bd=1, bg="white")
    c1.place(x=500, y=60)
    c2 = Checkbutton(frame3, text="A-                                           ",variable=b, width=20, height=1, bd=1, bg="white")
    c2.place(x=500, y=100)
    c3 = Checkbutton(frame3, text="B+                                           ",variable=c, width=20, height=1, bd=1, bg="white")
    c3.place(x=500, y=140)
    c4 = Checkbutton(frame3, text="B-                                           ",variable=d, width=20, height=1, bd=1, bg="white")
    c4.place(x=500, y=180)
    c5 = Checkbutton(frame3, text="AB+                                        ",variable=e, width=20, height=1, bd=1, bg="white")
    c5.place(x=500, y=220)
    c6 = Checkbutton(frame3, text="AB-                                       ",variable=f, width=20, height=1, bd=1, bg="white")
    c6.place(x=500, y=260)
    c7 = Checkbutton(frame3, text="O+                                         ",variable=g, width=20, height=1, bd=1, bg="white")
    c7.place(x=500, y=300)
    c8 = Checkbutton(frame3, text="O-                                         ",variable=h, width=20, height=1, bd=1, bg="white")
    c8.place(x=500, y=340)
    b2 = Button(frame3, text="OK", bg="brown", height="2", width="10", bd="5", command=lambda: ok(frame3,root,a,b,c,d,e,f,g,h))
    b2.place(x=420, y=400)
    b3 = Button(frame3, text="BACK", bg="brown", height="2", width="10", bd="5", command=lambda: back(frame3, root))
    b3.place(x=540, y=400)
    b4= Button(frame3, text="RESET", bg="brown", height="2", width="10", bd="5", command=lambda:show (frame1, root))
    b4.place(x=660, y=400)


    frame3.mainloop()
def submit(frame2,root,e1,variable,e3,e4,e5,e6):
    a = e1.get()
    b = variable.get()
    c = e3.get()
    d = e4.get()
    e = e5.get()
    f = e6.get()

    print(a, b, c, d, e, f)
    con = sqlite3.connect("BLOODDONATION")
    # cur=con.cursor()
    con.execute("create table if not exists test1 (name char[20],bloodgroup char[20],date int[20],dob int[10],age int[20],address char[10])")
    query = "insert into test1 (name,bloodgroup,date,dob,age,address)values('{}','{}',{},'{}',{},'{}')".format(a,b,c,d,e,f)

    i = con.execute(query)
    con.commit()
    m = con.execute("select * from test1")
    print(list(m))
    print("successfully inserted")
    con.close()

    if(a==0 and b==0 and c==0 and d==0 and e==0 and f==0):
        tkinter.messagebox.showinfo("complete", "before submitt completely fill the enrty")
    else:
        tkinter.messagebox.showinfo("successfull","successfully submitted")

def back(frame2,root):
    frame2.destroy()
    home()
def showback(frame3,root):
    frame3.destroy()
    home()
#def showreset(frame3,root):

   # pass
def ok(frame3,root,a,b,c,d,e,f,g,h):
    frame3.destroy()
    frame4=Frame(root,width=1366,height=768,bg="powder blue")
    img=ImageTk.PhotoImage(Image.open('bloodimage6.jpg'))
    Label(frame4,image=img,width=1366,height=768).place(x=0,y=0)
    f1=a.get()
    f2= b.get()
    f3= c.get()
    f4= d.get()
    f5= e.get()
    f6= f.get()
    f7 = g.get()
    f8 = h.get()
    print((f1,f2,f3,f4,f5,f6,f7,f8))
    con=sqlite3.connect("BLOODDONATION")
    frame4.pack()
    scrolling_area = Scrolling_Area(frame4, height=220)
    scrolling_area.place(x=0, y=0)
    table = Table(scrolling_area.innerframe,
                  ["name   ", "bloodgroup  ", "date  ", "dob", "    age   ", "address  "],
                  column_minwidths=[222, 222, 220, 220, 222, 222, 222])
    table.pack(expand=True,fill=X)

    table.on_change_data(scrolling_area.update_viewport)
    #text_area = Text(frame4, bg="white", width=200, height=20, bd=10)
    #text_area.insert(INSERT, "")
    #text_area.place(x=0, y=250)

    if f1==1:
        #tkinter.messagebox.showinfo("information","data will be sucessfullyn retrieve from the database")
        o1=con.execute("select * from Test1 where bloodgroup='A+'")
        con.commit()

        data = []
        for row in o1:
            column = []
            data.append(column)
            for r in row:
                print(r)
                column.append(r)

        table.set_data(data)

    if f2==1:
        o2=con.execute("select * from Test1 where bloodgroup='A-'")
        con.commit()

        data = []
        for row in o2:
            column = []
            data.append(column)
            for r in row:
                column.append(r)

        table.set_data(data)

    if f3==1:
        o3=con.execute("select * from Test1 where bloodgroup='B+' ")
        con.commit()

        data = []
        for row in o3:
            column = []
            data.append(column)
            for r in row:
                column.append(r)

        table.set_data(data)

    if f4==1:
        o4=con.execute("select * from Test1 where bloodgroup='B-'")
        con.commit()

        data = []
        for row in o4:
            column = []
            data.append(column)
            for r in row:
                column.append(r)

        table.set_data(data)

    if f5==1:
        o5=con.execute("select * from Test1 where bloodgroup='AB+'")
        con.commit()

        data = []
        for row in o5:
            column = []
            data.append(column)
            for r in row:
                column.append(r)

        table.set_data(data)

    if f6==1:
        o6=con.execute("select * from Test1 where bloodgroup='AB-'")
        con.commit()

        data = []
        for row in o6:
            column = []
            data.append(column)
            for r in row:
                column.append(r)

        table.set_data(data)

    if f7==1:
        o7=con.execute("select * from Test1 where bloodgroup='O+'")
        con.commit()

        data = []
        for row in o7:
            column = []
            data.append(column)
            for r in row:
                column.append(r)

        table.set_data(data)

    if f8==1:
        o8=con.execute("select * from Test1 where bloodgroup='O-'")
        con.commit()

        data = []
        for row in o8:
            column = []
            data.append(column)
            for r in row:
                column.append(r)


        table.set_data(data)

    if f1==0 and f2==0 and f3==0 and f4==0 and f5==0 and f6==0 and f7==0 and f8==0:
        tkinter.messagebox.showwarning("warning","firstly select the bloodgroup")
    else:
        tkinter.messagebox.showinfo("successfully","successfully fetch the data from the dataabase")

    #b1=Button(frame4, text="SEND MAIL", bd=10, height=1, font=('arial', 8, 'bold'))
    #b1.place(x=20, y=630)

    Button(frame4, text="BACK ", bd=10, height=2, width=11,bg="brown", font=('arial', 8, 'bold'),command=lambda: show(frame4, root)).place(x=900, y=280)
    frame4.mainloop()

def back2(frame4,root):
    frame4.destroy()

def getdate(frame2):
    cd = CalendarDialog(frame2)
    result = cd.result
    selected_date.set(result.strftime("%d-%m-%Y"))



home()












