import os

from flask import Flask, render_template, jsonify, request
import requests
import json


app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://franz8410:test@3.34.48.67', 27017)
# client = MongoClient('localhost', 27017)
db = client.mobilecard


@app.route('/')
def log_in():
    return render_template('login.html')


@app.route('/oauth')
def oauth():
    code = str(request.args.get('code'))
    return str(code)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/my_page')
def my_page():
    return render_template('my_page.html')


@app.route('/search', methods=['GET'])
def get_school():
    school_name = request.args.get('schoolName')
    school_result = list(db.school.find({'name':{'$regex': school_name}}, {'_id': False}))
#   exact 검색을 할 경우엔 아래의 코드
#   school_result = list(db.school.find({'name': school_name}, {'_id': False}))
    print(school_result)
    result = {'result': 'success', 'msg': school_result}
    return jsonify(result)


@app.route('/choice', methods=['GET'])
def choice_school():
    choice_school_name = request.args.get('choiceSchoolName')
    choice_school_result = list(db.school.find({'name': choice_school_name}, {'_id': False}))
    print(choice_school_result)
    result = {'result': 'success', 'msg': choice_school_result}
    return jsonify(result)


# @app.route('/webhook', methods=['POST'])
# def web_hook():
#     web_hook_data = request.form
#     print(web_hook_data)
#     os.system('cd /home/ubuntu/my_projects && git pull')
#     return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


# 로그인 정보 참조 코드
# from bson import ObjectId
# from flask import Flask, render_template, request, session, redirect, jsonify
# from pymongo import MongoClient
#
# app = Flask(__name__)
# app.secret_key = 'mobilecard'
#
# client = MongoClient('localhost', 27017)
# db = client.mobilecard
#
#
# @app.route('/')
# def hello_world():
#     # 세션에 'sessionID'라는 변수가 있는
#     if 'sessionID' in session:
#         # 세션에 'sessionID'라는 변수의 값을 가져와서
#         session_id = session['sessionID']
#         # 'sessionID'에 담긴 값(유저 생성시에 만들어진 _id 값)에 대한
#         # 유저 정보가 user DB에 있는지 확인
#         user = db.user.find_one({'_id': ObjectId(session_id)})
#
#         # 세션에 'sessionID'라는 변수의 값이 비어있거나
#         # 'sessionID'에 담긴 값(유저 생성시에 만들어진 _id 값)에 대한
#         # 유저 정보가 없다면
#         if session_id is None or user is None:
#             # 로그인 페이지를 띄워줌
#             return render_template('login.html')
#         # 아니라면 로그인 한 세션이 있는 유저이므로 메인 페이지로 보냄
#         return render_template('main.html', nickname=user['nickname'])
#     return render_template('login.html')
#
#
# @app.route('/login', methods=['GET'])
# def login_page():
#     return render_template('login.html')
#
#
# @app.route('/login', methods=['POST'])
# def login():
#     user_id = request.form['userID']
#     password = request.form['password']
#
#     user = db.user.find_one({'user_id': user_id, 'password': password})
#
#     if user is not None:
#         # 세션을 생성하는데
#         # 세션에 'sessionID'라는 변수에
#         # 유저 생성시 만들어진 _id 값을 넣어둠(유저 고유 식별자이기 때문)
#         session['sessionID'] = str(user['_id'])
#         return redirect('/')
#     return render_template('login.html')
#
#
# @app.route('/signUp', methods=['GET'])
# def sign_up_page():
#     return render_template('signUp.html')
#
#
# @app.route('/signUp', methods=['POST'])
# def sign_up():
#     user_id = request.form['userID']
#     password = request.form['password']
#     nickname = request.form['nickname']
#
#     db.user.insert_one({'user_id': user_id, 'password': password, 'nickname': nickname})
#     return render_template('login.html')
#
#
# @app.route('/logout', methods=['POST'])
# def logout():
#     session.pop('sessionID')
#     return jsonify({'result': 'success'})
#
#
# if __name__ == '__main__':
#     app.run()
