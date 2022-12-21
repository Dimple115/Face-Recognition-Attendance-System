from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from main import Face_Recognition_System
from student import Student

from train import Train
from face_recognition import Face_recognition
from attendence import Attendence



def main():
    new_window=Tk()
    app=Login(new_window)
    new_window.mainloop()


class Login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login")

       
        

        img_top=Image.open(r"college_images/u.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_1lbl=Label(self.root,image=self.photoimg_top)
        f_1lbl.place(x=0,y=55,width=1530,height=720)

        table_frame=Frame(f_1lbl,bd=2,relief=RIDGE,bg="black")
        table_frame.place(x=510,y=170,width=340,height=450)

        img=Image.open(r"college_images/LoginIconAppl.png")
        img=img.resize((100,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_1lbl=Label(image=self.photoimg,bg="black",borderwidth=0)
        f_1lbl.place(x=630,y=230,width=100,height=100)

        stuid_label=Label(table_frame,text="Get Started",font=("times new roman",20,"bold"),bg="black",fg="white")
        stuid_label.place(x=95,y=100)

        #student name
        stuname_label=Label(table_frame,text="UserName:",font=("times new roman",12,"bold"),bg="black",fg="white")
        stuname_label.place(x=50,y=155)

        self.studentname_entry=ttk.Entry(table_frame,width=20,font=("times new roman",12,"bold"))
        self.studentname_entry.place(x=40,y=180,width=270)

        #student name
        password_label=Label(table_frame,text="Password:",font=("times new roman",12,"bold"),bg="black",fg="white")
        password_label.place(x=50,y=225)

        self.studpassword_entry=ttk.Entry(table_frame,width=20,font=("times new roman",12,"bold"))
        self.studpassword_entry.place(x=40,y=250,width=270)

        login_btn=Button(table_frame,command=self.login,text="Login",font=("times new roman",12,"bold"),borderwidth=0,bg="red",fg="white",width="17")
        login_btn.place(x=110,y=300,width=120,height=40)

        register_btn=Button(table_frame,text="Register",command=self.register_win ,font=("times new roman",12,"bold"),bg="red",fg="white",width="17")
        register_btn.place(x=110,y=350,width=120)

    def register_win(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login (self):
        if self.studentname_entry.get()=="" or self.studpassword_entry.get()=="":
            messagebox.showerror("Error","All field required")
        elif self.studentname_entry.get()=="kapu" or self.studpassword_entry.get()=="ashu":
            messagebox.showerror("Success")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="MYSQL15",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                      self.studentname_entry.get(),
                                                                      self.studpassword_entry.get() 


            ))

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=Face_Recognition_System(self.new_window)
                else:
                        if not open_main:
                           return
            
            conn.commit()
            conn.close()

            



class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Register")

        self.var_studentname=StringVar()
        self.var_studentemail=StringVar()
        self.var_studentphnno=StringVar()
        self.var_studentpassword=StringVar()
        self.var_studentconfirmpassword=StringVar()
        

        img_top=Image.open(r"college_images/university.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_1lbl=Label(self.root,image=self.photoimg_top)
        f_1lbl.place(x=0,y=55,width=1530,height=720)

        table_frame=Frame(f_1lbl,bd=2,relief=RIDGE,bg="black")
        table_frame.place(x=450,y=170,width=500,height=450)

        reg_label=Label(table_frame,text="Register Here",font=("times new roman",20,"bold"),bg="black",fg="white")
        reg_label.place(x=20,y=20)

        name_label=Label(table_frame,text="UserName",font=("times new roman",13,"bold"),bg="black",fg="white")
        name_label.place(x=40,y=80)

        self.studentname_entry=ttk.Entry(table_frame,textvariable=self.var_studentname,width=20,font=("times new roman",12,"bold"))
        self.studentname_entry.place(x=40,y=100,width=270)

        email_label=Label(table_frame,text="Email",font=("times new roman",13,"bold"),bg="black",fg="white")
        email_label.place(x=40,y=125)

        self.studentemail_entry=ttk.Entry(table_frame,textvariable=self.var_studentemail,width=20,font=("times new roman",12,"bold"))
        self.studentemail_entry.place(x=40,y=145,width=270)

        phnno_label=Label(table_frame,text="Phone No.",font=("times new roman",13,"bold"),bg="black",fg="white")
        phnno_label.place(x=40,y=170)

        self.studentphnno_entry=ttk.Entry(table_frame,textvariable=self.var_studentphnno,width=20,font=("times new roman",12,"bold"))
        self.studentphnno_entry.place(x=40,y=190,width=270)

        password_label=Label(table_frame,text="Password",font=("times new roman",13,"bold"),bg="black",fg="white")
        password_label.place(x=40,y=215)

        self.studentpassword_entry=ttk.Entry(table_frame,textvariable=self.var_studentpassword,width=20,font=("times new roman",12,"bold"))
        self.studentpassword_entry.place(x=40,y=235,width=270)

        confirmpassword_label=Label(table_frame,text="Confirm Password",font=("times new roman",13,"bold"),bg="black",fg="white")
        confirmpassword_label.place(x=40,y=260)

        self.studentconfirmpassword_entry=ttk.Entry(table_frame,textvariable=self.var_studentconfirmpassword,width=20,font=("times new roman",12,"bold"))
        self.studentconfirmpassword_entry.place(x=40,y=280,width=270)

        register_btn=Button(table_frame,command=self.register,text="Register",font=("times new roman",12,"bold"),borderwidth=0,bg="red",fg="white",width="17")
        register_btn.place(x=50,y=330,width=120,height=40)

        login_btn=Button(table_frame,text="Login" ,font=("times new roman",12,"bold"),bg="red",fg="white",width="17")
        login_btn.place(x=50,y=380,width=120)

    def register (self):
        if self.var_studentname.get()=="" or self.var_studentemail.get()=="":
            messagebox.showerror("Error","All field required")
        elif self.var_studentpassword.get()!=self.var_studentconfirmpassword.get():
            messagebox.showerror("Error","Password and Confirm password not same")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="MYSQL15",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_studentemail.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","user already exits")
            else:
                my_cursor.execute("insert into register values(%s, %s, %s, %s, %s)",(
                                                                                        self.var_studentname.get(),
                                                                                        self.var_studentemail.get(),
                                                                                        self.var_studentphnno.get(),
                                                                                        self.var_studentpassword.get(),
                                                                                        self.var_studentconfirmpassword.get()
                                                                                                                                                                                                                                           
                    ))
            
            conn.commit()
            
            conn.close()
            messagebox.showinfo("Success","Student registered succesfully")





        

class Face_Recognition_System:
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

        title_lbl=Label(bg_img,text="Face Recognition Attendance System Software",font=("times new roman",30,"bold"),bg="white",fg="sea green")
        title_lbl.place(x=0,y=0,width=1500,height=40)

        #student btn

        img4=Image.open(r"C:\Users\dimple\Desktop\Face recognition system\Images fr\stu1.png")
        img4=img4.resize((700,260),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=120,y=100,width=220,height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="sea green")
        b1_1.place(x=120,y=300,width=220,height=40)


        #Detect Face btn

        img5=Image.open(r"C:\Users\dimple\Desktop\Face recognition system\Images fr\face3.jpg")
        img5=img5.resize((250,260),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=450,y=100,width=220,height=200)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="white",fg="sea green")
        b1_1.place(x=450,y=300,width=220,height=40)

        #Attendance btn

        img6=Image.open(r"C:\Users\dimple\Desktop\Face recognition system\Images fr\aten1.jpg")
        img6=img6.resize((300,260),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence)
        b1.place(x=780,y=100,width=220,height=200)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendence,font=("times new roman",15,"bold"),bg="white",fg="sea green")
        b1_1.place(x=780,y=300,width=220,height=40)

        #Help btn

        img7=Image.open(r"C:\Users\dimple\Desktop\Face recognition system\Images fr\help1.jpg")
        img7=img7.resize((300,260),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=200)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="sea green")
        b1_1.place(x=1100,y=300,width=220,height=40)
 
        #Train Data

        img8=Image.open(r"C:\Users\dimple\Desktop\Face recognition system\Images fr\train.jpg")
        img8=img8.resize((1500,690),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=115,y=400,width=220,height=200)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="white",fg="sea green")
        b1_1.place(x=115,y=600,width=220,height=40)

        #Photos

        img9=Image.open(r"C:\Users\dimple\Desktop\Face recognition system\Images fr\photo1.png")
        img9=img9.resize((300,260),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=445,y=400,width=220,height=200)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="sea green")
        b1_1.place(x=445,y=600,width=220,height=40)

        #Developer 

        img10=Image.open(r"C:\Users\dimple\Desktop\Face recognition system\Images fr\dev.jpg")
        img10=img10.resize((300,260),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=775,y=400,width=220,height=200)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="sea green")
        b1_1.place(x=775,y=600,width=220,height=40)
       
        #Exit 

        img11=Image.open(r"C:\Users\dimple\Desktop\Face recognition system\Images fr\exit1.jpg")
        img11=img11.resize((300,260),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1105,y=400,width=220,height=200)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="sea green")
        b1_1.place(x=1105,y=600,width=220,height=40)

    def open_img(self):
        os.startfile("data")

        #==========================functions button=============================

    def student_details(self):
              self.new_window=Toplevel(self.root)
              self.app=Student(self.new_window) #declaration



    def train_data(self):
              self.new_window=Toplevel(self.root)
              self.app=Train(self.new_window) #declaration
    

    def face_data(self):
              self.new_window=Toplevel(self.root)
              self.app=Face_recognition(self.new_window) #declaration

    def attendence(self):
              self.new_window=Toplevel(self.root)
              self.app=Attendence(self.new_window) #declaration









if  __name__ == "__main__":
   main()
