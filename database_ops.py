import sqlite3

dbh=sqlite3.connect("ericsson.db")
c=dbh.cursor()

def create_table():
    c.execute("CREATE TABLE employee(empid REAL, empname TEXT, tech TEXT, exp REAL)")

def load_data():
    e_id=int(input("Enter your emp id:"))
    e_name=input("Enter your name:")
    e_tech=input("Enter your technology:")
    e_exp=int(input("Enter your experience:"))
    #c.execute("INSERT INTO employee VALUES(1000,'Siva Murugan','Python',15)")\
    c.execute("INSERT INTO employee VALUES(?,?,?,?)",(e_id,e_name,e_tech,e_exp))
    dbh.commit()

def update_records():
    c.execute("UPDATE employee SET tech='BigData' WHERE empid=1005")
    dbh.commit()
    c.close()
    dbh.close()

def delete_data():
    c.execute("DELETE FROM employee WHERE exp=20")
    dbh.commit()
    c.close()
    dbh.close()
def fetch_data():
    c.execute("SELECT * FROM employee")
    #fetchone,fetchmany,fetchall
    #print(c.fetchone())
    #print(c.fetchmany(3))
    #print(c.fetchall())

    for row in c.fetchall():
        if row[3] > 15:
            print(row[1] + " - "+row[2].upper() + ' - ' + str(row[3]))
#create_table()
# for x in range(5):
#     load_data()
#update_records()
#delete_data()
fetch_data()