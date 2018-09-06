import sqlite3
try:
    con = sqlite3.connect('yashasvi.db')
    cursor = con.cursor()
    query = 'create table students(rollno int(10) primary key, sname varchar(20), class varchar(5)'
    cursor.execute(query)
    con.commit()
    print("Table created successfully!")
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('problem occured: ', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done!')
