from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_recognition
from attendence import Attendence

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

















if __name__ == "__main__":
     root = Tk()
     obj=Face_Recognition_System(root)
     root.mainloop()