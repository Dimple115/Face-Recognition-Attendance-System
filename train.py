from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="Train Data Set",font=("times new roman",30,"bold"),bg="white",fg="Red")
        title_lbl.place(x=0,y=0,width=1500,height=40)

        img_top=Image.open(r"Images fr\facial-recognition-ID-2-adobe_searchsitetablet_520X173.jpg")
        img_top=img_top.resize((1530,355),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_1lbl=Label(self.root,image=self.photoimg_top)
        f_1lbl.place(x=0,y=55,width=1530,height=355)


#=============button=======
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=360,width=1530,height=60)


        img_bottom=Image.open(r"Images fr\facial-recognition-ID-2-adobe_searchsitetablet_520X173.jpg")
        img_bottom=img_bottom.resize((1530,355),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_1lbl=Label(self.root,image=self.photoimg_bottom)
        f_1lbl.place(x=0,y=455,width=1530,height=355)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert("L")  #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #=================== train the classifier and save ==============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data set completed!!!")










if  __name__ == "__main__":
    root = Tk()
    obj=Train(root)
    root.mainloop()
