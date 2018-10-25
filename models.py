import sqlite3 as sql
import random



def insertUser(table,data):
    con = sql.connect("accomodations.db")
    cur = con.cursor()
    c = "insert into "+table+" values ("+data+") ;"
    print(c)
    cur.execute(c)
    id = cur.lastrowid
    con.commit()
    con.close()
    return id



def select_all(prop_set):
    con = sql.connect("accomodations.db")
    cur = con.cursor()
    data = []
    a_data = []
    for i in prop_set:
        c =" SELECT * FROM room_details natural join location_details natural join properties natural join accom_amenities natural join accom_facilities natural  join visitor_propert where property_id ="+str(i)+";"
        # print(c)

        cur.execute(" SELECT * FROM room_details natural join location_details natural join properties natural join accom_amenities natural join accom_facilities natural  join properties_posted where property_id ="+str(i)+";")
        data.append(cur.fetchall())
    # c =  [i[0] for i in cur.execute(" SELECT property_id FROM properties_posted where property_status != 'booked'").fetchall()]
    # print(c)
    # for i in data:
    #     if i[0][0] in c:
    #         a_data.append(i)
    # print (a_data[0])
    con.commit()
    con.close()
    # print(data)
    return data

def group_by(field, condition, table):
    con = sql.connect("accomodations.db")
    cur = con.cursor()
    c = " SELECT " + field + " FROM " + table + " group by " + condition + ";"
    print(c)
    cur.execute(c)
    data = cur.fetchall()
    con.commit()
    con.close()
    return data

def select(field, condition, table):
    con = sql.connect("accomodations.db")
    cur = con.cursor()
    c = " SELECT "+ field + " FROM "+ table +" where " + condition+ ";"
    # print(c)
    cur.execute(c)
    data = cur.fetchall()
    con.commit()
    con.close()
    return data

def update(table, field, condition):
    con = sql.connect("accomodations.db")
    cur = con.cursor()
    c = " UPDATE "+ table + " SET "+ field+" where " + condition+ ";"
    # print(c)
    cur.execute(c)
    con.commit()
    con.close()

