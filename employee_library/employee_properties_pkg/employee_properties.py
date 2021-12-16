import mysql.connector

class EmployeeProperties:

    # connect to db
    con = mysql.connector.connect(host="localhost", user ="root", password="password", database="emp")

    # Function to Display All Employees
    # from Employee Table
    def Show_employees(self):
        
        # query to select all rows from
        # Employee Table
        sqlquery = 'select * from Employeedb'
        c = con.cursor()
        
        # Executing the SQL Query
        c.execute(sqlquery)
        
        # Fetching all details of all the
        # Employees
        r = c.fetchall()
        for i in r:
            print("Employee id : ", i[0])
            print("Employee Fullname: ", i[1])
            print("Employee Mobile : ", i[2])
            print("Employee Position : ", i[3])
    
    def add_employees(self):
        
        employeeid = input("Enter Employee id : ")
        
        #check if already exists in db
        sqlquery = 'select * from Employeedb where employeeid=%s'
        c = con.cursor(buffered=True)
        data = (employeeid)
        c.execute(sqlquery,data)
        r = c.rowcount
        if r ==1:
            print("Employee Already exists")
        else:
            fullname = input("Employee Fullname: ")
            mobile = input("Employee Mobile : ")
            position = input("Employee Position : ")
            data = (employeeid, fullname, mobile, position)

            sqlquery = 'insert into Employeedb values(%s,%s,%s,%s)'
            c = con.cursor()
         
            # Executing the SQL Query
            c.execute(sqlquery, data)
            
            # commit() method to make changes in
            # the table
            con.commit()
            print("Employee Added Successfully ")
