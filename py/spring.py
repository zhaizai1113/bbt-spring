from flask import Flask
from flask import Response,session
from flask import request
#from app import app
from config import db
import config
from database import check1,adduser,queryuser,checktel,updateuser
import pymysql
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = config.app['secret_key']

con=pymysql.connect(db['host'],db['user'],db['passwd'],db['database'],charset='utf8')
cursor=con.cursor()

@app.route('/',methods=['post','get'],endpoint='apply')
def apply():
    # username = request.values.get("username")
    # sex = request.values.get("sex")
    # grade = request.values.get("grade")
    # location = request.values.get("location")
    # academy = request.values.get("academy")
    # phone = request.values.get("phone")
    # first = request.values.get("first")
    # second = request.values.get("second")
    # adjust = request.values.get("adjust")
    # time = request.values.get("time")
    # introduce = request.values.get("introduce")
    username = "admin"
    sex = "0"
    grade = "1"
    location = "第三次调试"
    academy = "软件学院"
    phone = "15564660744"
    first = "软件"
    second = "医学"
    adjust = "0"
    time = '2020-4-5'
    introduce = "我爱学习"
    #print('hello1')
    if check1(username, sex, grade, location, academy, phone, first, adjust, time, introduce):
        #print('check函数正常')
        result = adduser(username, sex, grade, location, academy, phone, first, second, adjust, time, introduce)
    else:
        result = {'errmsg':'error2'}
        #print('hello2')
    return Response(json.dumps(result),content_type="applation/json")

@app.route('/query',methods=['post','get'],endpoint='query')
def query():
# #这样只能做到查询，而修改则可能改变掉作为判断条件的东西，而此时id是不会变的，应该通过phone查询id，再通过这，获得信息，并修改信息
# #看情况修改把
    tel = request.form['phone']
    if checktel(tel):
        _dir = queryuser(tel)
    else:
        _dir = {'errmsg':"电话格式有误",'msg': False}
    return Response(json.dumps(_dir),content_type="applation/json")


@app.route('/update',methods=['post'],endpoint='update')
def update():
    _id = session['id']
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
    _dir = updateuser(username, sex, grade, location, academy, phone, first, second, adjust, time, introduce,_id)
    return Response(json.dump(_dir),content_type="applation/json")


@app.route('/introduce',methods=['post'])
def department_introduce():
    _id = request.values.get("id")
    sql = 'select * from departments where id = %d' ,(_id,)
    cursor.execute(sql)
    result = cursor.fetchone()
    _dir = {'usernmae':result[1],'introduce':result[2]}
    return Response(json.dump(_dir),content_type="applation/json")

if __name__ == '__main__':
    app.run()