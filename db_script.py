import sqlite3 as sql
import random
from werkzeug.security import generate_password_hash, check_password_hash
con = sql.connect("accomodations.db")
# cur = con.cursor()
# cur.execute(" select property_id from properties;")
# bath = ['bath_image_27.jpg', 'bath_image_26.jpg', 'bath_image_52.jpg', 'bath_image_35.jpg', 'bath_image_72.jpg', 'bath_image_42.jpg', 'bath_image_62.jpg', 'bath_image_29.jpg', 'bath_image_2.jpg', 'bath_image_22.jpg', 'bath_image_28.jpg', 'bath_image_31.jpg', 'bath_image_25.jpg']
# bed = ['bed_image_34.jpg', 'bed_image_2.jpg', 'bed_image_5.jpg', 'bed_image_27.jpg', 'bed_image_16.jpg', 'bed_image_6.jpg', 'bed_image_26.jpg', 'bed_image_7.jpg', 'bed_image_31.jpg', 'bed_image_40.jpg', 'bed_image_23.jpg', 'bed_image_11.jpg', 'bed_image_17.jpg', 'bed_image_4.jpg', 'bed_image_39.jpg', 'bed_image_3.jpg', 'bed_image_33.jpg', 'bed_image_38.jpg', 'bed_image_32.jpg', 'bed_image_8.jpg', 'bed_image_25.jpg', 'bed_image_37.jpg', 'bed_image_9.jpg', 'bed_image_20.jpg']
# dine = ['dining_image_61.jpg', 'dining_image_12.jpg', 'dining_image_35.jpg', 'dining_image_2.jpg', 'dining_image_31.jpg', 'dining_image_24.jpg', 'dining_image_23.jpg', 'dining_image_51.jpg', 'dining_image_20.jpg', 'dining_image_13.jpg', 'dining_image_43.jpg', 'dining_image_32.jpg']
# kit = ['kitchen_image_30.jpg', 'kitchen_image_28.jpg', 'kitchen_image_1.jpg']
# ent = ['entrance_image_21.jpg', 'entrance_image_2.jpg', 'entrance_image_32.jpg', 'entrance_image_24.jpg', 'entrance_image_42.jpg', 'entrance_image_27.jpg', 'entrance_image_31.jpg', 'entrance_image_12.jpg']
# liv = ['living_image_15.jpg', 'living_image_14.jpg', 'living_image_29.jpg', 'living_image_36.jpg', 'living_image_18.jpg', 'living_image_10.jpg', 'living_image_19.jpg', 'living_image_12.jpg', 'living_image_24.jpg', 'living_image_21.jpg']
# std = ['studio_image_3.jpg','studio_image_35.jpg','studio_image_22.jpg']
# L = ('Kitchen', 'Shampoo', 'Heating', 'Air conditioning', 'Washing Machine', 'Dryer', 'Wireless', 'Internet', 'Breakfast', 'Indoor fireplace', 'Doorman', 'Hair dryer', 'Hangers', 'Iron', 'TV', 'Crib', 'High chair', 'Self check-in', 'Smoke detector', 'Laptop friendly workspace', 'Carbon monoxide detector', 'Buzzer/wireless intercom')
#
# for i in cur.fetchall():
#     k = random.randint(0, 12)
#     c = "insert into accom_photos (property_id, accom_photo, photo_description) values ('"+str(i[0])+"','"+bath[k]+"','bathroom');"
#     cur.execute(c)
#
# con.commit()
# con.close()


# for i in cur.fetchall():
#     k = random.randint(1, 20)
#     c = "update location_details set unit_num = '"+str(k)+"' where property_id ="+str(i[0])+";"
#     cur.execute(c)

# d = {'house': ['bungalow','cottage','townhouse', 'villa'], 'apartment':['condominium', 'casa', 'loft', 'serviced apartment']}
# for i in cur.fetchall():
#     k,b = random.choice(list(d.items()))
#     m = random.choice(b)
#     c = "update properties set property_type = '"+ k +"' , property_subtype = '"+ m +"' where property_id = "+str(i[0])+";"
#     cur.execute(c)
# 10/01 02:00 PM - 10/04 10:00 PM

# def check(m):
#     if m<9:
#         m = '0'+str(m)
#     else:
#         m = str(m)
#     return m
# for i in cur.fetchall():
#     d1 = random.randint(1, 31)
#     h1 = random.randint(1, 11)
#     mi1 = random.choice(['00', '30'])
#     m1 = random.randint(1, 5)
#     d2 = random.randint(1, 31)
#     m2 = random.randint(5, 12)
#     h2 = random.randint(1, 11)
#     mi2 = random.choice(['00', '30'])
#     l = [d1,m1,h1,d2,m2,h2]
#     s = []
#     for v in l:
#         s.append(check(v))
#
#
#
#     d = s[0]+"/"+s[1]+ " "+ s[2]+":"+mi1+" "+random.choice(['AM', 'PM'])+" - "+s[3]+"/"+s[4]+ " "+ s[5]+":"+mi2+" "+random.choice(['AM', 'PM'])
#     c = "insert into room_details (property_id, bedrooms_num, bed_num, bathrooms_num, duration, cost) values ('"+str(i[0])+"','"+str(random.randint(1,3))+"','"+str(random.randint(2,4))+"','"+str(random.randint(1,3))+"','"+d+"','"+str(random.randint(90,400))+"');"
#     cur.execute(c)
# cur.execute(" select user_id from user_detail;")
# l = ['user_12.jpg', 'user_2.jpg', 'user_18.jpg', 'user_17.jpg', 'user_7.jpg', 'user_9.jpg', 'user_11.jpg', 'user_10.jpg', 'user_8.jpg', 'user_16.jpg', 'user_13.jpg', 'user_5.jpg', 'user_1.jpg', 'user_6.jpg', 'user_14.jpg', 'user_15.jpg', 'user_4.jpg', 'user_3.jpg']
# for i in cur.execute(" select property_id, duration from room_details;").fetchall():
#     c = "update room_details set from_date = '" + i[1].split(' - ')[0]+ "', to_date = '" + i[1].split('-')[1] + "' where property_id =" + str(i[0]) + ";"
#     cur.execute(c)

# for i in cur.execute(" select property_id, from_date from room_details where substr(from_date, 1,2) = '9/';").fetchall():
#     c = "update room_details set from_date = '" + '0'+i[1] + "' where property_id =" + str(i[0]) + ";"
#     cur.execute(c)

# for i in cur.execute(" select property_id, to_date, substr(to_date, 6,6) as a from room_details where a like ' 9%'").fetchall():
#     a = i[1].replace(i[1].split(' ')[1], '0'+i[1].split(' ')[1])
#     c = "update room_details set to_date = '" + a + "' where property_id =" + str(i[0]) + ";"
#     cur.execute(c)


d = {'Greater metropolitan Sydney': ['Bayside', 'Blacktown', 'Burwood', 'Camden', 'Campbelltown', 'Canada Bay', 'Canterbury-Bankstown', 'Cumberland', 'Fairfield', 'Georges River', 'The Hills Shire', 'Hornsby Shire', "Hunter's Hill", 'Inner West', 'Ku-ring-gai', 'Lane Cove', 'Liverpool', 'Mosman', 'Northern Beaches', 'North Sydney', 'Parramatta', 'Penrith', 'Randwick', 'Ryde', 'Strathfield', 'Sutherland Shire', 'Sydney', 'Waverley', 'Willoughby', 'Woollahra'],
     'Sydney surrounds': ['Blue Mountains', 'Central Coast', 'Hawkesbury', 'Wollondilly Shire'],
     'Mid North Coast': ['Bellingen Shire', 'Clarence Valley', 'Coffs Harbour', 'Kempsey Shire', 'Nambucca Shire', 'Port Macquarie-Hastings', 'Lord Howe Island'],
     'Murray': ['Albury', 'Balranald Shire', 'Berrigan Shire', 'Edward River', 'Federation', 'Greater Hume Shire', 'Murray River', 'Murrumbidgee', 'Snowy Valleys', 'Wentworth Shire'],
     'Murrumbidgee': ['Carrathool Shire', 'Coolamon Shire', 'Griffith', 'Cootamundra-Gundagai', 'Hay Shire', 'Junee Shire', 'Leeton Shire', 'Lockhart Shire', 'Narrandera Shire', 'Temora Shire', 'Wagga Wagga'],
     'Hunter': ['Cessnock', 'Dungog Shire', 'Lake Macquarie', 'Maitland', 'Mid-Coast', 'Muswellbrook', 'Newcastle', 'Port Stephens', 'Singleton', 'Upper Hunter Shire'],
     'Illawarra': ['Kiama', 'Shellharbour', 'Shoalhaven', 'Wingecarribee Shire', 'Wollongong'],
     'Richmond-Tweed': ['Ballina Shire', 'Byron Shire', 'Kyogle', 'Lismore', 'Richmond Valley', 'Tweed Shire'],
     'Canberra Region': ['Bega Valley Shire', 'Eurobodalla Shire', 'Goulburn Mulwaree', 'Hilltops', 'Queanbeyan–Palerang', 'Snowy Monaro', 'Upper Lachlan Shire', 'Yass Valley'],
     'Northern': ['Armidale', 'Glen Innes Severn', 'Gunnedah Shire', 'Gwydir Shire', 'Inverell Shire', 'Liverpool Plains Shire', 'Moree Plains Shire', 'Narrabri Shire', 'Tamworth', 'Tenterfield Shire', 'Uralla Shire', 'Walcha Shire'],
     'Central West': ['Bathurst', 'Bland Shire', 'Blayney Shire', 'Cabonne Shire', 'Cowra Shire', 'Forbes Shire', 'Lachlan Shire', 'Lithgow', 'Mid-Western', 'Oberon Shire', 'Orange', 'Parkes Shire', 'Weddin Shire'],
     'North Western': ['Bogan Shire', 'Bourke Shire', 'Brewarrina Shire', 'Cobar Shire', 'Coonamble Shire', 'Dubbo', 'Gilgandra Shire', 'Narromine Shire', 'Walgett Shire', 'Warren Shire', 'Warrumbungle Shire'],
     'Far West':['Broken Hill', 'Central Darling Shire', 'Unincorporated Far West']}
# m = []
#
# k = [3, 5, 6, 7, 10, 12]
# for i in range(0,1000):
#      l = set([1, 2, 4, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
#      for j in range(random.randint(0,6)):
#           l.add(random.choice(k))
#      m.append(tuple(l))
#      j = 0
# for i in cur.execute(" select property_id, amenities_list from accom_amenities").fetchall():
#      d = i[1].replace(', ',',')
#      c = "update accom_amenities set amenities_list ='"+d+"' where property_id="+str(i[0])+";"
#      cur.execute(c)
#
L = []
cur = con.cursor()
da = [i[0]  for i in  cur.execute(" select property_id from properties;").fetchall()][350:400]
pa =  [i[0]  for i in  cur.execute(" select user_id from user_detail;").fetchall()[0:400]]
print (da)
print (pa)
sa = ['booked','saved']

for i in da:
     u =  random.choice(pa)
     s = random.choice(sa)
     q =  random.choice([1,2,3,4,5])
     cp = random.choice(['134', '155', '251', '359', '218', '249', '221', '311', '258', '164', '125', '299', '308', '256', '124', '120'])
     c = "insert into visitor_property values ('{}','{}','{}','{}','{}','{}')".format(u,i,s, '10/16 08:00 AM - 10/17 04:00 PM', str(q),  cp)
     cur.execute(c)

# for i in cur.execute(" select user_id, password  from user_detail;").fetchall():
#     cur.execute("update user_detail set password=\'"+generate_password_hash(i[1])+"\' where user_id=\'"+str(i[0])+"\'")

# print (check_password_hash(generate_password_hash('abc'),'abc'))
con.commit()
con.close()


