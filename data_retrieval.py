import time

from flask import Flask, render_template, request, url_for, redirect, jsonify
import pandas as pd
app = Flask(__name__)
@app.route('/', methods=['POST'])
def register():
    return render_template("bio_form.html")

@app.route('/retrieve_data', methods=['GET', 'POST'])
def retrieve_data():
    if request.method == 'GET':
        data = {}
        data['username'] = request.args.get('username')
        data['age'] = request.args.get('age')
        data['place'] = request.args.get('place')
        csv_file = "details_from_user.csv"
        df = pd.DataFrame([data])
        df.to_csv(csv_file, index = False, encoding='utf-8')
        return jsonify({'Name':data['username'],
                        'Age':data['age'],
                        'Place':data['place']})

if __name__ == '__main__':
    app.run()


