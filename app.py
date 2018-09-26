# coding=utf-8
from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    title = u'这是一个打招呼的页面'
    return render_template('index.html', title=title)


@app.route('/hj')
def huaji():
    title = u'9999+滑稽.jpg'
    return render_template('huaji.html', title=title)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
