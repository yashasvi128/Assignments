import sqlite3
try:
    con = sqlite3.connect('yashasvi.db')
    cursor = con.cursor()
    for i in range(0,10):
        sname = input("enter the name of the student :")
        smarks = int(input("enter the marks obtained by the student in the range 0 to 100 :"))
        cursor.execute('insert into students (sname, smarks) values(?, ?)',(sname, smarks))
    con.commit()
    print("data entered in the table!")
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('problem : ', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done!')
