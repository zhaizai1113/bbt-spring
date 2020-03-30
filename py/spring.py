from flask import Flask
from flask import Response,session
from flask import request
# from wtforms import ValidationError,StringField
# from wtforms.validators import DataRequired,Length,Regexp
import pymysql
import json
app = Flask(__name__)

con=pymysql.connect('localhost','root','123456','spring',charset='utf8')
cursor=con.cursor()

@app.route('/apply',methods=['post'])
def apply():
    username = request.values.get("username")
    sex = request.values.get("sex")
    grade = request.values.get("grade")
    location = request.values.get("location")
    academy = request.values.get("academy")
    phone = request.values.get("phone")
    first = request.values.get("first")
    second = request.values.get("second")
    adjust = request.values.get("adjust")
    time = request.values.get("time")
    introduce = request.values.get("introduce")
    cursor.execute("INSERT INTO users (username, sex, grade, location, academy, phone, first, second, adjust, time, introduce)"
                   "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                   (username, sex, grade, location, academy, phone, first, second, adjust, time, introduce))
    con.commit()
    sql = 'select * from users where phone = %s' %phone
    cursor.rowcount = cursor.execute(sql)
    if cursor.rowcount == 1 :
        result = {'msg':True}
    else:
        result = {'msg':False}
    return Response(json.dumps(result))

@app.route('/query',methods=['post'])
def query():
# #这样只能做到查询，而修改则可能改变掉作为判断条件的东西，而此时id是不会变的，应该通过phone查询id，再通过这，获得信息，并修改信息
# #看情况修改把
    tel = request.form['phone']
    sql = 'select * from users where phone = %s' %tel
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
        _dir = {'username':username, 'sex':sex, 'grade':grade, 'location':location, 'academy':academy,
                'phone':phone, 'first':first, 'second':second, 'adjust':adjust, 'time':time,
                'introduce':introduce, 'msg':True}
    else:
        _dir = {'msg':False}
    return Response(json.dumps(_dir))

@app.route('/update',methods=['post'])
def update():
    _id = session['id']
    # tel = '15581490744'
    # sql = 'select * from users where phone = %s' % tel
    # cursor.rowcount = cursor.execute(sql)
    # if cursor.rowcount == 1:
    #     result = cursor.fetchone()
    #     # session['id'] = result[0]
    #     username = result[1]
    #     sex = result[2]
    #     grade = result[3]
    #     location = result[4]
    #     academy = result[5]
    #     phone = result[6]
    #     first = result[7]
    #     second = result[8]
    #     adjust = result[9]
    #     time = result[10]
    #     introduce = result[11]
    username = request.values.get("username")
    sex = request.values.get("sex")
    grade = request.values.get("grade")
    location = request.values.get("location")
    academy = request.values.get("academy")
    phone = request.values.get("phone")
    first = request.values.get("first")
    second = request.values.get("second")
    adjust = request.values.get("adjust")
    time = request.values.get("time")
    introduce = request.values.get("introduce")
    sql = 'update users set username = "%s", sex = "%s", grade = "%s", location = "%s", academy = "%s", phone ="%s", first = "%s", second = "%s", adjust = "%s", time = "%s" , introduce = "%s" where id = %d' %(username ,sex ,grade ,location ,academy, phone ,first,second ,adjust ,time ,introduce,_id)
    cursor.execute(sql)
    cursor.commit()
    return Response(json.dump({'msg': True}))

@app.route('introduce',methods=['post'])
def department_introduce():
    _id = request.values.get("id")
    sql = 'select * from departments where id = %d' %_id
    cursor.execute(sql)
    result = cursor.fetchone()
    _dir = {'usernmae':result[1],'introduce':result[2]}
    return Response(json.dump(_dir))


if __name__=='__main__':
    app.run()