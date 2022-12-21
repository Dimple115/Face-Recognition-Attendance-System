from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


#=====================variables=================
        self.var_dep=StringVar()
        self.var_cou=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_stdid=StringVar()
        self.var_stdname=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_photo=StringVar()
        self.var_radio1=StringVar()
        

 #first img

        img=Image.open(r"C:\Users\dimple\Desktop\Face recognition system\Images fr\facial-recognition-ID-2-adobe_searchsitetablet_520X173.jpg")
        img=img.resize((450,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_1lbl=Label(self.root,image=self.photoimg)
        f_1lbl.place(x=0,y=0,width=450,height=100)
        
        #second img

        img1=Image.open(r"C:\Users\dimple\Desktop\Face recognition system\Images fr\facial-recognition-ID-2-adobe_searchsitetablet_520X173.jpg")
        img1=img1.resize((450,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_1lbl=Label(self.root,image=self.photoimg1)
        f_1lbl.place(x=450,y=0,width=450,height=100)
        
        #third img

        img2=Image.open(r"C:\Users\dimple\Desktop\Face recognition system\Images fr\facial-recognition-ID-2-adobe_searchsitetablet_520X173.jpg")
        img2=img2.resize((470,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_1lbl=Label(self.root,image=self.photoimg2)
        f_1lbl.place(x=900,y=0,width=470,height=100)

        #bgimage

        img3=Image.open(r"C:\Users\dimple\Desktop\Face recognition system\Images fr\poly-bg-1.jpg")
        img3=img3.resize((1500,690),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1500,height=690)

        title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",30,"bold"),bg="white",fg="Red")
        title_lbl.place(x=0,y=0,width=1500,height=40)

        #frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1450,height=640)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=650,height=580)

        img4=Image.open(r"C:\Users\dimple\Desktop\Face recognition system\Images fr\stu1.png")
        img4=img4.resize((470,100),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        f_1lbl=Label(Left_frame,image=self.photoimg4)
        f_1lbl.place(x=5,y=0,width=640,height=100)

        #Current Course
        Current_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Course Detail",font=("times new roman",12,"bold"))
        Current_frame.place(x=10,y=110,width=650,height=120)

        #Department
        dep_label=Label(Current_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(Current_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width="20")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        cou_label=Label(Current_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        cou_label.grid(row=0,column=2,padx=10,sticky=W)

        cou_combo=ttk.Combobox(Current_frame,textvariable=self.var_cou,font=("times new roman",12,"bold"),state="readonly",width="20")
        cou_combo["values"]=("Select Course","FE","SE","TE","BE")
        cou_combo.current(0)
        cou_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(Current_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(Current_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width="20")
        year_combo["values"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        sem_label=Label(Current_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(Current_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width="20")
        sem_combo["values"]=("Select Semester","First","Second","Third","Fourth")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student Information
        Class_student_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        Class_student_frame.place(x=10,y=250,width=650,height=320)

        #student id
        stuid_label=Label(Class_student_frame,text="Student Id:",font=("times new roman",12,"bold"),bg="white")
        stuid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentid_entry=ttk.Entry(Class_student_frame,textvariable=self.var_stdid,width=20,font=("times new roman",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        stuname_label=Label(Class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        stuname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(Class_student_frame,textvariable=self.var_stdname,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        classdiv_label=Label(Class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        classdiv_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)


        div_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width="18")
        div_combo["values"]=("Select Division","A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #roll no.
        roll_label=Label(Class_student_frame,text="Roll No.:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(Class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gen_label=Label(Class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gen_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #gender_entry=ttk.Entry(Class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        #gender_entry.grid(row=2,column= 1,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width="18")
        gender_combo["values"]=("Select Gender","MALE","FEMALE","OTHER")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #Date of birth
        dob_label=Label(Class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(Class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email
        email_label=Label(Class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(Class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column= 1,padx=10,pady=5,sticky=W)

        #phone no.
        phn_label=Label(Class_student_frame,text="Phone No.:",font=("times new roman",12,"bold"),bg="white")
        phn_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phn_entry=ttk.Entry(Class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phn_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        add_label=Label(Class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        add_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        add_entry=ttk.Entry(Class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        add_entry.grid(row=4,column= 1,padx=10,pady=5,sticky=W)

        #teachers name
        teach_label=Label(Class_student_frame,text="Teachers Name:",font=("times new roman",12,"bold"),bg="white")
        teach_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        taech_entry=ttk.Entry(Class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        taech_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        
        #radio button 1
        self.var_radiobtn1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_student_frame,variable=self.var_radiobtn1,text="Take a Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        
        radiobtn2=ttk.Radiobutton(Class_student_frame,variable=self.var_radiobtn1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)

        #button frame 1
        btn_frame=Frame(Class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=645,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data ,font=("times new roman",12,"bold"),bg="blue",fg="white",width="17")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",12,"bold"),bg="blue",fg="white",width="17")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",12,"bold"),bg="blue",fg="white",width="17")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white",width="17")
        reset_btn.grid(row=0,column=3)

        #button frame 2
        btn_frame2=Frame(Class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame2.place(x=0,y=235,width=645,height=35)
        
        tphoto_btn=Button(btn_frame2,command=self.generate_dataset,text="Take Photo Sample",font=("times new roman",12,"bold"),bg="blue",fg="white",width="35")
        tphoto_btn.grid(row=0,column=0)

        uphoto_btn=Button(btn_frame2,text="Update Photo Sample",font=("times new roman",12,"bold"),bg="blue",fg="white",width="35")
        uphoto_btn.grid(row=0,column=1)



        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=640,height=570)

        img5=Image.open(r"C:\Users\dimple\Desktop\Face recognition system\Images fr\facial-recognition-ID-2-adobe_searchsitetablet_520X173.jpg")
        img5=img5.resize((470,100),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        f_1lbl=Label(Right_frame,image=self.photoimg4)
        f_1lbl.place(x=5,y=0,width=640,height=100)


        #===========Search System=============
        #seacrch frame
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=10,y=105,width=625,height=80)

        Search_label=Label(search_frame,text="Search By:",font=("times new roman",14,"bold"),bg="red",fg="white")
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width="15")
        search_combo["values"]=("Select","Roll_NO","Phone No","TE","BE")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",font=("times new roman",12,"bold"),bg="blue",fg="white",width="10")
        search_btn.grid(row=0,column=3,padx=5)

        showall_btn=Button(search_frame,text="Show All",font=("times new roman",12,"bold"),bg="blue",fg="white",width="10")
        showall_btn.grid(row=0,column=4,padx=5)

        #===========Table frame==========
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=190,width=625,height=350)

        #scroll Bar

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","cou","year","sem","stuid","stuname","classdiv","roll","gen","dob","email","phn","add","teach","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("cou",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("stuid",text="Student Id")
        self.student_table.heading("stuname",text="Student Name")
        self.student_table.heading("classdiv",text="Class Division")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("gen",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phn",text="Phone No.")
        self.student_table.heading("add",text="Address")
        self.student_table.heading("teach",text="Teacher Name")
        self.student_table.heading("photo",text="Photo Sample")
       

        self.student_table["show"]="headings"

        self.student_table.column("dep",width="100")
        self.student_table.column("cou",width="100")
        self.student_table.column("year",width="100")
        self.student_table.column("sem",width="100")
        self.student_table.column("stuid",width="100")
        self.student_table.column("stuname",width="100")
        self.student_table.column("classdiv",width="100")
        self.student_table.column("roll",width="100")
        self.student_table.column("gen",width="100")
        self.student_table.column("dob",width="100")
        self.student_table.column("email",width="100")
        self.student_table.column("phn",width="100")
        self.student_table.column("add",width="100")
        self.student_table.column("teach",width="100")
        self.student_table.column("photo",width="200")
       
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #====================function declaration==================

    def add_data(self):
            if self.var_dep.get()=="Select Department" or self.var_stdname.get()=="" or self.var_stdid.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="MYSQL15",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                                                                                                                            self.var_dep.get(),
                                                                                                                            self.var_cou.get(),
                                                                                                                            self.var_year.get(),
                                                                                                                            self.var_semester.get(),
                                                                                                                            self.var_stdid.get(),
                                                                                                                            self.var_stdname.get(),
                                                                                                                            self.var_div.get(),
                                                                                                                            self.var_roll.get(),
                                                                                                                            self.var_gender.get(),
                                                                                                                            self.var_dob.get(),
                                                                                                                            self.var_email.get(),
                                                                                                                            self.var_phone.get(),
                                                                                                                            self.var_address.get(),
                                                                                                                            self.var_teacher.get(),
                                                                                                                            self.var_radiobtn1.get()                                                                                                               
                    ))

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Student details has been added succesfully",parent=self.root)

                except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #===========================Fetch data========================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="MYSQL15",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #========================get cursor========================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_cou.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_stdid.set(data[4]),
        self.var_stdname.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radiobtn1.set(data[14]) 

    # ======update function======
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stdname.get()=="" or self.var_stdid.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update student details",parent=self.root)
                if update > 0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="MYSQL15",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,student_name=%s,division=%s,roll=%s,dob=%s,gender=%s,email=%s,phone=%s,address=%s,teacher=%s,photo=%s where student_id=%s",(

                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                            self.var_cou.get(),
                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                                            
                                                                                                                                                                                                            self.var_stdname.get(),
                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                                            self.var_radiobtn1.get(),
                                                                                                                                                                                                            self.var_stdid.get()
                                                                                                                                                                                                                                                      
                                                                                                                                                                                                        ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #============delete function======
    def delete_data(self):
        if self.var_stdid.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete page","Do you want to delete student details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="MYSQL15",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_stdid.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #==========reset data======
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_cou.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_stdid.set(""),
        self.var_stdname.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radiobtn1.set("") 

    #======================Generate data Set or Take a Photo Sample======================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_stdname.get()=="" or self.var_stdid.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="MYSQL15",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,student_name=%s,division=%s,roll=%s,dob=%s,gender=%s,email=%s,phone=%s,address=%s,teacher=%s,photo=%s where student_id=%s",(

                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                            self.var_cou.get(),
                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                                            
                                                                                                                                                                                                            self.var_stdname.get(),
                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                                            self.var_radiobtn1.get(),
                                                                                                                                                                                                            self.var_stdid.get()==id+1
                                                                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #=============Load predefined data on face frontals from opencv=================
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #Minimun neighbour = 5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 









if  __name__ == "__main__":
    root = Tk()
    obj=Student(root)
    root.mainloop()
