import sqlite3
try:
    con = sqlite3.connect('yashasvi.db')
    cursor = con.cursor()
    query = "select * from students"
    cursor.execute(query)
    con.commit()
    data = cursor.fetchall()
    for i in data:
        smarks = i[3]
        if smarks > 80:
            print('sname: {}, smarks: {}'.format(i[1], i[3]))
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
