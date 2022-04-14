import sqlite3  
  
con = sqlite3.connect("ERMS.db")
print("Database opened successfully")
con.execute("Create table other_charges(Infrastructure_Charges integer not null)")

print("Table created successfully")


con.close()
'''con.execute(
    "create table Employees (id INTEGER PRIMARY KEY, name TEXT NOT NULL,phone_no INTEGER NOT NULL, department text NOT NULL, role TEXT NOT NULL, salary INTEGER NOT NULL)")
con.execute(
    "create table Clients(id integer primary key,name text not null,email email not null,department text not null,charges integer not null)")'''
