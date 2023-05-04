from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from Student_add import Student_add
import os
from mark_attendance import mark_attendance



class Attendance_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("ATTENDANCE MANAGEMENT SYSTEM | Shivam & Molik")


        header = Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",bg="white",fg="blue",font=("verdana", 36,"bold"))
        header.pack(fill=X)

        t_img=Image.open("img/title_logo.png")
        t_img=t_img.resize((96,96), Image.Resampling.LANCZOS)
        self.title_img = ImageTk.PhotoImage(t_img) 
        title_img_Label=Label(header,image = self.title_img,bg="white")
        title_img_Label.pack(side=LEFT,padx=20,pady=5)

        t_img1=Image.open("img/title_logo.png")
        t_img1=t_img1.resize((96,96), Image.Resampling.LANCZOS)
        self.title_img1 = ImageTk.PhotoImage(t_img1) 
        title_img_Label=Label(header,image = self.title_img1,bg="white")
        title_img_Label.pack(side=RIGHT,padx=20,pady=5)


        label_text=Label(self.root,text="Select the Options",fg="Blue",font=("Comicsans",24,"italic"))
        label_text.place(x=540,y=150)
 # Student Button.....................       
        img4 = Image.open("img/student_add.png")
        img4 = img4.resize((210,190), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(self.root, image=self.photoimg4,command=self.Student_add,cursor="hand2")
        b1.place(x=300, y=240, width=210, height=190)


        b1_1 = Button(self.root,text='ADD STUDENT',command=self.Student_add,cursor="hand2",font=("times new roman", 15 , "bold"), bg="brown", fg="white")
        b1_1.place(x=300, y=430, width=210, height=40)

# attendance Button.....................       
        img6 = Image.open("img\mark_attendance.jpg")
        img6 = img6.resize((210,190), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(self.root, image=self.photoimg6, cursor="hand2",command=self.mark_attendance)
        b3.place(x=550, y=240, width=210, height=190)


        b3_1 = Button(self.root,text='MARK ATTENDANCE', cursor="hand2",command=self.mark_attendance,font=("times new roman", 15 , "bold"), bg="brown", fg="white")
        b3_1.place(x=550, y=430, width=210, height=40)




# Exit Button.....................       
        img11 = Image.open("img/exit.png")
        img11 = img11.resize((210,190), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(self.root, image=self.photoimg11, cursor="hand2",command=self.iExit)
        b8.place(x=800, y=240, width=210, height=190)


        b8_1 = Button(self.root,text='EXIT', cursor="hand2",command=self.iExit,font=("times new roman", 15 , "bold"), bg="brown", fg="white")
        b8_1.place(x=800, y=430, width=210, height=40)

        end_frame=Frame(bd=2,bg="white")
        end_frame.place(x=0,y=650,width=1800,height=100)

        developer_label=Label(text="Design & Developer By Shivam & Molik | Copyright: © 2023 ",fg="red",bg="white",font=("Verdana",20,"italic"),)
        developer_label.place(x=250, y=680)


    def open_img(self):
        os.startfile("data")


    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Attendance Management System", "do you want to exit",parent=self.root)
        if  self.iExit > 0:
            self.root.destroy()
        else:
            return


# ==============================Function Buttons====================================
    def Student_add(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_add(self.new_window)
   

    def mark_attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=mark_attendance(self.new_window)


if __name__=="__main__":
    root=Tk()
    obj=Attendance_System(root)
    root.mainloop()
 