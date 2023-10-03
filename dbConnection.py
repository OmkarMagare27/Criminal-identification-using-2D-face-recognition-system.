import mysql.connector as con
import sys
import mysql


def conn(head_name,address,lat_,long_,email,mobile):
    db = con.connect(host="localhost", port=3306, user="root", password="root", database="db_accident", charset='utf8')
    cur=db.cursor()

    
    query="insert into tbl_police(head_name,address,lat_,long_,email,mobile) values(%s,%s,%s,%s,%s,%s)"
    value=[head_name,address,lat_,long_,email,mobile]
    cur.execute(query,value)
    db.commit()
    #tkMessageBox.showinfo("Information", "Person Added Successfull")


def conn2(hname,addr,lat_2,long_2,email2,mobile2):
    db = con.connect(host="localhost", port=3306, user="root", password="root", database="db_accident", charset='utf8')
    cur=db.cursor()

    
    query="insert into tbl_hospitals(hname,addr,lat_2,long_2,email2,mobile2) values(%s,%s,%s,%s,%s,%s)"
    value=[hname,addr,lat_2,long_2,email2,mobile2]
    cur.execute(query,value)
    db.commit()

def conn3():
    db=con.connect(host="localhost", port=3306, user="root", password="root", database="db_accident", charset='utf8')
    cur = db.cursor()
    
    
    if mysql.connector.connect():
        print("Database is Connected")
        cur.execute("select * from tbl_police")
        data = cur.fetchall()
        #for row in data:
        print (data)


def delete(id):
    db = con.connect(host="localhost", port=3306, user="root", password="root", database="db_accident", charset='utf8')
    cur=db.cursor()

    
    query="delete from  tbl_police where id="+str(id)
    
    cur.execute(query)
    db.commit()


def delete1(id):
    db = con.connect(host="localhost", port=3306, user="root", password="root", database="db_accident", charset='utf8')
    cur=db.cursor()

    
    query="delete from  tbl_hospitals where h_id="+str(id)
    
    cur.execute(query)
    db.commit()

def conn4():
    db=con.connect(host="localhost", port=3306, user="root", password="root", database="db_accident", charset='utf8')
    cur = db.cursor()
    
    
    if mysql.connector.connect():
        print("Database is Connected")
        cur.execute("select * from tbl_hospitals")
        data = cur.fetchall()
        #for row in data:
        print (data)




def conn5(id,name,mobile,class_,div_,adh_,em_,type_):
    db = con.connect(host="localhost", port=3306, user="root", password="root", database="db_accident", charset='utf8')
    cur=db.cursor()

    #id, name, mobile, address, crime_details, adh_, em_, crime_code
    query="insert into tbl_criminal_record(id,name,mobile,address,crime_details,adh_,em_,crime_code) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    value=[id,name,mobile,class_,div_,adh_,em_,type_]
    cur.execute(query,value)
    db.commit()
    #tkMessageBox.showinfo("Information", "Person Added Successfull")
    







def view_all_attendance(name):
    
    db = con.connect(host="localhost", user="root", password="root", database="db_accident", charset='utf8')
    cur = db.cursor()
    
    query="SELECT count(id), name FROM tbl_criminal_record where name='"+name+"'"
    cur.execute(query)
    names=cur.fetchall()
    for row in names:
       return row[0]

    #print(names)
    db.commit()
    if(len(names)>0):
        return names
    else:
        return 'no'



        
        

    

