'''
Hope Tambala
25677464
'''

# these should be the only imports you need
import sys
import sqlite3

import pandas as pd

# write your code here
# usage should be 
#  python3 part2.py customers
#  python3 part2.py employees
#  python3 part2.py orders cust=<customer id>
#  python3 part2.py orders emp=<employee last name>

sqlite_file = 'Northwind_small.sqlite'


# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

def customers(c):
    c.execute("SELECT Id,CompanyName FROM Customer")
 
    rows = c.fetchall()
    
    for row in rows:
        print(str(row))

def employees(c):
    
    c.execute("SELECT Id,FirstName,LastName FROM Employee")
 
    rows = c.fetchall()
    
    for row in rows:
        print(str(row))

def ordersCustomers(c, customerID):
    #c.execute("SELECT OrderId FROM OrderDetail WHERE ProductId=" + str(t))
    c.execute("SELECT OrderDate FROM 'Order' WHERE CustomerId=?",(customerID,))
 
    rows = c.fetchall()
    
    for row in rows:
        print(str(row))

def ordersEmployees(c,employeeID):
    c.execute("SELECT OrderDate FROM 'Order' WHERE EmployeeId=?",(employeeID,))
 
    rows = c.fetchall()
    
    for row in rows:
        print(str(row))



customers(c);

employees(c);

string = 'HANAR'
ordersCustomers(c,string);
ordersEmployees(c,2);