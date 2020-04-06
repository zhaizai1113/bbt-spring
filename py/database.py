from config import db
from flask import session
import pymysql

con=pymysql.connect(db['host'],db['user'],db['passwd'],db['database'],charset='utf8mb4')
cursor=con.cursor()

def check1(username, sex, grade, location, academy, phone, first, adjust, time, introduce):
    if username is "":
        return False
    if sex is "":
        return False
    if grade is "":
        return False
    if location is "":
        return False
    if academy is "":
        return False
    if phone is "":
        return False
    else:
        tel = str(phone)
        if tel.__sizeof__() is 11:
            if not tel[0] is '1':
                print('666')
                return False
        else:
            return True
    if first is "":
        return False
    if adjust is "":
        return False
    if time is "":
        return False
    if introduce is "":
        return False
    return True

def adduser(username, sex, grade, location, academy, phone, first, second, adjust, time, introduce):
    #print('3')
    cursor.rowcount = cursor.execute('select * from users where phone = %s', (phone,))
    if cursor.rowcount == 1 :
        return {'msg':False,'errmsg':"该电话号码已被使用报名"}
    cursor.execute("INSERT INTO users (username, sex, grade, location, academy, phone, first, second, adjust, time, introduce)"
                   "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                   (username, sex, grade, location, academy, phone, first, second, adjust, time, introduce))
    #print('4')
    try:
        #print('5')
        con.commit()
        return {'msg': True}
    except AssertionError as error:
        print(error)
        return {'msg': False, 'errmsg': "数据插入出错"}

def checktel(phone):
    if phone is "":
        return False
    else:
        tel = str(phone)
        if tel.__sizeof__() is 11:
            if not tel[0] is '1':
                return False
        else:
            return False


def queryuser(tel):
    sql = 'select * from users where phone = %s', (tel,)
    cursor.rowcount = cursor.execute(sql)
    if cursor.rowcount == 1 :
        result = cursor.fetchone()
        session['id'] = result[0]
        username = result[1]
        sex = result[2]
        grade = result[3]
        location = result[4]
        academy = result[5]
        phone = result[6]
        first = result[7]
        second = result[8]
        adjust = result[9]
        time = result[10]
        introduce = result[11]
        return {'username':username, 'sex':sex, 'grade':grade, 'location':location, 'academy':academy,
                'phone':phone, 'first':first, 'second':second, 'adjust':adjust, 'time':time,
                'introduce':introduce, 'msg':True}
    else:
        return {'msg':False,'errmsg':"您尚未报名"}

def updateuser(username, sex, grade, location, academy, phone, first, second, adjust, time, introduce,_id):
    sql = 'update users set username = "%s", sex = "%s", grade = "%s", location = "%s", academy = "%s", phone ="%s", first = "%s", second = "%s", adjust = "%s", time = "%s" , introduce = "%s" where id = %d' % (
    username, sex, grade, location, academy, phone, first, second, adjust, time, introduce, _id)
    cursor.execute(sql)
    try:
        con.commit()
        return {'msg':True}
    except:
        return {'msg':False}