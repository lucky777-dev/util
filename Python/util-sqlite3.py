#coding:utf-8

import sqlite3

#Connects to database (creates it if it doesn't exists)
con = sqlite3.connect("test.db")

#Create cursor
c = con.cursor()

#Create a table in db
#--------------------
c.execute("""CREATE TABLE customers (name TEXT,
                                    lastName TEXT,
                                    age INTEGER)""")
print("Database created!")
#NULL
#INTEGER
#REAL
#TEXT
#BLOB (bin)


#Insert a line in db
#-------------------
c.execute("INSERT INTO customers VALUES (\"Smile\", \"42art\", \"28\")")
print("\"Smile/42/28yo\" added in db!")
c.execute("INSERT INTO customers VALUES (\"Lucky\", \"777jackpot\", \"28\")")
print("\"Lucky/777/28yo\" added in db!")
c.execute("INSERT INTO customers VALUES (\"Harry\", \"Potter\", \"29\")")
print("\"Harry/Potter/29yo\" added in db!")


#Insert multiple lines at once in db
#-----------------------------------
many_customers = [("Francois", "Perusse", 56), 
                    ("Paul", "Van Haever", 29), 
                    ("Aurelien", "Barrau", 42)]
c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)
print("3 customers added!")


#Query the db
#------------
#Get data
c.execute("SELECT * FROM customers")
print(f"FIRST LINE:\n{c.fetchone()}\n\n")
print(f"THREE NEXT LINES:\n{c.fetchmany(3)}\n\n")
print(f"ALL NEXT LINES:\n{c.fetchall()}\n")

print("------------------------------------------------------------------\n")

c.execute("SELECT * FROM customers")
print(f"FIRST LINE:\n{c.fetchone()}\n\n")
c.execute("SELECT * FROM customers")
print(f"THREE FIRST LINES:\n{c.fetchmany(3)}\n\n")
c.execute("SELECT * FROM customers")
print(f"ALL LINES:\n{c.fetchall()}\n")

print("------------------------------------------------------------------\n")
#Get data with conditions
c.execute("SELECT * FROM customers WHERE age == 28")
print(f"ALL LINES WHERE AGE == 28: \n{c.fetchall()}\n")

print("------------------------------------------------------------------\n")

c.execute("SELECT * FROM customers WHERE AGE == 42")
print(f"FIRST LINE WHERE AGE == 42:\nNAME = {c.fetchone()[0]}")
c.execute("SELECT * FROM customers WHERE AGE == 42")
print(f"LASTNAME = {c.fetchone()[1]}")
c.execute("SELECT * FROM customers WHERE AGE == 42")
print(f"AGE = {c.fetchone()[2]}\n")

print("------------------------------------------------------------------\n")
#Primary keys
c.execute("SELECT rowid, * FROM customers")
tmp = c.fetchall()
print("ALL LINES WITH PRIMARY KEYS:\n")
for i in tmp:
    print(f"KEY = {i[0]}\t\tNAME = {i[1]}\t\tLASTNAME = {i[2]}  \t\tAGE = {i[3]}")

print("\n------------------------------------------------------------------\n")
#String % = *
c.execute("SELECT * FROM customers WHERE name LIKE \"%r%\"")
print(f"ALL LINES WITH A 'r' IN NAME:\n{c.fetchall()}")

print("\n------------------------------------------------------------------\n")
#Change mulitple values
c.execute("SELECT * FROM customers WHERE age == 29 OR age == 30")
tmp = c.fetchall()
print(f"ALL LINES WHERE age == 29 OR 30:\n{tmp}")
for i in tmp:
    if i[2] == 29:
        c.execute("""UPDATE customers SET age = 30
                    WHERE age == 29""")
    else:
        c.execute("""UPDATE customers SET age = 29
                    WHERE age == 30""")
c.execute("SELECT * FROM customers WHERE age == 29 OR age == 30")
print(f"LINES AFTER CHANGES:\n{c.fetchall()}")

print("\n------------------------------------------------------------------\n")
#Change value with primary key
c.execute("SELECT rowid, * FROM customers")
tmp = c.fetchone()
print(f"FIRST LINE:\n{tmp}")
if tmp[1] == "Smile":
    c.execute("UPDATE customers SET name = \"Smile42\" WHERE rowid == 1")
else:
    c.execute("UPDATE customers SET name = \"Smile\" WHERE rowid == 1")
c.execute("SELECT rowid, * FROM customers")
print(f"FIRST LINE AFTER CHANGE:\n{c.fetchone()}")

print("\n------------------------------------------------------------------\n")
#Delete lines
c.execute("DELETE FROM customers WHERE rowid >= 4")
c.execute("SELECT rowid, * FROM customers")
tmp = c.fetchall()
print("LINES WHERE primary key >= 4 DELETED:")
for i in tmp:
    print(f"KEY = {i[0]}\t\tNAME = {i[1]}\t\tLASTNAME = {i[2]}  \t\tAGE = {i[3]}")

many_customers = [("Francois", "Perusse", 56), 
                    ("Paul", "Van Haever", 29), 
                    ("Aurelien", "Barrau", 42)]
c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)
c.execute("SELECT rowid, * FROM customers")
tmp = c.fetchall()
print("\nDELETED LINES ARE BACK:")
for i in tmp:
    print(f"KEY = {i[0]}\t\tNAME = {i[1]}\t\tLASTNAME = {i[2]}  \t\tAGE = {i[3]}")

print("\n------------------------------------------------------------------\n")
#Order by..
c.execute("SELECT rowid, * FROM customers ORDER BY age")
tmp = c.fetchall()
print("ORDER BY AGE (ASC):")
for i in tmp:
    print(f"KEY = {i[0]}\t\tNAME = {i[1]}\t\tLASTNAME = {i[2]}  \t\tAGE = {i[3]}")

c.execute("SELECT rowid, * FROM customers ORDER BY age DESC")
tmp = c.fetchall()
print("\nORDER BY AGE (DESCENDING):")
for i in tmp:
    print(f"KEY = {i[0]}\t\tNAME = {i[1]}\t\tLASTNAME = {i[2]}  \t\tAGE = {i[3]}")
    
c.execute("DROP TABLE customers")

print("\n------------------------------------------------------------------\n")
#Delete table

print("DELETING 'customers' TABLE...\n")
con.commit()

print("'customers' TABLE DELETED !\n")

con.close()