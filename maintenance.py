from tkinter import *
from tkinter import ttk
from datetime import datetime


GUI = Tk()

GUI.geometry('1300x600')
GUI.title('โปรแกรมซ่อมบำรุง v.0.0.1 by Loong') 

F1 = Frame(GUI)
F1.place(x=50,y=50)

#1
L = Label(F1,text='อุปกรณ์/เครื่องจักร',font=(None,20)).pack()
#2
v_machine = StringVar()
E = Entry(F1,textvariable=v_machine ,font=(None,20)).pack()

#3
L = Label(F1,text='อาการเสีย',font=(None,20)).pack()
#4
v_problem = StringVar()
E = Entry(F1,textvariable=v_problem, font=(None,20)).pack()

#5
L = Label(F1,text='ผู้แจ้งซ่อม',font=(None,20)).pack()
#6
v_reporter = StringVar()
E = Entry(F1,textvariable=v_reporter ,font=(None,20)).pack()

#7

def Save():
    machine = v_machine.get()
    problem = v_problem.get()
    reporter = v_reporter.get()
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(machine, problem, reporter)
    with open('log.txt','a',encoding='utf-8') as file:
        text = machine +','+ problem +','+ reporter +','+ date + '\n'
        file.write(text)
    v_machine.set('')
    v_problem.set('')
    v_reporter.set('')

    # clear table
    table.delete(*table.get_children())

    # Insert data from log.txt
    with open('log.txt','r',encoding='utf-8') as file:
        text = file.readlines()
        print(text)
        for t in text:
            data = t.strip().split(',')
            table.insert('','end',values=data)
    
B = Button(F1, text='บันทึก',command=Save).pack(ipadx=50,ipady=30,pady=20)


###############################
F2 = Frame(GUI)
F2.place(x=400,y=50)
header = ['เครื่องจักร/อุปกรณ์','อาการ','ผู้แจ้งซ่อม','วันแจ้งซ่อม']

table = ttk.Treeview(F2, columns=header,show='headings',height=20)
table.pack()

#show header
for h in header:
    table.heading(h,text=h)

##########LOAD DATA TO TABLE############
with open('log.txt','r',encoding='utf-8') as file:
    text = file.readlines()
    print(text)
    for t in text:
        data = t.strip().split(',')
        table.insert('','end',values=data)


GUI.mainloop()
