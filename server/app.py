#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<parameter>')
def count(parameter):
    count_value = int(parameter)
    result = ''

    for x in range(count_value):
        result += f'{x}\n'
    
    return result

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return "Invalid input", 400

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Invalid operation"
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"

    return str(result)
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)

