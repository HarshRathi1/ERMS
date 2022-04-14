from distutils.log import debug
from tokenize import Name
from flask import *  
import sqlite3  
  
app = Flask(__name__)  
 
@app.route("/")  
def login():
    return render_template("login.html"); 

@app.route('/success',methods = ['POST'])  
def success():  
      passwrd=request.form['pass']  
      if passwrd=="12345":  
          return render_template('index.html') 
        
      elif passwrd=="67890": 
          return render_template('index2.html')

@app.route("/index")  
def index():  
    return render_template("index.html");

@app.route("/index2")  
def index2():  
    return render_template("index2.html"); 
 
@app.route("/add")  
def add():  
    return render_template("add.html")  

 
@app.route("/savedetails",methods = ["GET","POST"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            id = request.form["id"]  
            name = request.form["name"]
            phone_no = request.form["phone_no"]
            department = request.form["department"]
            role = request.form["role"] 
            salary = request.form["salary"]

            con = sqlite3.connect('ERMS.db')
            cur = con.cursor()  
            cur.execute("INSERT into Employees (id , name , phone_no ,department, role , salary) VALUES (?,?,?,?,?,?)",(id , name ,phone_no,department,role , salary))
            con.commit()  
            msg = "Employee successfully Added"  
            
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"  
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()  

 

@app.route("/view")  
def view():  
    con = sqlite3.connect("ERMS.db")
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Employees")

    rows = cur.fetchall()
    return render_template("view.html",rows = rows)


@app.route("/viewl")  
def viewl():  
    con = sqlite3.connect("ERMS.db")
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Employees")  
    rows = cur.fetchall()  
    return render_template("viewl.html",rows = rows)  



@app.route("/search")  
def search():  
    return render_template("search.html")  


@app.route("/searchrecord",methods = ["POST","GET"])  
def searchrecord(): 
    if request.method == "POST": 
        id = request.form["id"]  
        con = sqlite3.connect("staff.db")  
        con.row_factory = sqlite3.Row
        try:  
            cur = con.cursor()  
            cur.execute("select * from Employees where id = ? ",(id,)) 
            con.commit()   
            rows = cur.fetchall()  

        except:  
            msg = "can't be searched "  
        finally:  
                return render_template("view.html",rows = rows)  

@app.route("/search2")  
def search2():  
    return render_template("search2.html")  


@app.route("/searchrecord2",methods = ["POST","GET"])  
def searchrecord2(): 
    if request.method == "POST": 
        Dname = request.form["Dname"]  
        con = sqlite3.connect("staff.db")  
        con.row_factory = sqlite3.Row
        try:  
            cur = con.cursor()  
            cur.execute("select * from Department where Dname = ? ",(Dname,)) 
            con.commit()   
            rows = cur.fetchall()  

        except:  
            msg = "can't be searched "  
        finally:  
                return render_template("view2.html",rows = rows)  

@app.route("/search3")  
def search3():  
    return render_template("search3.html")  


@app.route("/searchrecord3",methods = ["POST","GET"])  
def searchrecord3(): 
    if request.method == "POST": 
        CourseID = request.form["CourseID"]  
        con = sqlite3.connect("staff.db")  
        con.row_factory = sqlite3.Row
        try:  
            cur = con.cursor()  
            cur.execute("select * from Course where CourseID = ? ",(CourseID,)) 
            con.commit()   
            rows = cur.fetchall()  

        except:  
            msg = "can't be searched "  
        finally:  
                return render_template("view3.html",rows = rows) 

@app.route("/search4")  
def search4():  
    return render_template("search4.html")  


@app.route("/searchrecord4",methods = ["POST","GET"])  
def searchrecord4(): 
    if request.method == "POST": 
        CourseID = request.form["CourseID"]  
        con = sqlite3.connect("staff.db")  
        con.row_factory = sqlite3.Row
        try:  
            cur = con.cursor()  
            cur.execute("select * from Course where CourseID = ? ",(CourseID,)) 
            con.commit()   
            rows = cur.fetchall()  

        except:  
            msg = "can't be searched "  
        finally:  
                return render_template("view.html",rows = rows)  




@app.route("/updaterecord2",methods = ["POST","GET"])  
def updaterecord2():
     
    if request.method == "POST": 
       Dnumber = request.form["Dnumber"]  
       Dname = request.form["Dname"]    
    con = sqlite3.connect("staff.db")  
    con.row_factory = sqlite3.Row
    try:  
            cur = con.cursor()  
            cur.execute("update Department set Dname = ? where Dnumber = ? ",(Dname,Dnumber,)) 
            con.commit()   
            rows = cur.fetchall() 
            msg="Updated Successfully" 

    except:  
            msg = "can't be updated"  
    finally:  
                return render_template("updateview2.html",msg=msg)
    
@app.route("/updaterecord3",methods = ["POST","GET"])  
def updaterecord3():
     
    if request.method == "POST": 
       EmployeID = request.form["EmployeID"]  
       Full_day = request.form["Full_day"]    
       half_day = request.form["half_day"]    
    con = sqlite3.connect("staff.db")  
    con.row_factory = sqlite3.Row
    try:  
            cur = con.cursor()  
            cur.execute("update LeaveRecord set Full_day = ?, half_day =? where EmployeID = ? ",( Full_day, half_day, EmployeID,)) 
            con.commit()   
            rows = cur.fetchall() 
            msg="Updated Successfully" 

    except:  
            msg = "can't be updated "  
    finally:  
                return render_template("updateview3.html",msg=msg)  

@app.route("/updaterecord4",methods = ["POST","GET"])  
def updaterecord4():
     
    if request.method == "POST": 
       C_no = request.form["C_no"]  
       EmpId = request.form["EmpId"]    
    con = sqlite3.connect("staff.db")  
    con.row_factory = sqlite3.Row
    try:  
            cur = con.cursor()  
            cur.execute("update Teaches set EmpId = ? where C_no = ? ",( EmpId,C_no,)) 
            con.commit()   
            rows = cur.fetchall() 
            msg="Updated Successfully" 

    except:  
            msg = "can't be updated "  
    finally:  
                return render_template("updateview4.html",msg=msg)  



@app.route("/delete")  
def delete():  
    return render_template("delete.html")  
 
@app.route("/deleterecord",methods = ["POST","GET"])  
def deleterecord(): 
    if request.method == "POST": 
        id = request.form["id"]  
        
        con = sqlite3.connect("ERMS.db")
        con.row_factory = sqlite3.Row
        try:  
            cur = con.cursor()  
            cur.execute("delete from Employees where id = ? ",(id,)) 
            rows = cur.fetchall()  

            con.commit() 
            msg = "Record successfully deleted"
        except:  
            msg = "Can't be deleted"
        finally:  
            return render_template("delete_record.html",msg = msg)


@app.route("/update")  
def update():  
    return render_template("update.html") 

@app.route("/update2")  
def update2():  
    return render_template("update2.html") 

@app.route("/update3")  
def update3():  
    return render_template("update3.html") 

@app.route("/update4")  
def update4():  
    return render_template("update4.html") 



@app.route("/add2")  
def add2():  
    return render_template("add2.html")
  

@app.route("/savedeptdetails",methods = ["GET","POST"])  
def saveDeptDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            id = request.form["id"]
            name = request.form["name"]
            email = request.form["email"]
            department = request.form["department"]
            charges=request.form["charges"]

            con = sqlite3.connect('ERMS.db')
            cur = con.cursor()  
            cur.execute("INSERT into Clients (id,name,email,department,charges) VALUES (?,?,?,?,?)",(id,name,email,department,charges))
            con.commit()  
            msg = "Client successfully Added"
            
        except:  
            con.rollback()  
            msg = "We can not add the client to the list"
        finally:  
            return render_template("success2.html",msg = msg)  
            con.close()  


@app.route("/view2")  
def viewDept():  
    con = sqlite3.connect("ERMS.db")
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Clients")
    rows = cur.fetchall()  
    return render_template("view2.html",rows = rows)  

@app.route("/viewl2")  
def viewDeptl2():  
    con = sqlite3.connect("staff.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Department")  
    rows = cur.fetchall()  
    return render_template("viewl2.html",rows = rows)  

@app.route("/delete2")  
def deleteDept():  
    return render_template("delete2.html")  
 
@app.route("/deletedeptrecord",methods = ["POST","GET"])  
def deletedeptrecord(): 
    if request.method == "POST": 
        id = request.form["id"]
        
        con = sqlite3.connect("ERMS.db")
        con.row_factory = sqlite3.Row
        try:  
            cur = con.cursor()  
            cur.execute("delete from Clients where id = ? ",(id))
            con.commit() 
            msg = "Record successfully deleted"
        except:  
            msg = "Can't be deleted"
        finally:  
            return render_template("delete_record2.html",msg = msg)

@app.route("/add3")  
def add3():  
    return render_template("add3.html")

@app.route("/saveleavedetails", methods = ["GET","POST"])  
def saveleavedetails():
    msg = "msg"
    if request.method == "POST":
        try:
            Infrastructure_Charges = request.form["Infrastructure_Charges"]


            con = sqlite3.connect('ERMS.db')
            cur = con.cursor()
            cur.execute("INSERT into other_charges (Infrastructure_Charges) VALUES (?)",
                        (Infrastructure_Charges))
            con.commit()
            msg = "Client successfully Added"

        except:
            con.rollback()
            msg = "We can not add the client to the list"
        finally:
            return render_template("success3.html", msg=msg)
            con.close()


@app.route("/view3")  
def viewCourse():  
    con = sqlite3.connect("ERMS.db")
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from other_charges")
    rows = cur.fetchall()  
    return render_template("view3.html",rows = rows)

@app.route("/viewl3")  
def viewCoursel3():  
    con = sqlite3.connect("staff.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Course")  
    rows = cur.fetchall()  
    return render_template("viewl3.html",rows = rows)  

@app.route("/delete3")  
def deleteCousre():  
    return render_template("delete3.html")  
 
@app.route("/deleteleaverecord",methods = ["POST","GET"])  
def deleteleaverecord(): 
    if request.method == "POST": 
        EmployeID = request.form["EmployeID"]  
        
        con = sqlite3.connect("staff.db")  
        con.row_factory = sqlite3.Row
        try:  
            cur = con.cursor()  
            cur.execute("delete from LeaveRecord where EmployeID = ? ",(EmployeID,)) 
            con.commit() 
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_record3.html", msg = msg)

@app.route("/add4")  
def add4():  
    return render_template("add4.html")

@app.route("/savecoursefacultydetails", methods = ["GET","POST"])  
def savecoursefacultydetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            EmpId = request.form["EmpId"]  
            C_no = request.form["C_no"]  

            con = sqlite3.connect('staff.db')  
            cur = con.cursor()  
            cur.execute("INSERT into Teaches (EmpId , C_no ) VALUES (?,?)",(EmpId , C_no ))  
            con.commit()  
            msg = "Faculty associated with course successfully Added"      
        except:  
            con.rollback()  
            msg = "We can not add faculty and associated course to the list"  
        finally:  
            return render_template("success4.html",msg = msg)  
            con.close()  


@app.route("/view4")  
def viewfacultywithCourse():  
    con = sqlite3.connect("ERMS.db")
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select sum(salary) from Employees")
    rows = cur.fetchall()  
    return render_template("view4.html",rows = rows)

@app.route("/viewl4")  
def viewfacultywithCoursel4():  
    con = sqlite3.connect("staff.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Teaches")  
    rows = cur.fetchall()  
    return render_template("viewl4.html",rows = rows)  

@app.route("/delete4")  
def deletefacultyCousre():  
    return render_template("delete4.html")  
 
@app.route("/deletefacultycourserecord",methods = ["POST","GET"])  
def deletefacultycourserecord(): 
    if request.method == "POST": 
        EmpId = request.form["EmpId"]  
        
        con = sqlite3.connect("staff.db")  
        con.row_factory = sqlite3.Row
        try:  
            cur = con.cursor()  
            cur.execute("delete from Teaches where EmpId = ? ",(EmpId,)) 
            con.commit() 
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_record4.html", msg = msg)

if __name__ == "__main__":  
    app.run(debug=True)