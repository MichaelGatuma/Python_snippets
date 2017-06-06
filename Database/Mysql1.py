'''
Created on May 16, 2017

@author: duncan
'''
import os.path
import csv
import sqlite3 as lite
import sys
import MySQLdb


#readinf normal flat files
#Check if file first exists

if not os.path.isfile("testFile.txt"):
    print("The file does not exixt" )
else:
    print("File exists")
    #Open file for reading -- mode r
    with open("testFile.txt","r") as f:
        content = f.readlines()
    for x in content:
        print(x)
   
   
#writing to csv file 
    
with open("persons.csv","wb") as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Name', 'Profession'])
    filewriter.writerow(['Derek', 'Software Developer'])
    filewriter.writerow(['Steve', 'Software Developer'])
    filewriter.writerow(['Paul', 'Manager'])
    print('File writting done')
    
# Reading csv files

with open('persons.csv', 'rb') as f:
    reader = csv.reader(f)
 
    # read file row by row
    for row in reader:
        print (row)


## Using sqlite
con = None
 
try:
    con = lite.connect('test.db')
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    try:
        cur.execute("if not exists(create table user(name varchar,age int))")
    except Exception:
        print ("Table exists")
    cur.execute("insert into user values('duncan','towers')")
    cur.execute("Select * from user")

    data = cur.fetchall()
    for row in data:
        print (row)      
except lite.Error, e:   
    print "Error %s:" % e.args[0]
    sys.exit(1)
finally:    
    if con:
        con.close()

#Mysql connection to dabasase 
db = MySQLdb.connect(host="localhost",  # your host 
                     user="duncan",       # username
                     passwd="mysql123",     # password
                     db="trivia")   # name of the database
# Create a Cursor object to execute queries.
cur = db.cursor()
 
# Select data from table using SQL query.
cur.execute("SELECT * FROM role")
 
# print the first and second columns      
for row in cur.fetchall() :
    print row[0], " ", row[1]
    
    
    
    