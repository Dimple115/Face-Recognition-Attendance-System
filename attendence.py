from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

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

        title_lbl=Label(bg_img,text="Student Attendence Management System",font=("times new roman",30,"bold"),bg="white",fg="Red")
        title_lbl.place(x=0,y=0,width=1500,height=40)

        #frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1450,height=640)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=650,height=580)

        img4=Image.open(r"C:\Users\dimple\Desktop\Face recognition system\Images fr\stu1.png")
        img4=img4.resize((470,100),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        f_1lbl=Label(Left_frame,image=self.photoimg4)
        f_1lbl.place(x=5,y=0,width=640,height=100)


        

        #left frame
        leftinside_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        leftinside_frame.place(x=10,y=110,width=650,height=150)

        #label and entry

        #attendence id
        stuid_label=Label(leftinside_frame,text="Attendence Id:",font=("times new roman",12,"bold"),bg="white")
        stuid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentid_entry=ttk.Entry(leftinside_frame,width=20,font=("times new roman",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        stuname_label=Label(leftinside_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        stuname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(leftinside_frame,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #roll no.
        roll_label=Label(leftinside_frame,text="Roll No.:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(leftinside_frame,width=20,font=("times new roman",12,"bold"))
        rollno_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #date
        roll_label=Label(leftinside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(leftinside_frame,width=20,font=("times new roman",12,"bold"))
        rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #time
        roll_label=Label(leftinside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(leftinside_frame,width=20,font=("times new roman",12,"bold"))
        rollno_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Attendence
        classdiv_label=Label(leftinside_frame,text="Attendence:",font=("times new roman",12,"bold"),bg="white")
        classdiv_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)


        div_combo=ttk.Combobox(leftinside_frame,font=("times new roman",12,"bold"),state="readonly",width="18")
        div_combo["values"]=("Select","Present","Absent","Leave")
        div_combo.current(0)
        div_combo.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #button frame 1
        btn_frame=Frame(leftinside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=110,width=645,height=35)

        save_btn=Button(btn_frame,text="Import Csv",command=self.importcsv,font=("times new roman",12,"bold"),bg="blue",fg="white",width="17")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export Csv",command=self.exportcsv,font=("times new roman",12,"bold"),bg="blue",fg="white",width="17")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",font=("times new roman",12,"bold"),bg="blue",fg="white",width="17")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",font=("times new roman",12,"bold"),bg="blue",fg="white",width="17")
        reset_btn.grid(row=0,column=3)

        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=640,height=570)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=620,height=455)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="Attendence id")
        self.AttendenceReportTable.heading("roll",text="Roll No.")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence")

        self.AttendenceReportTable["show"]="headings"
       


        self.AttendenceReportTable.pack(fill=BOTH,expand=1)

        #fetch data

    def fetchdata(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)
    

    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="opencsv",filetypes=(("CSV FILE","*.csv"),("ALL FILE","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="opencsv",filetypes=(("CSV FILE","*.csv"),("ALL FILE","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported","Your data exported"+"successfully")
        except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
        














if  __name__ == "__main__":
    root = Tk()
    obj=Attendence(root)
    root.mainloop()