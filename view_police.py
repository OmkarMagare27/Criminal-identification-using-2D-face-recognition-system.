from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from dbConnection import conn3
from dbConnection import delete
import os
import mysql.connector as con
import math
from importlib import reload
import _thread
import importlib
import sys
import datetime
import logiccheck


global window
def view_police():
    global window
    def selectItem(a):
        curItem = tree.focus()
        gg=tree.item(curItem)
        print (gg)
        x = gg["values"]
        print(x)
        y=x[0]
        
        delete(y)
        window.destroy()
        window.after(1000,view_police)
    #reload(logiccheck)
    
   
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
    tree = ttk.Treeview(window)
    


    window.title("View Police Station")
    image2 =Image.open('grayscale.jpg')
    image1 = ImageTk.PhotoImage(image2)
    w = image1.width()
    h = image1.height()
    window.geometry('%dx%d+0+0' % (w,h))
    filename =ImageTk.PhotoImage(Image.open('grayscale.jpg'))

    Label(window, text="Police Station Details", bg="Grey", height=1, width=250,font=("Arial Bold", 20), command = conn3()).pack()



    
    

    tree["column"] = ("ID", "Police Station Name", "Address", "Latitude", "Longitude", "Email", "Mobile No")
    tree.column("ID", width=50)
    tree.heading("ID", text="ID")
    tree.column("Police Station Name", width=150)
    tree.heading("Police Station Name", text="Police Station Name")
    tree.column("Address", width=100)
    tree.heading("Address", text="Address")
    tree.column("Latitude", width=100)
    tree.heading("Latitude", text="Latitude")
    tree.column("Longitude", width=100)
    tree.heading("Longitude", text="Longitude")
    tree.column("Email", width=100)
    tree.heading("Email", text="Email")
    tree.column("Mobile No", width=100)
    tree.heading("Mobile No", text="Mobile No")
    tree.bind('<ButtonRelease-1>', selectItem)
    db=con.connect(host="localhost", port=3306, user="root", password="root", database="db_accident" ,charset='utf8')
    cur = db.cursor()
    cur.execute("SELECT * FROM tbl_police")
    row = cur.fetchall()

    cpt = 0
    for i in row:
        #print(i)
        tree.insert('', 'end', values=i)
        #values=row.values(lenght(row))
    cpt += 1
    tree.pack()

    back_button = Button(window, text="Back", height=1, width=20,bg="Blue",fg="white",font=("Arial Bold", 10), command=backandclose)
    back_button.pack()

    Label(window, text="Click on a data to delete", bg="red", fg="white", height=1, width=250,font=("Arial Bold", 12)).pack()

    
    #window.destroy()
    #window.mainloop()
    

def backandclose():
    
    
    window.destroy()
    window.quit()
    import dashboard

view_police()


  



