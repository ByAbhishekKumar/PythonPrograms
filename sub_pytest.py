import sqlite3
conn = sqlite3.connect("Databases_one.db")
cc = conn.cursor()
#conn.execute("""create table students_result(
#			first text,
#			last text,
#			roll_no integer not null,
#			class integer,
#			chemistry real,
#			math real,
#			physics real )""")
#conn.commit()
#conn.execute('insert into students_result values ("Ankit","Raj",3,9,89,95,91)')
cc.execute("select * from students_result;")
print(cc.fetchall())
##firstname= input("Enter firstname: ")
##lastname=input("Enter lastname: ")
##rollno=int(input("Enter roll number: "))
##class1=int(input("Enter class: "))
##chem_marks=float(input("Enter chemistry marks: "))
##math_marks=float(input("Enter maths marks: "))
##physics_marks=float(input("Enter physics marks: "))
    
#try block to catch exceptions
#try:
#	cc=conn.cursor()
#	cc.execute("INSERT INTO students_result (first,last,roll_no,class,chemistry,math,physics) VALUES (?,?,?,?,?,?,?)", (firstname,lastname,rollno,class1,chem_marks,math_marks,physics_marks))
#	conn.commit()
#	print ("One record added successfully.")

#except block to handle exceptions    
#except:
#	print ("Error in operation.")
#	conn.rollback()
    
conn.close()
