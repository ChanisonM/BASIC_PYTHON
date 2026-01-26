import sqlite3 
from tabulate import tabulate

conn = sqlite3.connect('database.db')
cur = conn.cursor()
sql = 'SELECT * FROM employee'
rows = cur.execute(sql)

head = ('ID' , 'Name' , 'Position' , 'Salary' , 'Phone' , 'Birthday')
print(tabulate( rows,  
                head ,
                tablefmt='psql' ,
                floatfmt=',.0f',
                stralign='left'))