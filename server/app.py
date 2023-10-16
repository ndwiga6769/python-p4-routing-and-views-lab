#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route("/print/<my_string>")
def print_string(my_string):
    print (my_string)
    return f"{my_string}"
@app.route("/count/<int:number>")
def count(number):
    nums = ""
    for number in range(0,number):
        nums += str(number) + "\n"
    return nums

@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1,operation,num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else :
        print("invalid operation")

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
