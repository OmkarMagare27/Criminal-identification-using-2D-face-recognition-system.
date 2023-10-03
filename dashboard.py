import cv2
import numpy as np 
import sqlite3
import os
from PIL import ImageTk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import PIL.Image, PIL.ImageTk



import mysql.connector as con
import tkinter.messagebox
global var
import TrainModule
from dbConnection import view_all_attendance
from dbConnection import conn5
from PIL import ImageTk,Image

global screen

    
def main_screen():
    global screen3
    screen3=Tk()

    C= Canvas(screen3, height=250, width=300)
    filename = ImageTk.PhotoImage(Image.open('186040.gif'))
    background_label = Label(screen3, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.create_image(0,0,anchor=NW, image=filename)
    C.pack()
    screen3.title("DASHBOARD")
    screen3.geometry('720x720')
    filename.image2 =ImageTk.PhotoImage(Image.open('186040.gif'))
    #image = ImageTk.PhotoImage(image2)
    w = filename.image2.width()
    h = filename.image2.height()
    screen3.geometry('%dx%d+0+0' % (w,h))
    Label(screen3, text="Smart CCTV Surveillance for Criminal Detection", bg="Gray", height=2, width=250,font=("Arial Bold", 24)).pack()

    tool_bar = Frame(width=50, height=185, bg='lightgrey')
    tool_bar.pack(side='left', fill='both', padx=1, pady=1, expand=True)
 
    filter_bar = Frame(width=50, height=185, bg='lightgrey')
    filter_bar.pack(side='right', fill='both', padx=1, pady=1, expand=True)


    
    #Label(tool_bar, bg="blue").pack()
    b1 =  Button(tool_bar,text="Add police Station",height=2,width=50,bg="Black",fg="blue",font=("Arial Bold", 15), command=add_police_station)
    b1.pack(padx=5, pady=5)

   
    #Label(screen3, text="", bg="yellow").pack()
    b3 =  Button(tool_bar,text="View Police Station",height=2,width=50,bg="Black",fg="yellow",font=("Arial Bold", 15), command=view_police1)
    b3.pack(padx=5, pady=5)

   


    #Label(screen3, text="", bg="white").pack()
    b5 =  Button(tool_bar,text="Add Criminal Record",height=2,width=50,bg="black",fg="blue",font=("Arial Bold", 15),command=add_criminal)
    
    b5.pack(padx=5, pady=5)
    Label(screen3, text="", bg="white").pack()
    b6=Button(filter_bar,text="Train Model",height=2,width=50,bg="black",fg="red",font=("Arial Bold", 15),command=train_model)
    b6.pack(padx=5, pady=5)
    #Label(screen3, text="", bg="white").pack()
    b7= Button(filter_bar, text="Live Camera Feeding",height=2,width=50,bg="black",fg="yellow",font=("Arial Bold", 15),command=mark_attnd)
    b7.pack(padx=5, pady=5)
    #Label(screen3, text="", bg="white").pack()
    b8 = Button(filter_bar, text="Exit", height=2, width=50,bg="black",fg="blue",font=("Arial Bold", 15),command=screen3.destroy)
    b8.pack(padx=5, pady=5)



    C= Canvas(screen3)
    filename = ImageTk.PhotoImage(Image.open('186040.gif'))
    background_label = Label(screen3, image=filename)
    C.pack()
    

    

    Label(screen3, text="", bg="green").pack()
    b9 =  Button(screen3,text="Exit",height=2,width=50,bg="Black",fg="green",font=("Arial Bold", 15),command=screen3.destroy)
    b9.pack()




def train_model():
    TrainModule.train1()
import FaceRecognation
def mark_attnd():
    
    FaceRecognation.mark_attend()



def add_criminal():
    global screen3
    global name1_
    global mobile1_
    global class1_
    global div1_
    global adh_
    global em_
    global variable
    screen3=Toplevel(screen3)
    screen3.configure(background='white')
    screen3.geometry('1280x720')
    Label(screen3, text="Criminal Identification", font=("Arial Bold", 25),bg="grey",width=250,height=2).pack()
    Label(screen3, text="", bg="white").pack()
    Label(screen3, text="", bg="white").pack()
    
    name = Label(screen3, text="Name", height=2, bg="white",font=("Arial Bold", 11))
    name.pack()
    name1_ = Entry(screen3, width=60)
    name1_.pack()
    mobile = Label(screen3, text="mobile", height=2, bg="white",font=("Arial Bold", 11))
    mobile.pack()
    mobile1_ = Entry(screen3, width=60)
    mobile1_.pack()

    class_ = Label(screen3, text="Address", height=2, bg="white",font=("Arial Bold", 11))
    class_.pack()
    class1_ = Entry(screen3, width=60)
    class1_.pack()

    div_ = Label(screen3, text="Crimes", height=2, bg="white",font=("Arial Bold", 11))
    div_.pack()
    div1_ = Entry(screen3, width=60)
    div1_.pack()

    adh_ = Label(screen3, text="Adhar Number", height=2, bg="white",font=("Arial Bold", 11))
    adh_.pack()
    adh_ = Entry(screen3, width=60)
    adh_.pack()

    em_ = Label(screen3, text="Email", height=2, bg="white",font=("Arial Bold", 11))
    em_.pack()
    em_ = Entry(screen3, width=60)
    em_.pack()

    OPTIONS = [
        "Select Criminal Type",
    "Green",
    "Red",
    "Yellow"
    ] #etc



    variable = StringVar(screen3)
    variable.set(OPTIONS[0]) # default value

    w = OptionMenu(screen3, variable, *OPTIONS)
    w.pack()


    Label(screen3, text="", bg="white").pack()
    Label(screen3, text="", bg="white").pack()
    login = Button(screen3, text="Add Record", height=2, width=30,command=record_faces,bg="black",fg="white",font=("Arial Bold", 13))
    login.pack()

def view_police1():
    screen3.destroy()
    import view_police
    



def record_faces():
    a=name1_.get()
    b=mobile1_.get()
    c=div1_.get()
    d=class1_.get()
    e=adh_.get()
    f=em_.get()
    g=variable.get()
    
    print(a)
    path1 = 'dataset'
    model_detector='opencv_face_detector.pbtxt'
    imagePaths = [os.path.join(path1,f) for f in os.listdir(path1)]
    print(imagePaths)
  
    id=1;
    for imagePath in imagePaths:
    
    
        print(os.path.split(imagePath)[-1].split('.')[2])

    
        ID = int(os.path.split(imagePath)[-1].split('.')[2])
        if ID>id:
            id=ID
    if not os.path.exists('./dataset'):
        os.makedirs('./dataset')
#c = conn.cursor()
    face_cascade = cv2.CascadeClassifier('haar.xml')
    cap = cv2.VideoCapture(0)
    #uname = input("Enter your name: ")

    sampleNum = id+20
    while True:
      ret, img = cap.read()
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray, 1.3, 5)
      for (x,y,w,h) in faces:
        id = id+1
        cv2.imwrite("dataset/User."+str(a)+"."+str(id)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        cv2.waitKey(100)
        conn5(id,a,b,d,c,e,f,g) 
      cv2.imshow('img',img)
      cv2.waitKey(1);
      if id > sampleNum:
         break
    cap.release()
    messagebox.showinfo("Information", "Criminal Record Added Successfully.")
    
    #conn.commit()
    #conn.close()
    cv2.destroyAllWindows()



def add_police_station():
    global screen3
    

    global head_name_log
    global address_log
    global lat__log
    global long__log
    global email_log
    global mobile_log
    
    screen3=Toplevel(screen3)
    screen3.configure(background='white')
    screen3.geometry('1280x720')
    Label(screen3, text="Add Police Station", font=("Arial Bold", 25),bg="grey",width=250,height=2).pack()
    Label(screen3, text="", bg="white").pack()
    Label(screen3, text="", bg="white").pack()

    head_name = Label(screen3, text="Head Name", fg="Blue", height=2,font=("Arial Bold", 11))
    head_name.pack()
    head_name_log = Entry(screen3, width=60)
    head_name_log.pack()
    
    address = Label(screen3, text="Address", fg="Blue", height=2,font=("Arial Bold", 11))
    address.pack()
    address_log = Entry(screen3, width=60)
    address_log.pack()

    
    lat_ = Label(screen3, text="Latitude", fg="Blue", height=2,font=("Arial Bold", 11))
    lat_.pack()
    lat__log = Entry(screen3, width=60)
    lat__log.pack()

    long_ = Label(screen3, text="Longitude", fg="Blue", height=2,font=("Arial Bold", 11))
    long_.pack()
    long__log = Entry(screen3, width=60)
    long__log.pack()

    email = Label(screen3, text="Email", fg="Blue", height=2,font=("Arial Bold", 11))
    email.pack()
    email_log = Entry(screen3, width=60)
    email_log.pack()

    mobile = Label(screen3, text="Mobile", fg="Blue", height=2,font=("Arial Bold", 11))
    mobile.pack()
    mobile_log = Entry(screen3, width=60)
    mobile_log.pack()
    
    
    Label(screen3, text="", bg="white").pack()
    Label(screen3, text="", bg="white").pack()
    add = Button(screen3, text="Add", height=2, width=30,command=add_police_record,bg="Blue",fg="white",font=("Arial Bold", 13))
    add.pack()
    

    back_button = Button(screen3, text="Back",  height=1, width=20,bg="black",fg="Red",font=("Arial Bold", 10),command=backandclose)
    back_button.pack()



from dbConnection import conn
def add_police_record():
    
    gg=head_name_log.get()
    bb=address_log.get()
    cc=lat__log.get()
    dd=long__log.get()
    ee=email_log.get()
    ff=mobile_log.get()
    conn(gg,bb,cc,dd,ee,ff)
    messagebox.showinfo("Information", "Details Added Successfully.")

    
def backandclose():
    os.system('python dashboard.py')
    screen3.destroy()
    screen3.quit()




















main_screen()

