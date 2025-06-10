# app0_hello.py

from flask import Flask

app = Flask(__name__)

# @
@app.route('/')
def hello():

    return '나의 첫 파이썬 웹'