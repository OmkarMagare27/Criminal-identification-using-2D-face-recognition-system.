import mysql.connector as con
import math
from importlib import reload
import _thread
import importlib
import sys

def again():
    
    global window
    window=Tk()
    tree = ttk.Treeview(window)
    


    window.title("View Police Station")
    image2 =Image.open('186040.gif')
    image1 = ImageTk.PhotoImage(image2)
    w = image1.width()
    h = image1.height()
    window.geometry('%dx%d+0+0' % (w,h))
    filename =ImageTk.PhotoImage(Image.open('g186040.gif'))

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
    db=con.connect(host="localhost", port=3306, user="root", password="", database="db_accident")
    cur = db.cursor()
    cur.execute("SELECT * FROM tbl_police")
    row = cur.fetchall()
