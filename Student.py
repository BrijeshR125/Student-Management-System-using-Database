from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("Times New Roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

        #All variables
        self.roll_no=StringVar()
        self.name=StringVar()
        self.email=StringVar()
        self.gender=StringVar()
        self.contact=StringVar()
        self.dob=StringVar()

        self.searchby=StringVar()
        self.searchtxt=StringVar()

        ManageFrame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        ManageFrame.place(x=20,y=100,width=450,height=620)

        mtitle=Label(ManageFrame,text="Manage Students",bg="crimson",fg="white",font=("Times New Roman",25,"bold"))
        mtitle.grid(row=0,columnspan=2,pady=20)

        lblRoll=Label(ManageFrame,text="Roll No.",bg="crimson",fg="white",font=("Times New Roman",15,"bold"))
        lblRoll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txtRoll=Entry(ManageFrame,textvariable=self.roll_no,font=("Times New Roman",20,"bold"),bd=5,relief=GROOVE)
        txtRoll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lblName=Label(ManageFrame,text="Name",bg="crimson",fg="white",font=("Times New Roman",15,"bold"))
        lblName.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txtName=Entry(ManageFrame,textvariable=self.name,font=("Times New Roman",20,"bold"),bd=5,relief=GROOVE)
        txtName.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lblEmail=Label(ManageFrame,text="Emial ID",bg="crimson",fg="white",font=("Times New Roman",15,"bold"))
        lblEmail.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txtEmail=Entry(ManageFrame,textvariable=self.email,font=("Times New Roman",20,"bold"),bd=5,relief=GROOVE)
        txtEmail.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lblGender=Label(ManageFrame,text="Gender",bg="crimson",fg="white",font=("Times New Roman",15,"bold"))
        lblGender.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        genderCombo=ttk.Combobox(ManageFrame,textvariable=self.gender,font=("Times New Roman",19,"bold"),state="readonly")
        genderCombo["values"]=("Male","Female","Other")
        genderCombo.grid(row=4,column=1,padx=20,pady=10)

        lblContact=Label(ManageFrame,text="Contact",bg="crimson",fg="white",font=("Times New Roman",15,"bold"))
        lblContact.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txtContact=Entry(ManageFrame,textvariable=self.contact,font=("Times New Roman",20,"bold"),bd=5,relief=GROOVE)
        txtContact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lblDOB=Label(ManageFrame,text="D.O.B.",bg="crimson",fg="white",font=("Times New Roman",15,"bold"))
        lblDOB.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        txtDOB=Entry(ManageFrame,textvariable=self.dob,font=("Times New Roman",20,"bold"),bd=5,relief=GROOVE)
        txtDOB.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lblAddress=Label(ManageFrame,text="Address",bg="crimson",fg="white",font=("Times New Roman",15,"bold"))
        lblAddress.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        self.txtAddress=Text(ManageFrame,width=40,height=4,font=("Times New Roman",10,"bold"),bd=5,relief=GROOVE)
        self.txtAddress.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        btnFrame=Frame(ManageFrame,bd=4,relief=RIDGE,bg="crimson")
        btnFrame.place(x=15,y=550,width=420)

        addButton=Button(btnFrame,text="Add",width=10,command=self.addStudent).grid(row=0,column=0,padx=10,pady=10)
        updateButton=Button(btnFrame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deleteButton=Button(btnFrame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearButton=Button(btnFrame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        DetailsFrame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        DetailsFrame.place(x=500,y=100,width=800,height=620)

        lblSearch=Label(DetailsFrame,text="Search by",bg="crimson",fg="white",font=("Times New Roman",20,"bold"))
        lblSearch.grid(row=0,column=0,padx=20,pady=10,sticky="w")
        searchCombo=ttk.Combobox(DetailsFrame,textvariable=self.searchby,width=10,font=("Times New Roman",13,"bold"),state="readonly")
        searchCombo["values"]=("Roll_no","Name","Contact")
        searchCombo.grid(row=0,column=1,padx=20,pady=10)
        txtSearch=Entry(DetailsFrame,textvariable=self.searchtxt,width=15,font=("Times New Roman",10,"bold"),bd=5,relief=GROOVE)
        txtSearch.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        searchButton=Button(DetailsFrame,text="Search",width=10,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showButton=Button(DetailsFrame,text="Show All",width=10,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        tableFrame=Frame(DetailsFrame,bd=4,relief=RIDGE,bg="crimson")
        tableFrame.place(x=10,y=70,width=760,height=550)

        scrollx=Scrollbar(tableFrame,orient=HORIZONTAL)
        scrolly=Scrollbar(tableFrame,orient=VERTICAL)
        self.studTable=ttk.Treeview(tableFrame,columns=("Roll","Name","Email","Gender","Contact","D.O.B.","Address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.studTable.xview)
        scrolly.config(command=self.studTable.yview)
        self.studTable.heading("Roll",text="Roll No.")
        self.studTable.heading("Name",text="Name")
        self.studTable.heading("Email",text="Email ID")
        self.studTable.heading("Gender",text="Gender")
        self.studTable.heading("Contact",text="Contact")
        self.studTable.heading("D.O.B.",text="D.O.B.")
        self.studTable.heading("Address",text="Address")
        self.studTable["show"]="headings"
        self.studTable.column("Roll",width=100)
        self.studTable.column("Name",width=100)
        self.studTable.column("Email",width=100)
        self.studTable.column("Gender",width=100)
        self.studTable.column("Contact",width=100)
        self.studTable.column("D.O.B.",width=100)
        self.studTable.column("Address",width=100)
        self.studTable.pack(fill=BOTH,expand=1)
        self.studTable.bind("<ButtonRelease-1>",self.getCursor)
        self.fetch_data()

    def addStudent(self):
        if self.roll_no.get()=="" or self.name.get()=="" or self.email.get()=="" or self.gender.get()=="" or self.contact.get()=="" or self.dob.get()=="" or self.txtAddress.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:    
            con=pymysql.connect(host="localhost",user="root",database="student")
            cur=con.cursor()
            cur.execute("insert into Students values(%s,%s,%s,%s,%s,%s,%s)",(self.roll_no.get(),self.name.get(),self.email.get(),self.gender.get(),self.contact.get(),self.dob.get(),self.txtAddress.get('1.0',END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",database="student")
        cur=con.cursor()
        cur.execute("select * from Students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.studTable.delete(*self.studTable.get_children())
            for row in rows:
                self.studTable.insert('',END,values=row)
                con.commit()
        con.close()

    def clear(self):
        self.roll_no.set("")
        self.name.set("")
        self.email.set("")
        self.gender.set("")
        self.contact.set("")
        self.dob.set("")
        self.txtAddress.delete("1.0",END)

    def getCursor(self,eve):
        currow=self.studTable.focus()
        contents=self.studTable.item(currow)
        row=contents['values']
        self.roll_no.set(row[0])
        self.name.set(row[1])
        self.email.set(row[2])
        self.gender.set(row[3])
        self.contact.set(row[4])
        self.dob.set(row[5])
        self.txtAddress.delete("1.0",END)
        self.txtAddress.insert(END,row[6])

    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",database="student")
        cur=con.cursor()
        cur.execute("update Students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(self.name.get(),self.email.get(),self.gender.get(),self.contact.get(),self.dob.get(),self.txtAddress.get('1.0',END),self.roll_no.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",database="student")
        cur=con.cursor()
        cur.execute("delete from Students where roll_no=%s",self.roll_no.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        if self.searchby.get()=="" or self.searchtxt.get()=="":
            messagebox.showerror("Error","Search by or Search text field is required")
        else:
            con=pymysql.connect(host="localhost",user="root",database="student")
            cur=con.cursor()
            cur.execute("select * from Students where "+str(self.searchby.get())+" LIKE '%"+str(self.searchtxt.get())+"%'")
            rows=cur.fetchall()
            if len(rows)!=0:
                messagebox.showinfo("Success","Record has been found")
                self.studTable.delete(*self.studTable.get_children())
                for row in rows:
                    self.studTable.insert('',END,values=row)
                    con.commit()
            else:
                messagebox.showinfo("Success","No such record found")
            con.close()
                    
root=Tk()
sd=Student(root)
root.mainloop()
