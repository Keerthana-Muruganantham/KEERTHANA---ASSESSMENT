from flask import Flask, render_template, request, url_for, redirect, jsonify
import pandas as pd
import re
app = Flask(__name__)
@app.route('/', methods=['GET'])
def register():
    return render_template("login_form.html")

@app.route('/get_data', methods=['GET'])
def get_data():
    if request.method == 'GET':
        data = {}
        username = request.args.get('username')
        password = request.args.get('password')
        place = request.args.get('place')
        if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[$@#])[\w\d$@#]{6,12}$", password):
            return jsonify({"message": "Valid user details", "code":200})
        else:
            return jsonify({"message": "Invalid user details", "code":401})

if __name__ == '__main__':
    app.run()