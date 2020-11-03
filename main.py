from tkinter import *

# creating window and setting its geometry and title
root = Tk()
root.geometry('800x500+300+100')
root.config(bg="black")
root.title('supervisor_allocation_portal_for_LPU')


def login():
    login = Tk()
    login.geometry('800x500+300+100')
    login.config(bg="skyblue")
    login.title('login_page')

    name_var = StringVar()
    username_label = Label(login, width=10, height=2,text='UserName').grid(row=0,column=2,padx=30,pady=15)
    entry1 = Entry(login,width=20,textvariable=name_var).grid(row=0,column=3)

    pass_var = StringVar()
    pass_label = Label(login,width=10,height=2, text='Password').grid(row=1,column=2, pady=15)
    entry2 = Entry(login, width=20, textvariable=pass_var).grid(row=1,column=3)

    btn4 = Button(login, text='register', width=20, height=3, command=register).grid(row=3,column=2,padx=50,pady=20)

    btn5 = Button(login, text='NewUser', width=20, height=3, command=newuser).grid(row=3,column=3,padx=2)


def newuser():
    newuser = Tk()
    newuser.geometry('800x500+300+100')
    newuser.title('Newuser')
    newuser.config(bg="blue")

    name_label = Label(newuser, text='Name').grid(row=0,column=2,padx=30,pady=15)
    name_var = StringVar()
    name_entry = Entry(newuser, width=20, textvariable=name_var).grid(row=0,column=3,padx=0,pady=15)

    Reg_label = Label(newuser, text='Reg.No').grid(row=1,column=2,padx=30,pady=15)
    Reg_var = IntVar()
    Reg_entry = Entry(newuser, width=20, textvariable=Reg_var).grid(row=1,column=3,padx=0,pady=15)

    mobile_label = Label(newuser, text='Mobile').grid(row=3,column=2,padx=30,pady=15)
    mobile = StringVar()
    mobile_entry = Entry(newuser, width=20, textvariable=mobile).grid(row=3,column=3,padx=0,pady=15)

    email_label = Label(newuser, text='e-mail').grid(row=2,column=2,padx=30,pady=15)
    email = StringVar()
    email_entry = Entry(newuser, width=20, textvariable=email).grid(row=2,column=3,padx=0,pady=15)

    spec_label = Label(newuser, text='Specialization').grid(row=4, column=2, padx=30, pady=15)
    specialization = StringVar()
    spec_entry = Entry(newuser, width=20, textvariable=specialization).grid(row=4, column=3, padx=0, pady=15)

    btn6 = Button(newuser, text='Register', width=20, height=2, command=register_student).grid(row=5,column=3,pady=15)


def supervisor():
    supervisor = Tk()
    supervisor.geometry('800x500+300+100')
    supervisor.title('New_User_Supervisor')
    supervisor.config(bg="orange")

    naam_label = Label(supervisor, text='Name').grid(row=0, column=2, padx=30, pady=15)
    naam = StringVar()
    naam_entry = Entry(supervisor, width=20, textvariable=naam).grid(row=0, column=3, padx=0, pady=15)

    uid_label = Label(supervisor, text='UID').grid(row=1, column=2, padx=30, pady=15)
    uid = IntVar()
    uid_entry = Entry(supervisor, width=20, textvariable=uid).grid(row=1, column=3, padx=0, pady=15)

    specialist_label = Label(supervisor, text='Specialization').grid(row=2, column=2, padx=30, pady=15)
    specialist = StringVar()
    specialist_entry = Entry(supervisor, width=20, textvariable=specialist).grid(row=2, column=3, padx=0, pady=15)

    mail_label = Label(supervisor, text='Email-ID').grid(row=3, column=2, padx=30, pady=15)
    mail = StringVar()
    mail_entru = Entry(supervisor, width=20, textvariable=mail).grid(row=3, column=3, padx=0, pady=15)

    phone_label = Label(supervisor, text='Mobile').grid(row=4, column=2, padx=30, pady=15)
    phone = IntVar()
    phone_entry = Entry(supervisor, width=20, textvariable=phone).grid(row=4, column=3, padx=0, pady=15)

    btn7 = Button(supervisor, text='Register', width=30, height=3, command=register_supervisor).grid(row=5,column=3,pady=15)


def request():
    request = Tk()
    request.geometry('800x500+300+100')
    request.title('request_for_supervisor')
    request.config(bg="purple")

    btn8 = Button(request, text='Login', width=30, height=3, command=login).pack(padx=10, pady=10)

    btn9 = Button(request, text='Newuser', width=30, height=3, command=supervisor).pack(padx=10, pady=10)

    btn10 = Button(request, text='Open Hours', width=30, height=3, command=openhours).pack(padx=10, pady=10)

    btn11 = Button(request, text='Select Students', width=30, height=3, command=selectstudents).pack(padx=10, pady=10)

def register_student():
    register_student = Tk()
    register_student.geometry('800x500+300+100')
    register_student.title('register_student')
    register_student.config(bg='pink')

    print1 = Label(register_student, width=30, height=3, text='YOU ARE REGISTERED AS STUDENT').pack()


def register_supervisor():
    register_supervisor = Tk()
    register_supervisor.geometry('800x500+300+100')
    register_supervisor.title('register_supervisor')
    register_supervisor.config(bg='brown')
    print2 = Label(register_supervisor, width=30, height=3, text='YOU ARE REGISTERED AS SUPERVISOR ').pack()


def register():
    register = Tk()
    register.geometry('800x500+300+100')
    register.title('register')
    register.config(bg='cyan')

    print5 = Label(register, width=30, height=3, text='YOU ARE REGISTERED').pack()


def openhours():
    openhours = Tk()
    openhours.geometry('800x500+300+100')
    openhours.title('openhours')
    openhours.config(bg='magenta')

    print4 = Label(openhours, width=30, height=3, text='OPENING HOUR    09:00 AM').pack()
    print5 = Label(openhours, width=30, height=3, text='CLOSING HOUR    05:00 PM').pack()

    # btn12 = Button(openhours, text='BACK', width=30, height=3, command='request').pack(padx=10, pady=10)


def selectstudents():
    selectstudents = Tk()
    selectstudents.geometry('800x500+300+100')
    selectstudents.title('select_students')
    selectstudents.config(bg='red')

    print5 = Label(selectstudents, width=30, height=3, text='STUDENTS ARE ABSENT').pack()


btn1 = Button(root, text='Login', width=30, height=3, command=login).pack(padx=10, pady=10)
btn2 = Button(root, text='New User',width=30, height=3,command=newuser).pack(padx=10, pady=10)
btn3 = Button(root, text='Request for Supervisor',width=30, height=3, command=request).pack(padx=10, pady=10)

root.mainloop()

