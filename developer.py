from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Developer",font=("times new roman",30,"bold"),bg="white",fg="Red")
        title_lbl.place(x=0,y=0,width=1500,height=40)

        img_top=Image.open(r"college_images/dev.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_1lbl=Label(self.root,image=self.photoimg_top)
        f_1lbl.place(x=0,y=55,width=1530,height=720)

        table_frame=Frame(f_1lbl,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=1000,y=0,width=500,height=655)

        img_top=Image.open(r"college_images/dev.jpg")
        img_top=img_top.resize((1530,200),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_1lbl=Label(table_frame,image=self.photoimg_top)
        f_1lbl.place(x=300,y=0,width=200,height=200)











if  __name__ == "__main__":
    root = Tk()
    obj=Developer(root)
    root.mainloop()