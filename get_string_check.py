from flask import Flask, render_template, request, url_for, redirect, jsonify
import pandas as pd
import re
app = Flask(__name__)
@app.route('/', methods=['GET'])
def register():
    return render_template("get_string.html")

@app.route('/check_string', methods=['GET'])
def check_str():
    if request.method == 'GET':
        str = request.args.get('str')
        with open('samp') as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
        if str in lines:
            return 'Given location is present in the file'
        else:
            return 'Given location is NOT present in the file'

if __name__ == '__main__':
    app.run()