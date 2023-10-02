#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter


@app.route('/count/<int:parameter>')
def count(parameter):
    x = range(0, parameter)
    list_of_strings = [f'{n}\n' for n in x]
    return ''.join(list_of_strings)


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        result = None
    return str(result)

# @app.route('/<string:username')
# def usser(username):
#     return f'<h1> Profile for {username}</h1>'


# if __name__ == '__main__':
#     app.run(port=5555, debug=True)


# if __name__ == '__main__':
#     app.run(port=5555, debug=True)
