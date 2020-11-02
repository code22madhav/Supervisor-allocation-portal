from tkinter import *

# creating window and setting its geometry and title
root = Tk()
root.geometry('500x400+500+200')
root.title('supervisor_allocation_portal_for_LPU')


def login():
    login = Tk()
    login.geometry('500x400+500+200')
    login.title('login_page')

    name_var = StringVar()
    username_label = Label(login, text='UserName').pack()
    entry1 = Entry(login, width=20, textvariable=name_var).pack()

    pass_var = StringVar()
    pass_label = Label(login, text='Password').pack()
    entry2 = Entry(login, width=20, textvariable=pass_var).pack()

    btn4 = Button(login, text='login', width=30, height=3).pack()

    btn5 = Button(login, text='NewUser', width=30, height=3, command=newuser).pack()


def newuser():
    newuser = Tk()
    newuser.geometry('500x400+500+200')
    newuser.title('Newuser')

    name_label = Label(newuser, text='Name').pack()
    name_var = StringVar()
    name_entry = Entry(newuser, width=20, textvariable=name_var).pack()

    Reg_label = Label(newuser, text='Reg.No').pack()
    Reg_var = IntVar()
    Reg_entry = Entry(newuser, width=20, textvariable=Reg_var).pack()

    spec_label = Label(newuser, text='Specialization').pack()
    specialization = StringVar()
    spec_entry = Entry(newuser, width=20, textvariable=specialization).pack()

    mobile_label = Label(newuser, text='Mobile').pack()
    mobile = StringVar()
    mobile_entry = Entry(newuser, width=20, textvariable=mobile).pack()

    email_label = Label(newuser, text='e-mail').pack()
    email = StringVar()
    email_entry = Entry(newuser, width=20, textvariable=email).pack()

    btn6 = Button(newuser, text='Register', width=30, height=3).pack()


def supervisor():
    supervisor = Tk()
    supervisor.geometry('500x400+500+200')
    supervisor.title('New_User_Supervisor')

    naam_label = Label(supervisor, text='Name').pack()
    naam = StringVar()
    naam_entry = Entry(supervisor, width=20, textvariable=naam).pack()

    uid_label = Label(supervisor, text='UID').pack()
    uid = StringVar()
    uid_entry = Entry(supervisor, width=20, textvariable=uid).pack()

    specialist_label = Label(supervisor, text='Specialization').pack()
    specialist = StringVar()
    specialist_entry = Entry(supervisor, width=20, textvariable=specialist).pack()


    mail_label = Label(supervisor, text='Email-ID').pack()
    mail = StringVar()
    mail_entru = Entry(supervisor, width=20, textvariable=mail).pack()

    phone_label = Label(supervisor, text='Mobile').pack()
    phone = StringVar()
    phone_entry = Entry(supervisor, width=20, textvariable=phone).pack()

    btn7 = Button(supervisor, text='Register', width=30, height=3).pack()


def request():
    request = Tk()
    request.geometry('500x400+500+200')
    request.title('request_for_supervisor')

    btn8 = Button(request, text='Login', width=30, height=3, command=login).pack()

    btn9 = Button(request, text='Newuser', width=30, height=3, command=supervisor).pack()

    btn10 = Button(request, text='Open Hours', width=30, height=3,).pack()

    btn11 = Button(request, text='Select Students', width=30, height=3).pack()







btn1 = Button(root, text='Login', width=30, height=3, command=login).pack()
btn2 = Button(root, text='New User', width=30, height=3, command=newuser).pack()
btn3 = Button(root, text='Request for Supervisor',width=30, height=3, command=request).pack()


root.mainloop()

