from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.mobilecard

## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('home.html')

