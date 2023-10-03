from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from dbConnection import conn
import os
from tkinter import messagebox


def register():
    global head_name_log
    global address_log
    global lat__log
    global long__log
    global email_log
    global mobile_log
    global window
    


    window=Tk()

    C= Canvas(window, height=180, width=720)
    filename = ImageTk.PhotoImage(Image.open('186040.gif'))
    background_label = Label(window, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.create_image(0,0,anchor=NW, image=filename)
    C.pack()
    window.title("DASHBOARD")
    window.geometry('720x720')
##    image2 =Image.open('186040.gif')
    filename.image2 =ImageTk.PhotoImage(Image.open('186040.gif'))
##    image = ImageTk.PhotoImage(filename.image2)
##    w = filename.image2.width()
##    h = filename.image2.height()
##    window.geometry('%dx%d+0+0' % (w,h))
##    Label(window, text="Smart CCTV Surveillance for Criminal Detection", bg="Gray", height=2, width=250,font=("Arial Bold", 24)).pack()
    
    window.title("Registration Form")

    Label(window, text="Register Police Station", bg="Grey", height=1, width=250,font=("Arial Bold", 20)).pack()
##    
    head_name = Label(window, text="Head Name", fg="Blue", height=2,font=("Arial Bold", 11))
    head_name.pack()
    head_name_log = Entry(window, width=60)
    head_name_log.pack()
    
    address = Label(window, text="Address", fg="Blue", height=2,font=("Arial Bold", 11))
    address.pack()
    address_log = Entry(window, width=60)
    address_log.pack()

    
    lat_ = Label(window, text="Latitude", fg="Blue", height=2,font=("Arial Bold", 11))
    lat_.pack()
    lat__log = Entry(window, width=60)
    lat__log.pack()

    long_ = Label(window, text="Longitude", fg="Blue", height=2,font=("Arial Bold", 11))
    long_.pack()
    long__log = Entry(window, width=60)
    long__log.pack()

    email = Label(window, text="Email", fg="Blue", height=2,font=("Arial Bold", 11))
    email.pack()
    email_log = Entry(window, width=60)
    email_log.pack()

    mobile = Label(window, text="Mobile", fg="Blue", height=2,font=("Arial Bold", 11))
    mobile.pack()
    mobile_log = Entry(window, width=60)
    mobile_log.pack()
    
    
    Label(window, text="", bg="white").pack()
    Label(window, text="", bg="white").pack()
    add = Button(window, text="Add", height=2, width=30,command=co,bg="Blue",fg="white",font=("Arial Bold", 13))
    add.pack()
    

    back_button = Button(window, text="Back",  height=1, width=20,bg="black",fg="Red",font=("Arial Bold", 10),command=backandclose)
    back_button.pack()

    image1 = ImageTk.PhotoImage(image2)
    w = image1.width()
    h = image1.height()
    window.geometry('%dx%d+0+0' % (w,h))
    filename =ImageTk.PhotoImage(Image.open('186040.gif'))
    
    

def co():
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
    window.destroy()
    window.quit()


register()
