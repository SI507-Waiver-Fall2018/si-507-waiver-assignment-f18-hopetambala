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

# Counts How Many Arguments
arguments = len(sys.argv) - 1  



# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

#Lists Customers
def customers(c):
    c.execute("SELECT Id,CompanyName FROM Customer")
 
    rows = c.fetchall()
    
    for row in rows:
        print(str(row))

#Lists Employees
def employees(c):
    
    c.execute("SELECT Id,FirstName,LastName FROM Employee")
 
    rows = c.fetchall()
    
    for row in rows:
        print(str(row))

#Lists Order Dates Placed by CustomerID
def ordersCustomers(c, customerID):
    #c.execute("SELECT OrderId FROM OrderDetail WHERE ProductId=" + str(t))
    c.execute("SELECT OrderDate FROM 'Order' WHERE CustomerId=?",(customerID,))
 
    rows = c.fetchall()
    
    for row in rows:
        print(str(row))

#Lists Order Dates Placed by EmployeeID
def ordersEmployees(c,employeeID):
    #c.execute("SELECT OrderDate FROM 'Order' WHERE EmployeeId=?",(employeeID,))
    #c.execute("SELECT 'Order.OrderDate' FROM 'Order' O INNER JOIN Employee ON 'Order.id' = Employee.id WHERE Employee.LastName=?",(employeeID,))
    c.execute("SELECT OrderDate FROM 'Order' O INNER JOIN Employee E ON O.EmployeeId = E.Id WHERE E.LastName IN ('King') ")
    c.execute("SELECT OrderDate FROM 'Order' O INNER JOIN Employee E ON O.EmployeeId = E.Id WHERE E.LastName IN (?) ", (employeeID,))

    rows = c.fetchall()
    
    for row in rows:
        print(str(row))


# Main
if arguments == 2:
    param1 = sys.argv[1]
    param2 = sys.argv[2]
    
    if param1 == 'orders':
        if param2[:5] =='cust=':
            ordersCustomers(c,param2[5:])
            #print('reached')
        elif param2[:4] == 'emp=':
            ordersEmployees(c,param2[4:])
            #print('reached')
    else:    
        print('Not Valid Arguments')
elif arguments == 1:
    param = sys.argv[1]

    if param == 'customers':
        customers(c);
    elif param == 'employees':
        employees(c);
    else:
        print ('Not Valid Argument')
else:
    print ('Not Valid Input')

