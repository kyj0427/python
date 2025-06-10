# app1_route.py
from zoneinfo import reset_tzpath

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello~'
# http://127.0.0.1:5000

@app.route('/users/<username>')
def get_user(username):
    return username + "님 입장"
# 127.0.0.1:5000/users/사용자이름  =>고정 url 을 주고 사용자이름을 뒤에 붙혀준다
