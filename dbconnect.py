import sqlite3
import cx_Oracle
conn=sqlite3.connect('test.db')
print ("Opened database successfully");
mycursor=conn.cursor()


#mycursor = conn.execute("SELECT ID,NAME,AGE,CITY,MARKS from STUDENT")

