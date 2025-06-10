# app.py
# flask run

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():




    return '파이썬 웹'