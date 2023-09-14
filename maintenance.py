from tkinter import *
from datetime import datetime

GUI = Tk()
GUI.geometry('500x400')
GUI.title('โปรแกรมซ่อมบำรุง v.0.0.1 by Loong') 

#1
L = Label(GUI,text='อุปกรณ์/เครื่องจักร',font=(None,20)).pack()
#2
v_machine = StringVar()
E = Entry(GUI,textvariable=v_machine ,font=(None,20)).pack()

#3
L = Label(GUI,text='อาการเสีย',font=(None,20)).pack()
#4
v_problem = StringVar()
E = Entry(GUI,textvariable=v_problem, font=(None,20)).pack()

#5
L = Label(GUI,text='ผู้แจ้งซ่อม',font=(None,20)).pack()
#6
v_reporter = StringVar()
E = Entry(GUI,textvariable=v_reporter ,font=(None,20)).pack()

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
    
B = Button(GUI, text='บันทึก',command=Save).pack(ipadx=50,ipady=30,pady=20)


GUI.mainloop()
