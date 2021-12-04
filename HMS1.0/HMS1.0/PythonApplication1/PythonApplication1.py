from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3

def open_login():

    purpose = ["Paitent", "Doctor"]
    purpose_var = StringVar()

    def database():
        email = email_input.get()
        password = password_input.get()
        purpose = purpose_var.get()
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        if purpose_var.get() == "Doctor":
            cursor = conn.execute('SELECT * from Doctors where Email_ID="%s" and Password="%s"'%(email,password))
        else:
            cursor = conn.execute('SELECT * from Paitent where Email_ID="%s" and Password="%s"'%(email,password))

        if cursor.fetchone():
            messagebox.showinfo("Success","Login Successful", parent=loginpage)
            loginpage.destroy()
        else:
            messagebox.showerror("Error","Email ID/ Password is Invalid", parent = loginpage)

    def login_act(input):
        if email_input.get()=="":
            messagebox.showerror("Error","Email ID can't be Empty", parent = loginpage)
        elif password_input.get()=="":
            messagebox.showerror("Error","Password can't be Empty", parent = loginpage)
        elif purpose_var.get()=="":
            messagebox.showerror("Error","Password can't be Empty", parent = loginpage)
        else:
            database()
      

    loginpage = Toplevel(root)
    loginpage.geometry("750x650")
    loginpage.title("Login Page")
    login_frame = Frame(loginpage, bg = "#037ef3")
    login_frame.place(x = 0, y = 0, width = 750, height = 650)
    header=Label(login_frame, text="Login",font=('Poppins Bold',20), fg="white",bg='#037ef3')
    header.place(relx=0.5, rely= 0.01, anchor = 'n')
    input = Frame(login_frame, bg = "#037ef3")
    input.place(relx = 0.5, rely = 0.5, anchor = 'center', width = 500, height = 500)
    email=Label(input, text="Email ID:",font=('Poppins Bold',13), fg="white",bg='#037ef3')
    email.place(relx=0.1, rely= 0.1, anchor = 'nw')
    email_input=Entry(input, font=("Poppins Regular",10),fg = 'black', bg='#00c16e', relief = GROOVE)
    email_input.place(relx = 0.1, rely = 0.16,anchor = 'nw', width = 400)
    password=Label(input, text="Password:",font=('Poppins Bold',13), fg="white",bg='#037ef3')
    password.place(relx=0.1, rely= 0.26, anchor = 'nw')
    password_input= tk.Entry(input, show = '*', font=('Poppins Regular',10), fg = 'black', bg='#00c16e', relief = GROOVE)
    password_input.place(relx = 0.1, rely = 0.32,anchor = 'nw', width = 400)
    purposelbl= Label(input, text="Purpose:",font=('Poppins Bold',13), fg="white",bg='#037ef3')
    purposelbl.place(relx=0.1, rely= 0.4, anchor = 'nw')
    get_purpose = OptionMenu(input, purpose_var, *purpose)
    get_purpose.config(width = 20, font=('Poppins Regular',10), bd = 0, fg = 'black', bg='#00c16e', relief = GROOVE)
    get_purpose.pack()
    get_purpose.place(relx=0.1, rely= 0.46, anchor = 'nw')
    lbl_login = Label(login_frame, text = "Login", font = ("Poppins Bold", 15), padx = 20, relief = GROOVE, fg = "white", bg = "#00c16e", cursor = "hand2")
    lbl_login.pack()
    lbl_login.bind("<Button-1>", lambda e: login_act(input))
    lbl_login.place(relx = 0.5 , rely = 0.6, anchor = 'n')
    already_register=Label(login_frame, text="Haven't Registerd?",font=('Poppins Bold',13), fg="white",bg='#037ef3')
    already_register.place(relx=0.5, rely= 0.68, anchor = 'n')
    lbl_register = Label(login_frame, text = "Register", font = ("Poppins Bold", 15), padx = 10, relief = GROOVE, fg = "white", bg = "#00c16e", cursor = "hand2")
    lbl_register.pack()
    lbl_register.bind("<Button-1>", lambda e: [loginpage.destroy(), open_register()])
    lbl_register.place(relx = 0.5 , rely = 0.75, anchor = 'n')

def open_register():

    genders = ["Male", "Female", "Others"]
    gender_var = StringVar()

    purpose = ["Paitent", "Doctor"]
    purpose_var = StringVar()

    def database():
        name = name_input.get()
        email = email_input.get()
        contact = contact_input.get()
        password = password_input.get()
        gender = gender_var.get()
        purpose = purpose_var.get()

        conn = sqlite3.connect('database.db')
        with conn:
            cursor=conn.cursor()

        if purpose == "Doctor":
            cursor.execute('CREATE TABLE IF NOT EXISTS Doctors (Name TEXT, Email_ID TEXT, Contact number, Password TEXT, Gender TEXT)')
            cursor.execute('INSERT INTO Doctors (Name, Email_ID, Contact, Password, Gender) VALUES(?,?,?,?,?)',(name ,email, contact, password, gender))
            conn.commit()
        else:
            cursor.execute('CREATE TABLE IF NOT EXISTS Paitent (Name text, Email_ID text, Contact number, Password text, Gender text)')
            cursor.execute('INSERT INTO Paitent (Name, Email_ID, Contact, Password, Gender) VALUES(?,?,?,?,?)',(name ,email, contact, password, gender))
            conn.commit()


    def register_act(input):
        if name_input.get()=="":
            messagebox.showerror("Error","Name can't be Empty", parent = registerpage)
        elif email_input.get()=="":
            messagebox.showerror("Error","Email ID can't be Empty", parent = registerpage)
        elif contact_input.get()=="":
            messagebox.showerror("Error","Contact can't be Empty", parent = registerpage)
        elif password_input.get()=="":
            messagebox.showerror("Error","Password can't be Empty", parent = registerpage)
        elif cnf_password_input.get()=="":
            messagebox.showerror("Error","Confirm Password can't be Empty", parent = registerpage)
        elif gender_var.get()=="":
            messagebox.showerror("Error","Gender can't be Empty", parent = registerpage)
        elif purpose_var.get()=="":
            messagebox.showerror("Error","Purpose can't be Empty", parent = registerpage)
        elif password_input.get()!= cnf_password_input.get():
            messagebox.showerror("Error","Password and Confirm Password Should Be Same", parent=registerpage)
        else:
            messagebox.showinfo("Success","Registration Successful", parent=registerpage)
            database()
            registerpage.destroy()
    

    registerpage = Toplevel(root)
    registerpage.geometry("750x750")
    registerpage.title("Registration Page")
    register_frame = Frame(registerpage, bg = "#037ef3")
    register_frame.place(x = 0, y = 0, width = 750, height = 750)
    header=Label(register_frame, text="Register",font=('Poppins Bold',20), fg="white",bg='#037ef3')
    header.place(relx=0.5, rely= 0.01, anchor = 'n')
    input = Frame(register_frame, bg = "#037ef3")
    input.place(relx = 0.5, rely = 0.4, anchor = 'center', width = 500, height = 500)
    name=Label(input, text="Name:",font=('Poppins Bold',13), fg="white",bg='#037ef3')
    name.place(relx=0.1, rely= 0.1, anchor = 'nw')
    name_input=Entry(input, font=("Poppins Regular",10),fg = 'black', bg='#00c16e', relief = GROOVE)
    name_input.place(relx = 0.1, rely = 0.16,anchor = 'nw', width = 400)
    email=Label(input, text="Email ID:",font=('Poppins Bold',13), fg="white",bg='#037ef3')
    email.place(relx=0.1, rely= 0.22, anchor = 'nw')
    email_input=Entry(input, font=("Poppins Regular",10),fg = 'black', bg='#00c16e', relief = GROOVE)
    email_input.place(relx = 0.1, rely = 0.28,anchor = 'nw', width = 400)
    contact=Label(input, text="Contact:",font=('Poppins Bold',13), fg="white",bg='#037ef3')
    contact.place(relx=0.1, rely= 0.34, anchor = 'nw')
    contact_input=Entry(input, font=("Poppins Regular",10),fg = 'black', bg='#00c16e', relief = GROOVE)
    contact_input.place(relx = 0.1, rely = 0.40,anchor = 'nw', width = 400)
    password=Label(input, text="Password:",font=('Poppins Bold',13), fg="white",bg='#037ef3')
    password.place(relx=0.1, rely= 0.46, anchor = 'nw')
    password_input= tk.Entry(input, show = '*', font=('Poppins Regular',10), fg = 'black', bg='#00c16e', relief = GROOVE)
    password_input.place(relx = 0.1, rely = 0.52,anchor = 'nw', width = 400)
    cnf_password=Label(input, text="Confirm Password:",font=('Poppins Bold',13), fg="white",bg='#037ef3')
    cnf_password.place(relx=0.1, rely= 0.58, anchor = 'nw')
    cnf_password_input=Entry(input, font=("Poppins Regular",10),fg = 'black', bg='#00c16e', relief = GROOVE)
    cnf_password_input.place(relx = 0.1, rely = 0.64,anchor = 'nw', width = 400)
    gender= Label(input, text="Gender:",font=('Poppins Bold',13), fg="white",bg='#037ef3')
    gender.place(relx=0.1, rely= 0.70, anchor = 'nw')
    get_gender = OptionMenu(input, gender_var, *genders)
    get_gender.config(width = 20, font=('Poppins Regular',10), bd = 0, fg = 'black', bg='#00c16e', relief = GROOVE)
    get_gender.pack()
    get_gender.place(relx=0.1, rely= 0.76, anchor = 'nw')
    purposelbl= Label(input, text="Purpose:",font=('Poppins Bold',13), fg="white",bg='#037ef3')
    purposelbl.place(relx=0.1, rely= 0.85, anchor = 'nw')
    get_purpose = OptionMenu(input, purpose_var, *purpose)
    get_purpose.config(width = 20, font=('Poppins Regular',10), bd = 0, fg = 'black', bg='#00c16e', relief = GROOVE)
    get_purpose.pack()
    get_purpose.place(relx=0.1, rely= 0.91, anchor = 'nw')
    lbl_register = Label(register_frame, text = "Register", font = ("Poppins Bold", 15), padx = 10, relief = GROOVE, fg = "white", bg = "#00c16e", cursor = "hand2")
    lbl_register.pack()
    lbl_register.bind("<Button-1>", lambda e: register_act(input))
    lbl_register.place(relx = 0.5 , rely = 0.75, anchor = 'n')
    already_register=Label(register_frame, text="Already Registerd?",font=('Poppins Bold',13), fg="white",bg='#037ef3')
    already_register.place(relx=0.5, rely= 0.82, anchor = 'n')
    lbl_login = Label(register_frame, text = "Login", font = ("Poppins Bold", 15), padx = 20, relief = GROOVE, fg = "white", bg = "#00c16e", cursor = "hand2")
    lbl_login.pack()
    lbl_login.bind("<Button-1>", lambda e: [registerpage.destroy(), open_login()])
    lbl_login.place(relx = 0.5 , rely = 0.88, anchor = 'n')

   
class HospitalManagementSystem:

    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1920x1080+0+0")

        # Banner placing
        img1 = Image.open(r"C:\Users\Gaura\OneDrive\Desktop\HMS1.0\Images\HMSBanner.png")
        img1 = img1.resize((1920,140), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lableimg = Label(self.root, image = self.photoimg1)
        lableimg.place(x=0, y=0, width = 1920, height = 140)

        #Loginbtn frame
        login_frame = Frame(self.root, bg = "#037ef3")
        login_frame.place(x = 0, y = 140, width = 1920, height = 50)
        lbl_login = Label(login_frame, text = "Login", font = ("Poppins Bold", 15), fg = "white", bg = "#037ef3", cursor = "hand2")
        lbl_login.pack()
        lbl_login.bind("<Button-1>", lambda e: open_login())
        lbl_login.place(relx = 0.89 , rely = 0.5, anchor = 'w')
        lbl_register = Label(login_frame, text = "Register", font = ("Poppins Bold", 15), fg = "white", bg = "#037ef3", cursor = "hand2")
        lbl_register.pack()
        lbl_register.bind("<Button-1>", lambda e: open_register())
        lbl_register.place(relx = 0.94 , rely = 0.5, anchor = 'w')
        lbl_menu = Label(login_frame, text = "MENU >>", font = ("Poppins Bold", 15), fg = "white", bg = "#037ef3")
        lbl_menu.place(relx = 0.01, rely = 0.5, anchor = 'w')

        #main frame
        main_frame = Frame(self.root)
        main_frame.place(x = 240, y = 190, width = (1920 - 240), height = 880)

        img2 = Image.open(r"C:\Users\Gaura\OneDrive\Desktop\HMS1.0\Images\Hospital.jpg")
        img2 = img2.resize(((1920-250),330), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lableimg2 = Label(main_frame, image = self.photoimg2)
        lableimg2.place(x=5, y=5, width = (1920-250), height = 330)

        
        def open_home():
            button_inactive()
            hide_frames()
            home_btn.config(bg = "#037ef3")
            home_frame.pack(fill = 'both', expand= 1)
#==========================================================================================
        def open_paitent():

            def save_act():
                conn = sqlite3.connect(database = r'database.db')
                cursor=conn.cursor()

                if self.var_name.get()=="":
                    messagebox.showerror("Error","Name can't be Empty", parent = paitent_frame)
                elif self.var_pat_id.get()=="":
                    messagebox.showerror("Error","Paitent ID can't be Empty", parent = paitent_frame)
                elif self.var_email.get()=="":
                    messagebox.showerror("Error","Email ID can't be Empty", parent = paitent_frame)
                elif self.var_contact.get()=="":
                    messagebox.showerror("Error","Contact can't be Empty", parent = paitent_frame)
                elif self.var_passwd.get()=="":
                    messagebox.showerror("Error","Password can't be Empty", parent =paitent_frame)
                elif self.var_gender.get()=="Select":
                    messagebox.showerror("Error","Gender can't be Empty", parent = paitent_frame)
                elif self.var_purpose.get()=="Select":
                    messagebox.showerror("Error","Purpose can't be Empty", parent = paitent_frame)
                else:
                    cursor.execute('Select * from Paitent2 where P_ID = ?', (self.var_pat_id.get(),))
                    row = cursor.fetchone()
                    if row != None:
                        messagebox.showerror("Error","Paitent ID is already in use", parent = paitent_frame)
                    else:
                        cursor.execute('CREATE TABLE IF NOT EXISTS Paitent2 (P_ID number PRIMARY KEY, Email_ID TEXT, Contact number, Name Text, Gender text, Doctor text, Date_Of_Join Date, Purpose text, Date_Of_Release date, Diagnosis text, Bill_Amount number, Password Text)')
                        cursor.execute('INSERT INTO Paitent2 (P_ID , Email_ID , Contact, Name , Gender , Doctor , Date_Of_Join , Purpose, Date_Of_Release, Diagnosis, Bill_Amount, Password ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(self.var_pat_id.get(), self.var_email.get(), self.var_contact.get(), self.var_name.get(), self.var_gender.get(), self.var_doc.get(), self.var_ad.get(), self.var_purpose.get(), self.var_rd.get(), self.txt_diag.get('1.0', END), self.var_bill.get(), self.var_passwd.get()))
                        conn.commit()
                        messagebox.showinfo("Success","Registration Successful", parent=paitent_frame)
                        showdata()
            
            def showdata():
                conn = sqlite3.connect(database = r'database.db')
                cursor=conn.cursor()
                try:
                    cursor.execute('select * from Paitent2')
                    rows = cursor.fetchall()
                    self.PaitentTable.delete(*self.PaitentTable.get_children())
                    for row in rows:
                        self.PaitentTable.insert('',END,values = row)
                except Exception as ex:
                    messagebox.showerror("Error",f"Error due to : {str(ex)}", parent = paitent_frame)

            def update_act():
                conn = sqlite3.connect(database = r'database.db')
                cursor=conn.cursor()

                if self.var_name.get()=="":
                    messagebox.showerror("Error","Name can't be Empty", parent = paitent_frame)
                elif self.var_pat_id.get()=="":
                    messagebox.showerror("Error","Paitent ID can't be Empty", parent = paitent_frame)
                elif self.var_email.get()=="":
                    messagebox.showerror("Error","Email ID can't be Empty", parent = paitent_frame)
                elif self.var_contact.get()=="":
                    messagebox.showerror("Error","Contact can't be Empty", parent = paitent_frame)
                elif self.var_passwd.get()=="":
                    messagebox.showerror("Error","Password can't be Empty", parent =paitent_frame)
                elif self.var_gender.get()=="Select":
                    messagebox.showerror("Error","Gender can't be Empty", parent = paitent_frame)
                elif self.var_purpose.get()=="Select":
                    messagebox.showerror("Error","Purpose can't be Empty", parent = paitent_frame)
                else:
                    cursor.execute('Select * from Paitent2 where P_ID = ?', (self.var_pat_id.get(),))
                    row = cursor.fetchone()
                    if row == None:
                        messagebox.showerror("Error","Invalid Paitent ID", parent = paitent_frame)
                    else:
                        cursor.execute('UPDATE Paitent2 set Email_ID = ? , Contact = ?, Name =?, Gender=? , Doctor=? , Date_Of_Join=? , Purpose=?, Date_Of_Release=?, Diagnosis=?, Bill_Amount=?, Password=? where P_ID = ?', (self.var_email.get(), self.var_contact.get(), self.var_name.get(), self.var_gender.get(), self.var_doc.get(), self.var_ad.get(), self.var_purpose.get(), self.var_rd.get(), self.txt_diag.get('1.0', END), self.var_bill.get(), self.var_passwd.get(), self.var_pat_id.get()))
                        conn.commit()
                        messagebox.showinfo("Success","Updation Successful", parent=paitent_frame)
                        showdata()

            def get_data(ev):
               f=self.PaitentTable.focus()
               content = (self.PaitentTable.item(f))
               row = content['values']
               self.var_pat_id.set(row[0])
               self.var_email.set(row[1])
               self.var_contact.set(row[2])
               self.var_name.set(row[3])
               self.var_gender.set(row[4])
               self.var_doc.set(row[5])
               self.var_ad.set(row[6])
               self.var_purpose.set(row[7])
               self.var_rd.set(row[8])
               self.txt_diag.delete('1.0', END)
               self.txt_diag.insert(END, row[9])
               self.var_bill.set(row[10])
               self.var_passwd.set(row[11])

            def delete_act():
                conn = sqlite3.connect(database = r'database.db')
                cursor=conn.cursor()
                if self.var_pat_id.get()=="":
                    messagebox.showerror("Error","Enter Paitent ID", parent = paitent_frame)
                else:
                    cursor.execute('Select * from Paitent2 where P_ID = ?', (self.var_pat_id.get(),))
                    row = cursor.fetchone()
                    if row == None:
                        messagebox.showerror("Error","Invalid Paitent ID", parent = paitent_frame)
                    else:
                        op=messagebox.askyesno("Confirm","Do you want to delete Entry?", parent = paitent_frame)
                        if op == True:
                            cursor.execute('DELETE from Paitent2 where P_ID = ?', (self.var_pat_id.get(),))
                            conn.commit()
                            messagebox.showinfo("Success","Deletion Successful", parent=paitent_frame)
                            showdata()
                            reset_act()

            def search_act():
                conn = sqlite3.connect(database = r'database.db')
                cursor=conn.cursor()
                if self.var_searchby.get()=="Select":
                    messagebox.showerror("Error","Select Search By Option", parent = paitent_frame)
                elif self.var_searchtxt.get()=="":
                    messagebox.showerror("Error","Search Text can't be Empty", parent = paitent_frame)
                else:
                    cursor.execute("Select * from Paitent2 where "+ self.var_searchby.get()+ " LIKE '%" + self.var_searchtxt.get()+ "%'")
                    rows = cursor.fetchall()
                    if len(rows) !=0:
                        self.PaitentTable.delete(*self.PaitentTable.get_children())
                        for row in rows:
                            self.PaitentTable.insert('',END,values = row)
                    else:
                        messagebox.showerror("Error","No record Found", parent = paitent_frame)
            
            def reset_act():
               self.var_pat_id.set("")
               self.var_email.set("")
               self.var_contact.set("")
               self.var_name.set("")
               self.var_gender.set("Select")
               self.var_doc.set("")
               self.var_ad.set("")
               self.var_purpose.set("Select")
               self.var_rd.set("")
               self.txt_diag.delete('1.0', END)
               self.var_bill.set("")
               self.var_passwd.set("")
               self.var_searchby.set("Select")
               self.var_searchtxt.set("")
               showdata()

            self.var_searchby = StringVar()
            self.var_searchtxt = StringVar()
            self.var_pat_id = StringVar()
            self.var_name = StringVar()
            self.var_contact = StringVar()
            self.var_email = StringVar()
            self.var_doc = StringVar()
            self.var_gender = StringVar()
            self.var_ad= StringVar()
            self.var_rd = StringVar()
            self.var_purpose = StringVar()
            self.var_bill = StringVar()
            self.var_passwd = StringVar()

            button_inactive()
            hide_frames()
            paitent_btn.config(bg = "#037ef3")
            paitent_frame.place(x = 0, y = 0, width = (1920-240), height = 880)
            paitent_frame.pack(fill = 'both', expand= 1)
            search_frame = LabelFrame(paitent_frame, text = "Search Paitent", bg = "white", font = ("Poppins Bold", 13))
            search_frame.place(x = 340, y = 50, width = 1000, height = 100)
            cmb_search = ttk.Combobox(search_frame,textvariable = self.var_searchby, values=("Select", "Name", "Contact", "Email"), state = "readonly", justify = CENTER, font = ("Poppins Regular", 10))
            cmb_search.place(x = 15, y = 10, width = 180, height = 40) 
            cmb_search.current(0)
            txt_search = Entry(search_frame, textvariable = self.var_searchtxt, font = ("Poppins Regular", 10), bg = "#037ef3", fg = "white")
            txt_search.place(x = 200, y = 10, height = 40, width = 650)
            lbl_search = Label(search_frame, text = "Search", font = ("Poppins Bold", 15), fg = "white", bg = "#00c16e", cursor = "hand2")
            lbl_search.place(x = 855, y = 10, width = 125, height = 40)
            lbl_search.bind("<Button-1>", lambda e: search_act())
            page_title = Label(paitent_frame, text = "Paitent Details", font = ("Poppins Bold", 15), bg = "#037ef3", fg = "White")
            page_title.place(x = 340, y = 180, width = 1000, height = 40)
            lbl_pat_id = Label(paitent_frame, text = "Paitent ID", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_id.place(x = 340, y = 250)
            lbl_pat_mail = Label(paitent_frame, text = "Email ID", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_mail.place(x = 680, y = 250)
            lbl_pat_contact = Label(paitent_frame, text = "Contact", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_contact.place(x = 1020, y = 250)
            txt_pat_id = Entry(paitent_frame, textvariable = self.var_pat_id, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_id.place(x = 440, y = 250, width = 200)
            txt_pat_mail = Entry(paitent_frame, textvariable = self.var_email, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_mail.place(x = 780, y = 250, width = 200)
            txt_pat_contact = Entry(paitent_frame, textvariable = self.var_contact, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_contact.place(x = 1120, y = 250, width = 200)
            lbl_pat_gender = Label(paitent_frame, text = "Gender", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_gender.place(x = 680, y = 280)
            cmb_gender = ttk.Combobox(paitent_frame,textvariable = self.var_gender, values=("Select", "Male", "Female", "Others"), state = "readonly", justify = CENTER, font = ("Poppins Regular", 10))
            cmb_gender.place(x = 780, y = 280, width = 200) 
            cmb_gender.current(0)
            lbl_pat_name = Label(paitent_frame, text = "Name", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_name.place(x = 340, y = 280)
            txt_pat_name = Entry(paitent_frame, textvariable = self.var_name, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_name.place(x = 440, y = 280, width = 200)
            lbl_pat_doc = Label(paitent_frame, text = "Doctor", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_doc.place(x = 1020, y = 280)
            txt_pat_doc = Entry(paitent_frame, textvariable = self.var_doc, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_doc.place(x = 1120, y = 280, width = 200)
            lbl_pat_purpose = Label(paitent_frame, text = "Purpose", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_purpose.place(x = 680, y = 310)
            cmb_purpose = ttk.Combobox(paitent_frame,textvariable = self.var_purpose, values=("Select", "Doctor", "Paitent"), state = "readonly", justify = CENTER, font = ("Poppins Regular", 10))
            cmb_purpose.place(x = 780, y = 310, width = 200) 
            cmb_purpose.current(0)
            lbl_pat_join = Label(paitent_frame, text = "Join Date", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_join.place(x = 340, y = 310)
            txt_pat_join = Entry(paitent_frame, textvariable = self.var_ad, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_join.place(x = 440, y = 310, width = 200)
            lbl_pat_release = Label(paitent_frame, text = "Release Date", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_release.place(x = 1020, y =310)
            txt_pat_release = Entry(paitent_frame, textvariable = self.var_rd, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_release.place(x = 1120, y = 310, width = 200)
            lbl_pat_bill = Label(paitent_frame, text = "Bill Amount", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_bill.place(x = 680, y = 340)
            txt_pat_bill = Entry(paitent_frame, textvariable = self.var_bill, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_bill.place(x = 780, y = 340, width = 200)
            lbl_pat_passwd = Label(paitent_frame, text = "Password", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_passwd.place(x = 1020, y = 340)
            txt_pat_passwd = Entry(paitent_frame, textvariable = self.var_passwd, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_passwd.place(x = 1120, y = 340, width = 200)
            lbl_pat_diag = Label(paitent_frame, text = "Diagnosis", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_diag.place(x = 340, y = 340)
            self.txt_diag = Text(paitent_frame, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            self.txt_diag.place(x = 440, y = 340, width = 200, height = 100 )
            lbl_save = Label(paitent_frame, text = "Save", font = ("Poppins Bold", 15), fg = "white", bg = "#00c16e", cursor = "hand2")
            lbl_save.place(x = 720, y = 400, width = 120, height = 40)
            lbl_save.bind("<Button-1>", lambda e: save_act())
            lbl_update = Label(paitent_frame, text = "Update", font = ("Poppins Bold", 15), fg = "white", bg = "#00c16e", cursor = "hand2")
            lbl_update.place(x = 850, y = 400, width = 120, height = 40)
            lbl_update.bind("<Button-1>", lambda e: update_act())
            lbl_delete = Label(paitent_frame, text = "Delete", font = ("Poppins Bold", 15), fg = "white", bg = "Red", cursor = "hand2")
            lbl_delete.place(x = 980, y = 400, width = 120, height = 40)
            lbl_delete.bind("<Button-1>", lambda e: delete_act())
            lbl_reset = Label(paitent_frame, text = "Reset", font = ("Poppins Bold", 15), fg = "white", bg = "Red", cursor = "hand2")
            lbl_reset.place(x = 1110, y = 400, width = 120, height = 40)
            lbl_reset.bind("<Button-1>", lambda e: reset_act())

            data_frame = Frame(paitent_frame, bd = 2, relief= RIDGE)
            data_frame.place(x = 340, y = 480, width = 1000, height = 300)
            scrolly = Scrollbar(data_frame, orient= VERTICAL)
            scrollx = Scrollbar(data_frame, orient= HORIZONTAL)
            
            self.PaitentTable = ttk.Treeview(data_frame, columns=("p_id", "email", "contact", "name", "gender", "doctor", "doj", "purpose", "dor", "diag", "bill", "password"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
            scrollx.pack(side=BOTTOM, fill=X)
            scrolly.pack(side = RIGHT, fill= Y)
            scrollx.config(command= self.PaitentTable.xview)
            scrolly.config(command= self.PaitentTable.yview)
            self.PaitentTable.heading("p_id", text = "Paitent ID")
            self.PaitentTable.heading("email", text = "Email ID")
            self.PaitentTable.heading("contact", text = "Contact")
            self.PaitentTable.heading("name", text = "Name")
            self.PaitentTable.heading("gender", text = "Gender")
            self.PaitentTable.heading("doctor", text = "Doctor")
            self.PaitentTable.heading("doj", text = "Join Date")
            self.PaitentTable.heading("purpose", text = "Purpose")
            self.PaitentTable.heading("dor", text = "Release Date")
            self.PaitentTable.heading("diag", text = "Diagnosis")
            self.PaitentTable.heading("bill", text = "Bill Amount")
            self.PaitentTable.heading("password", text = "Password")
            self.PaitentTable["show"] = "headings"
            self.PaitentTable.column("p_id", width = 90)
            self.PaitentTable.column("email", width = 90)
            self.PaitentTable.column("contact", width = 90)
            self.PaitentTable.column("name", width = 90)
            self.PaitentTable.column("gender", width = 90)
            self.PaitentTable.column("doctor", width = 90)
            self.PaitentTable.column("doj", width = 90)
            self.PaitentTable.column("purpose", width = 90)
            self.PaitentTable.column("dor", width = 90)
            self.PaitentTable.column("diag", width = 150)
            self.PaitentTable.column("bill", width = 90)
            self.PaitentTable.column("password", width = 90)
            self.PaitentTable.pack(fill = BOTH, expand = 1)
            self.PaitentTable.bind("<ButtonRelease-1>",get_data)
            showdata()
            
#==============================================================================================================
        def open_doctor():
            def save_act():
                conn = sqlite3.connect(database = r'database.db')
                cursor=conn.cursor()

                if self.var_docname.get()=="":
                    messagebox.showerror("Error","Name can't be Empty", parent = doctor_frame)
                elif self.var_doc_id.get()=="":
                    messagebox.showerror("Error","Doctor ID can't be Empty", parent = doctor_frame)
                elif self.var_docemail.get()=="":
                    messagebox.showerror("Error","Email ID can't be Empty", parent = doctor_frame)
                elif self.var_doccontact.get()=="":
                    messagebox.showerror("Error","Contact can't be Empty", parent = doctor_frame)
                elif self.var_docpasswd.get()=="":
                    messagebox.showerror("Error","Password can't be Empty", parent =doctor_frame)
                elif self.var_docgender.get()=="Select":
                    messagebox.showerror("Error","Gender can't be Empty", parent = doctor_frame)
                elif self.var_purpose.get()=="Select":
                    messagebox.showerror("Error","Purpose can't be Empty", parent = doctor_frame)
                else:
                    cursor.execute('Select * from Doctor2 where D_ID = ?', (self.var_doc_id.get(),))
                    row = cursor.fetchone()
                    if row != None:
                        messagebox.showerror("Error","Doctor ID is already in use", parent = doctor_frame)
                    else:
                        cursor.execute('CREATE TABLE IF NOT EXISTS Doctor2 (D_ID number PRIMARY KEY, Email_ID TEXT, Contact number, Name Text, Gender text, Specialization text, Date_Of_Join Date, Purpose text, Date_Of_Release date, Address text, Salary number, Password Text)')
                        cursor.execute('INSERT INTO Doctor2 (D_ID , Email_ID , Contact, Name , Gender , Specialization, Date_Of_Join , Purpose, Date_Of_Release, Address, Salary, Password ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(self.var_doc_id.get(), self.var_docemail.get(), self.var_doccontact.get(), self.var_docname.get(), self.var_docgender.get(), self.var_spl.get(), self.var_docad.get(), self.var_purpose.get(), self.var_docrd.get(), self.txt_add.get('1.0', END), self.var_sal.get(), self.var_docpasswd.get()))
                        conn.commit()
                        messagebox.showinfo("Success","Registration Successful", parent=doctor_frame)
                        showdata()
            
            def showdata():
                conn = sqlite3.connect(database = r'database.db')
                cursor=conn.cursor()
                try:
                    cursor.execute('select * from Doctor2')
                    rows = cursor.fetchall()
                    self.DoctorTable.delete(*self.DoctorTable.get_children())
                    for row in rows:
                        self.DoctorTable.insert('',END,values = row)
                except Exception as ex:
                    messagebox.showerror("Error",f"Error due to : {str(ex)}", parent = doctor_frame)

            def update_act():
                conn = sqlite3.connect(database = r'database.db')
                cursor=conn.cursor()

                if self.var_docname.get()=="":
                    messagebox.showerror("Error","Name can't be Empty", parent = doctor_frame)
                elif self.var_doc_id.get()=="":
                    messagebox.showerror("Error","Doctor ID can't be Empty", parent = doctor_frame)
                elif self.var_docemail.get()=="":
                    messagebox.showerror("Error","Email ID can't be Empty", parent = doctor_frame)
                elif self.var_doccontact.get()=="":
                    messagebox.showerror("Error","Contact can't be Empty", parent = doctor_frame)
                elif self.var_docpasswd.get()=="":
                    messagebox.showerror("Error","Password can't be Empty", parent =doctor_frame)
                elif self.var_docgender.get()=="Select":
                    messagebox.showerror("Error","Gender can't be Empty", parent = doctor_frame)
                elif self.var_purpose.get()=="Select":
                    messagebox.showerror("Error","Purpose can't be Empty", parent = doctor_frame)
                else:
                    cursor.execute('Select * from Doctor2 where D_ID = ?', (self.var_doc_id.get(),))
                    row = cursor.fetchone()
                    if row == None:
                        messagebox.showerror("Error","Invalid Doctor ID", parent = doctor_frame)
                    else:
                        cursor.execute('UPDATE Doctor2 set Email_ID = ? , Contact = ?, Name =?, Gender=? , Specialization=? , Date_Of_Join=? , Purpose=?, Date_Of_Release=?, Address=?, Salary=?, Password=? where D_ID = ?', (self.var_docemail.get(), self.var_doccontact.get(), self.var_docname.get(), self.var_docgender.get(), self.var_spl.get(), self.var_docad.get(), self.var_purpose.get(), self.var_docrd.get(), self.txt_add.get('1.0', END), self.var_sal.get(), self.var_docpasswd.get(), self.var_doc_id.get()))
                        conn.commit()
                        messagebox.showinfo("Success","Updation Successful", parent=doctor_frame)
                        showdata()

            def get_data(ev):
               f=self.DoctorTable.focus()
               content = (self.DoctorTable.item(f))
               row = content['values']
               self.var_doc_id.set(row[0])
               self.var_docemail.set(row[1])
               self.var_doccontact.set(row[2])
               self.var_docname.set(row[3])
               self.var_docgender.set(row[4])
               self.var_spl.set(row[5])
               self.var_docad.set(row[6])
               self.var_purpose.set(row[7])
               self.var_docrd.set(row[8])
               self.txt_add.delete('1.0', END)
               self.txt_add.insert(END, row[9])
               self.var_sal.set(row[10])
               self.var_docpasswd.set(row[11])

            def delete_act():
                conn = sqlite3.connect(database = r'database.db')
                cursor=conn.cursor()
                if self.var_doc_id.get()=="":
                    messagebox.showerror("Error","Enter Paitent ID", parent = doctor_frame)
                else:
                    cursor.execute('Select * from Paitent2 where P_ID = ?', (self.var_doc_id.get(),))
                    row = cursor.fetchone()
                    if row == None:
                        messagebox.showerror("Error","Invalid Paitent ID", parent = doctor_frame)
                    else:
                        op=messagebox.askyesno("Confirm","Do you want to delete Entry?", parent = doctor_frame)
                        if op == True:
                            cursor.execute('DELETE from Paitent2 where P_ID = ?', (self.var_doc_id.get(),))
                            conn.commit()
                            messagebox.showinfo("Success","Deletion Successful", parent=doctor_frame)
                            showdata()
                            reset_act()

            def search_act():
                conn = sqlite3.connect(database = r'database.db')
                cursor=conn.cursor()
                if self.var_searchby.get()=="Select":
                    messagebox.showerror("Error","Select Search By Option", parent = doctor_frame)
                elif self.var_searchtxt.get()=="":
                    messagebox.showerror("Error","Search Text can't be Empty", parent = doctor_frame)
                else:
                    cursor.execute("Select * from Paitent2 where "+ self.var_searchby.get()+ " LIKE '%" + self.var_searchtxt.get()+ "%'")
                    rows = cursor.fetchall()
                    if len(rows) !=0:
                        self.DoctorTable.delete(*self.DoctorTable.get_children())
                        for row in rows:
                            self.DoctorTable.insert('',END,values = row)
                    else:
                        messagebox.showerror("Error","No record Found", parent = doctor_frame)
            
            def reset_act():
               self.var_doc_id.set("")
               self.var_docemail.set("")
               self.var_doccontact.set("")
               self.var_docname.set("")
               self.var_docgender.set("Select")
               self.var_spl.set("")
               self.var_docad.set("")
               self.var_purpose.set("Select")
               self.var_docrd.set("")
               self.txt_add.delete('1.0', END)
               self.var_sal.set("")
               self.var_docpasswd.set("")
               self.var_searchby.set("Select")
               self.var_searchtxt.set("")
               showdata()

            self.var_searchby = StringVar()
            self.var_searchtxt = StringVar()
            self.var_doc_id = StringVar()
            self.var_docname = StringVar()
            self.var_doccontact = StringVar()
            self.var_docemail = StringVar()
            self.var_spl = StringVar()
            self.var_docgender = StringVar()
            self.var_docad= StringVar()
            self.var_docrd = StringVar()
            self.var_purpose = StringVar()
            self.var_sal = StringVar()
            self.var_docpasswd = StringVar()

            self.var_doc_id = StringVar()
            self.var_special = StringVar()

            button_inactive()
            hide_frames()
            doctor_btn.config(bg = "#037ef3")
            doctor_frame.place(x = 0, y = 0, width = (1920-240), height = 880)
            doctor_frame.pack(fill = 'both', expand= 1)
            search_frame = LabelFrame(doctor_frame, text = "Search Doctor", bg = "white", font = ("Poppins Bold", 13))
            search_frame.place(x = 340, y = 50, width = 1000, height = 100)
            cmb_search = ttk.Combobox(search_frame,textvariable = self.var_searchby, values=("Select", "Name", "Contact", "Email"), state = "readonly", justify = CENTER, font = ("Poppins Regular", 10))
            cmb_search.place(x = 15, y = 10, width = 180, height = 40) 
            cmb_search.current(0)
            txt_search = Entry(search_frame, textvariable = self.var_searchtxt, font = ("Poppins Regular", 10), bg = "#037ef3", fg = "white")
            txt_search.place(x = 200, y = 10, height = 40, width = 650)
            lbl_search = Label(search_frame, text = "Search", font = ("Poppins Bold", 15), fg = "white", bg = "#00c16e", cursor = "hand2")
            lbl_search.place(x = 855, y = 10, width = 125, height = 40)
            lbl_search.bind("<Button-1>", lambda e: search_act())
            page_title = Label(doctor_frame, text = "Doctor Details", font = ("Poppins Bold", 15), bg = "#037ef3", fg = "White")
            page_title.place(x = 340, y = 180, width = 1000, height = 40)
            lbl_pat_id = Label(doctor_frame, text = "Doctor ID", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_id.place(x = 340, y = 250)
            lbl_pat_mail = Label(doctor_frame, text = "Email ID", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_mail.place(x = 680, y = 250)
            lbl_pat_contact = Label(doctor_frame, text = "Contact", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_contact.place(x = 1020, y = 250)
            txt_doc_id = Entry(doctor_frame, textvariable = self.var_doc_id, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_doc_id.place(x = 440, y = 250, width = 200)
            txt_pat_mail = Entry(doctor_frame, textvariable = self.var_docemail, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_mail.place(x = 780, y = 250, width = 200)
            txt_pat_contact = Entry(doctor_frame, textvariable = self.var_doccontact, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_contact.place(x = 1120, y = 250, width = 200)
            lbl_pat_gender = Label(doctor_frame, text = "Gender", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_gender.place(x = 680, y = 280)
            cmb_gender = ttk.Combobox(doctor_frame,textvariable = self.var_docgender, values=("Select", "Male", "Female", "Others"), state = "readonly", justify = CENTER, font = ("Poppins Regular", 10))
            cmb_gender.place(x = 780, y = 280, width = 200) 
            cmb_gender.current(0)
            lbl_pat_name = Label(doctor_frame, text = "Name", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_name.place(x = 340, y = 280)
            txt_pat_name = Entry(doctor_frame, textvariable = self.var_docname, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_name.place(x = 440, y = 280, width = 200)
            lbl_pat_doc = Label(doctor_frame, text = "Specialization", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_doc.place(x = 1020, y = 280)
            txt_pat_doc = Entry(doctor_frame, textvariable = self.var_spl, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_doc.place(x = 1120, y = 280, width = 200)
            lbl_pat_purpose = Label(doctor_frame, text = "Purpose", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_purpose.place(x = 680, y = 310)
            cmb_purpose = ttk.Combobox(doctor_frame,textvariable = self.var_purpose, values=("Select", "Doctor", "Paitent"), state = "readonly", justify = CENTER, font = ("Poppins Regular", 10))
            cmb_purpose.place(x = 780, y = 310, width = 200) 
            cmb_purpose.current(0)
            lbl_pat_join = Label(doctor_frame, text = "Join Date", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_join.place(x = 340, y = 310)
            txt_pat_join = Entry(doctor_frame, textvariable = self.var_docad, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_join.place(x = 440, y = 310, width = 200)
            lbl_pat_release = Label(doctor_frame, text = "Release Date", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_release.place(x = 1020, y =310)
            txt_pat_release = Entry(doctor_frame, textvariable = self.var_docrd, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_release.place(x = 1120, y = 310, width = 200)
            lbl_pat_bill = Label(doctor_frame, text = "Salary", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_bill.place(x = 680, y = 340)
            txt_pat_bill = Entry(doctor_frame, textvariable = self.var_sal, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_bill.place(x = 780, y = 340, width = 200)
            lbl_pat_passwd = Label(doctor_frame, text = "Password", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_passwd.place(x = 1020, y = 340)
            txt_pat_passwd = Entry(doctor_frame, textvariable = self.var_docpasswd, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_passwd.place(x = 1120, y = 340, width = 200)
            lbl_pat_diag = Label(doctor_frame, text = "Address", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_diag.place(x = 340, y = 340)
            self.txt_add = Text(doctor_frame, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            self.txt_add.place(x = 440, y = 340, width = 200, height = 100 )
            lbl_save = Label(doctor_frame, text = "Save", font = ("Poppins Bold", 15), fg = "white", bg = "#00c16e", cursor = "hand2")
            lbl_save.place(x = 720, y = 400, width = 120, height = 40)
            lbl_save.bind("<Button-1>", lambda e: save_act())
            lbl_update = Label(doctor_frame, text = "Update", font = ("Poppins Bold", 15), fg = "white", bg = "#00c16e", cursor = "hand2")
            lbl_update.place(x = 850, y = 400, width = 120, height = 40)
            lbl_update.bind("<Button-1>", lambda e: update_act())
            lbl_delete = Label(doctor_frame, text = "Delete", font = ("Poppins Bold", 15), fg = "white", bg = "Red", cursor = "hand2")
            lbl_delete.place(x = 980, y = 400, width = 120, height = 40)
            lbl_delete.bind("<Button-1>", lambda e: delete_act())
            lbl_reset = Label(doctor_frame, text = "Reset", font = ("Poppins Bold", 15), fg = "white", bg = "Red", cursor = "hand2")
            lbl_reset.place(x = 1110, y = 400, width = 120, height = 40)
            lbl_reset.bind("<Button-1>", lambda e: reset_act())

            data_frame = Frame(doctor_frame, bd = 2, relief= RIDGE)
            data_frame.place(x = 340, y = 480, width = 1000, height = 300)
            scrolly = Scrollbar(data_frame, orient= VERTICAL)
            scrollx = Scrollbar(data_frame, orient= HORIZONTAL)
            
            self.DoctorTable = ttk.Treeview(data_frame, columns=("d_id", "email", "contact", "name", "gender", "spl", "doj", "purpose", "dor", "add", "sal", "password"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
            scrollx.pack(side=BOTTOM, fill=X)
            scrolly.pack(side = RIGHT, fill= Y)
            scrollx.config(command= self.DoctorTable.xview)
            scrolly.config(command= self.DoctorTable.yview)
            self.DoctorTable.heading("d_id", text = "Doctor ID")
            self.DoctorTable.heading("email", text = "Email ID")
            self.DoctorTable.heading("contact", text = "Contact")
            self.DoctorTable.heading("name", text = "Name")
            self.DoctorTable.heading("gender", text = "Gender")
            self.DoctorTable.heading("spl", text = "Specialization")
            self.DoctorTable.heading("doj", text = "Join Date")
            self.DoctorTable.heading("purpose", text = "Purpose")
            self.DoctorTable.heading("dor", text = "Release Date")
            self.DoctorTable.heading("add", text = "Address")
            self.DoctorTable.heading("sal", text = "Salary")
            self.DoctorTable.heading("password", text = "Password")
            self.DoctorTable["show"] = "headings"
            self.DoctorTable.column("d_id", width = 90)
            self.DoctorTable.column("email", width = 90)
            self.DoctorTable.column("contact", width = 90)
            self.DoctorTable.column("name", width = 90)
            self.DoctorTable.column("gender", width = 90)
            self.DoctorTable.column("spl", width = 90)
            self.DoctorTable.column("doj", width = 90)
            self.DoctorTable.column("purpose", width = 90)
            self.DoctorTable.column("dor", width = 90)
            self.DoctorTable.column("add", width = 150)
            self.DoctorTable.column("sal", width = 90)
            self.DoctorTable.column("password", width = 90)
            self.DoctorTable.pack(fill = BOTH, expand = 1)
            self.DoctorTable.bind("<ButtonRelease-1>",get_data)
            showdata()
#===========================================================================================
        def open_appointment():

            def book_act():
                conn = sqlite3.connect(database = r'database.db')
                cursor=conn.cursor()

                if self.var_appname.get()=="":
                    messagebox.showerror("Error","Name can't be Empty", parent = appointment_frame)
                elif self.var_appdate.get()=="":
                    messagebox.showerror("Error","Doctor ID can't be Empty", parent = appointment_frame)
                elif self.var_apptime.get()=="":
                    messagebox.showerror("Error","Email ID can't be Empty", parent = appointment_frame)
                elif self.var_appcat.get()=="":
                    messagebox.showerror("Error","Contact can't be Empty", parent = appointment_frame)
                else:
                    cursor.execute('CREATE TABLE IF NOT EXISTS App2 (Name text, Appoint_Date text, Appoint_Time text, Category text)')
                    cursor.execute('INSERT INTO App2 (Name, Appoint_Date, Appoint_Time, Category) VALUES(?,?,?,?)',(self.var_appname.get(), self.var_appdate.get(), self.var_apptime.get(), self.var_appcat.get()))
                    conn.commit()
                    messagebox.showinfo("Success","Appointment Successful", parent=appointment_frame)
                    showdata()

            def showdata():
                conn = sqlite3.connect(database = r'database.db')
                cursor=conn.cursor()
                try:
                    cursor.execute('select * from App2')
                    rows = cursor.fetchall()
                    self.AppointTable.delete(*self.AppointTable.get_children())
                    for row in rows:
                        self.AppointTable.insert('',END,values = row)
                except Exception as ex:
                    messagebox.showerror("Error",f"Error due to : {str(ex)}", parent = appointment_frame)

            def get_data(ev):
               f=self.AppointTable.focus()
               content = (self.AppointTable.item(f))
               row = content['values']
               self.var_appname.set(row[0])
               self.var_appdate.set(row[1])
               self.var_apptime.set(row[2])
               self.var_appcat.set(row[3])

            button_inactive()
            hide_frames()
            appointment_btn.config(bg = "#037ef3")
            appointment_frame.place(x = 0, y = 0, width = (1920-240), height = 880)
            appointment_frame.pack(fill = 'both', expand= 1)

            self.var_appname = StringVar()
            self.var_appdate = StringVar()
            self.var_apptime = StringVar()
            self.var_appcat = StringVar()

            page_title = Label(appointment_frame, text = "Appointment Booking", font = ("Poppins Bold", 15), bg = "#037ef3", fg = "White")
            page_title.place(x = 340, y = 80, width = 1000, height = 40)
            lbl_pat_name = Label(appointment_frame, text = "Name", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_name.place(x = 340, y = 180)
            txt_pat_name = Entry(appointment_frame, textvariable = self.var_appname, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_name.place(x = 440, y = 180, width = 200)
            lbl_pat_date = Label(appointment_frame, text = "Date", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_date.place(x = 740, y = 180)
            txt_pat_date = Entry(appointment_frame, textvariable = self.var_appdate, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_date.place(x = 840, y = 180, width = 200)

            lbl_pat_time = Label(appointment_frame, text = "Time", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_time.place(x = 340, y = 220)
            txt_pat_name = Entry(appointment_frame, textvariable = self.var_apptime, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_name.place(x = 440, y = 220, width = 200)
            lbl_pat_cat = Label(appointment_frame, text = "Category", font = ("Poppins regular", 10), bg = "White", fg = "Black")
            lbl_pat_cat.place(x = 740, y = 220)
            txt_pat_cat = Entry(appointment_frame, textvariable = self.var_appcat, font = ("Poppins regular", 10), bg = "White", fg = "Black")
            txt_pat_cat.place(x = 840, y = 220, width = 200)

            lbl_save = Label(appointment_frame, text = "Book Appointment", font = ("Poppins Bold", 15), fg = "white", bg = "#00c16e", cursor = "hand2")
            lbl_save.place(x = 720, y = 400, width = 200, height = 40)
            lbl_save.bind("<Button-1>", lambda e: book_act())

            data_frame = Frame(appointment_frame, bd = 2, relief= RIDGE)
            data_frame.place(x = 340, y = 480, width = 1000, height = 300)
            scrolly = Scrollbar(data_frame, orient= VERTICAL)
            scrollx = Scrollbar(data_frame, orient= HORIZONTAL)
            
            self.AppointTable = ttk.Treeview(data_frame, columns=("name", "date", "time", "cat"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
            scrollx.pack(side=BOTTOM, fill=X)
            scrolly.pack(side = RIGHT, fill= Y)
            scrollx.config(command= self.AppointTable.xview)
            scrolly.config(command= self.AppointTable.yview)
            self.AppointTable.heading("name", text = "Name")
            self.AppointTable.heading("date", text = "Date")
            self.AppointTable.heading("time", text = "Time")
            self.AppointTable.heading("cat", text = "Category")
            self.AppointTable["show"] = "headings"
            self.AppointTable.column("name", width = 100)
            self.AppointTable.column("date", width = 100)
            self.AppointTable.column("time", width = 100)
            self.AppointTable.column("cat", width = 100)
            self.AppointTable.pack(fill = BOTH, expand = 1)
            self.AppointTable.bind("<ButtonRelease-1>",get_data)
            showdata()




        def open_billing():
            button_inactive()
            hide_frames()
            billing_btn.config(bg = "#037ef3")
            billing_frame.place(x = 0, y = 0, width = (1920-240), height = 880)
            billing_frame.pack(fill = 'both', expand= 1)

        def open_contact():
            button_inactive()
            hide_frames()
            contact_btn.config(bg = "#037ef3")
            contact_frame.place(x = 0, y = 0, width = (1920-240), height = 880)
            contact_frame.pack(fill = 'both', expand= 1)

            img4 = Image.open(r"C:\Users\Gaura\OneDrive\Desktop\HMS1.0\Images\Hospital.jpg")
            img4 = img4.resize(((1920-250),330), Image.ANTIALIAS)
            self.photoimg4 = ImageTk.PhotoImage(img4)

            lableimg3 = Label(contact_frame, image = self.photoimg4)
            lableimg3.place(x=5, y=5, width = (1920-250), height = 330)

            lbl_stats = Label(contact_frame, font = ("Poppins Bold", 15), text = "Contact\nDetails", bg = "#037ef3", fg = "white")
            lbl_stats.place(x = 90, y = 340, width = 300, height = 150)
            self.lbl_paitent = Label(contact_frame, font = ("Poppins Regular", 15), text = "Vedansh\n12011217", bg = "#00c16e", fg = "white")
            self.lbl_paitent.place(x = 395, y = 340, width = 300, height = 150)
            self.lbl_doctors = Label(contact_frame, font = ("Poppins Regular", 15), text = "Gaurav\n12007335", bg = "#00c16e", fg = "white")
            self.lbl_doctors.place(x = 700, y = 340, width = 300, height = 150)
            self.lbl_beds = Label(contact_frame, font = ("Poppins Regular", 15), text = "Manoj\n12012337", bg = "#00c16e", fg = "white")
            self.lbl_beds.place(x = 1005, y = 340, width = 300, height = 150)
            self.lbl_specialities = Label(contact_frame, font = ("Poppins Regular", 15), text = "INT213\nHospital Management\n System Project", bg = "#00c16e", fg = "white")
            self.lbl_specialities.place(x = 1310, y = 340, width = 300, height = 150)



        def hide_frames():
            home_frame.pack_forget()
            paitent_frame.pack_forget()
            doctor_frame.pack_forget()
            appointment_frame.pack_forget()
            billing_frame.pack_forget()
            contact_frame.pack_forget()

        def button_inactive():
            home_btn.config(bg = "#00c16e")
            paitent_btn.config(bg = "#00c16e")
            doctor_btn.config(bg = "#00c16e")
            appointment_btn.config(bg = "#00c16e")
            billing_btn.config(bg = "#00c16e")
            contact_btn.config(bg = "#00c16e")

        #menu
        menu_frame = Frame(self.root, bg = "#037ef3")
        menu_frame.place(x = 0, y = 190, width = 240, height = 880)

        home_btn = Button(menu_frame, text = "Home", font = ("Poppins Bold", 13), command = open_home, activebackground = "#037ef3", activeforeground = "white", fg = "white", bg = "#00c16e", bd=0, width = 22, cursor = "hand2" )
        home_btn.grid(row = 0, column = 0, pady = 1)
        paitent_btn = Button(menu_frame, text = "Paitent", font = ("Poppins Bold", 13), command = open_paitent, activebackground = "#037ef3", activeforeground = "white", fg = "white", bg = "#00c16e", bd=0, width = 22, cursor = "hand2" )
        paitent_btn.grid(row = 1, column = 0, pady = 1)
        doctor_btn = Button(menu_frame, text = "Doctor", font = ("Poppins Bold", 13), command = open_doctor, activebackground = "#037ef3", activeforeground = "white", fg = "white", bg = "#00c16e", bd=0, width = 22, cursor = "hand2" )
        doctor_btn.grid(row = 2, column = 0, pady = 1)
        appointment_btn = Button(menu_frame, text = "Appointment", font = ("Poppins Bold", 13), command = open_appointment, fg = "white", activebackground = "#037ef3", activeforeground = "white", bg = "#00c16e", bd=0, width = 22, cursor = "hand2" )
        appointment_btn.grid(row = 3, column = 0, pady = 1)
        billing_btn = Button(menu_frame, text = "Billing", font = ("Poppins Bold", 13), command = open_billing, activebackground = "#037ef3", activeforeground = "white", fg = "white", bg = "#00c16e", bd=0, width = 22, cursor = "hand2" )
        billing_btn.grid(row = 4, column = 0, pady = 1)
        contact_btn = Button(menu_frame, text = "Contact", font = ("Poppins Bold", 13), command = open_contact, activebackground = "#037ef3", activeforeground = "white", fg = "white", bg = "#00c16e", bd=0, width = 22, cursor = "hand2" )
        contact_btn.grid(row = 5, column = 0, pady = 1)

        #home page
        home_frame = Frame(main_frame)
        home_frame.place(x = 0, y = 0, width = (1920-240), height = 880)

        img2 = Image.open(r"C:\Users\Gaura\OneDrive\Desktop\HMS1.0\Images\Hospital.jpg")
        img2 = img2.resize(((1920-250),330), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lableimg2 = Label(home_frame, image = self.photoimg2)
        lableimg2.place(x=5, y=5, width = (1920-250), height = 330)

        lbl_stats = Label(home_frame, font = ("Poppins Bold", 15), text = "Current\nStatistics", bg = "#037ef3", fg = "white")
        lbl_stats.place(x = 90, y = 340, width = 300, height = 150)
        self.lbl_paitent = Label(home_frame, font = ("Poppins Regular", 15), text = "Paitent Admitted \n 0", bg = "#00c16e", fg = "white")
        self.lbl_paitent.place(x = 395, y = 340, width = 300, height = 150)
        self.lbl_doctors = Label(home_frame, font = ("Poppins Regular", 15), text = "Doctors Aviliable \n 0", bg = "#00c16e", fg = "white")
        self.lbl_doctors.place(x = 700, y = 340, width = 300, height = 150)
        self.lbl_beds = Label(home_frame, font = ("Poppins Regular", 15), text = "Beds Aviliable \n 100", bg = "#00c16e", fg = "white")
        self.lbl_beds.place(x = 1005, y = 340, width = 300, height = 150)
        self.lbl_specialities = Label(home_frame, font = ("Poppins Regular", 15), text = "Specialities \n 0", bg = "#00c16e", fg = "white")
        self.lbl_specialities.place(x = 1310, y = 340, width = 300, height = 150)

        #Paitent Page
        paitent_frame = Frame(main_frame, bg= 'white')

        #Doctor Page
        doctor_frame = Frame(main_frame, bg= 'white')

        #Appointment Page
        appointment_frame = Frame(main_frame, bg= 'white')

        #Billing Page
        billing_frame = Frame(main_frame, bg= 'white')

        #Contact Page
        contact_frame = Frame(main_frame, bg= 'white')

        

if __name__ == "__main__":
    root = Tk()
    obj = HospitalManagementSystem(root)
    root.state("zoomed")
    root.mainloop()
