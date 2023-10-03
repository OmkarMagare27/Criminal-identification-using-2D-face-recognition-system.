import cv2
import numpy as np 
import sqlite3
from dbConnection import conn
import mysql.connector as con
import os
import Single_Email
#conn = sqlite3.connect('database.db')
#c = conn.cursor()
import datetime
from datetime import timedelta
def mark_attend():
  fname = "recognizer/trainingData.yml"
  if not os.path.isfile(fname):
    print("Please train the data first")
    exit(0)
  face_cascade = cv2.CascadeClassifier('haar.xml')
  cap = cv2.VideoCapture(0)
  recognizer = cv2.face.LBPHFaceRecognizer_create()
  recognizer.read(fname)
  while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
      cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
      ids,conf = recognizer.predict(gray[y:y+h,x:x+w])
      #print(conf)
      nn=log(ids)
      name=""
      
      #print(nn)
      for i in nn:
        print (i[1])
        name=i[1]
        #if(i[7]=="Red"):
         # print("red")
        db = con.connect(host="localhost", user="root", password="root", database="db_accident",charset='utf8')
        cur = db.cursor()
        query="SELECT head_name,mobile,lat_, long_,min(sqrt(pow((69.1 * (lat_ - (18.560589))), 2) +pow((69.1 * ((73.929360) - long_) * cos(lat_ / 57.3)), 2))) AS distance FROM tbl_police "
        cur.execute(query)
        names=cur.fetchall()
        for row,prediction in zip(names,nn):
                
              sms =" Dear Sir Criminal identified at:  Lat: "+str(18.560589)+"longitude : "+str(73.929360)+"  With Details "+str(nn)
              email="shreyasjoshi130@gmail.com"
              Single_Email.sendEmail(email,sms)
              print(sms)
              #send_sms(str(row[1]),msg)
              #send_sms("9834780214",msg)
                
                
        
      
      
      
      
   
      if conf < 100:
        cv2.putText(img, name, (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (150,255,0),2)
      else:
        cv2.putText(img, 'No Match', (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
    cv2.imshow('Face Recognizer',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
      break
  cap.release()
  cv2.destroyAllWindows()


def log(id):
    flag=str(id)
    db = con.connect(host="localhost", user="root", password="root", database="db_accident",charset='utf8')
    cur = db.cursor()
    
    query="select * from tbl_criminal_record where id='"+flag+"'"
    cur.execute(query)
    names=cur.fetchall()
    for row in names:
       return names
       #print(row[1])

    #print(names)
    db.commit()
    #if(len(names)>0):
     #   return row
    #else:
     #   return 'no record'


import requests
 
def send_sms(phone,text):
        user="richhelps1234"
        pass1="richhelps1234"
        sender="PRJCTP"
        #phone="7350456969"
        #text="Hello friend"
        priority="ndnd"
        stype="normal"
        ploads = {'user':user,'pass':pass1,'sender':sender,'phone':phone,'text':text,'priority':priority,'stype':stype}
        r = requests.get('http://bhashsms.com/api/sendmsg.php',params=ploads)
        print(r.text)
        print(r.url)
