import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-RT99G2E\SQLEXPRESS;'
                      'Database=TSQL;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute("SELECT sc.companyname, country city FROM Sales.Customers as sc WHERE sc.country = 'Mexico'")

for i in cursor:
    print(i)