#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

@app.route('/count/<int:number>')

def count(number):
    display_nums = f''
    for num in range(number):
        display_nums += f'{num}\n'
    return display_nums

@app.route('/math/<int:num1>/<string:operator>/<int:num2>')
def math(num1, operator, num2):
    operations = ["+","-","*","%"]
    if operator in operations:
        return str(eval(f"{num1} {operator} {num2}"))
    elif operator == 'div':
        return str(eval(f"{num1} / {num2}"))
    else:
        return 'Operation not recognized. Please use one of the following: + - * div %'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
