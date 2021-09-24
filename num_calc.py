from flask import Flask, render_template, request, url_for, redirect, jsonify
import pandas as pd
import re
app = Flask(__name__)
@app.route('/', methods=['GET'])
def register():
    return render_template("get_num.html")

@app.route('/compute', methods=['GET'])
def cmp_data():
    if request.method == 'GET':
        num1 = request.args.get('num1')
        num2 = request.args.get('num2')
        sum = str(int(num1) + int(num2))
        # print(type(sum),'@@@@@@@@@@@@@@@@@@@')
        return sum

if __name__ == '__main__':
    app.run()