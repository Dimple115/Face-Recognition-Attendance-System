from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from login import Login
import mysql.connector
import cv2



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

        name_label=Label(table_frame,text="Name",font=("times new roman",13,"bold"),bg="black",fg="white")
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















if  __name__ == "__main__":
    root = Tk()
    obj=Register(root)
    root.mainloop()