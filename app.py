from flask import Flask,render_template,request,redirect,flash,jsonify
import os
import requests
import urllib.request ,json 
api_url = "https://jsonplaceholder.typicode.com/todos/1"
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec2]1'

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'remon' or request.form['password'] != '1234':
            error = 'Invalid credentials'
           
        else:
            flash('You were successfully logged in')
            
            return redirect('/index')
    return render_template('login.html', error=error)

@app.route("/getJsonData")
def get_json_data():
    try:
      api_response = requests.get(api_url)
      json_dict = api_response.json()
      return jsonify(json_dict.get('title'))
      return render_template('index.html',json_dict=json_dict)
    except Exception as e:
      print("Error occured :: %s" % e.message.get)

@app.route('/index', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        return redirect(f'/result/{name}/{age}')
    return render_template('index.html')

@app.route('/remon/<string:value>')
def string(value):
    return f"<p>Hi this is a string value {value}</p>"

@app.route('/path/<path:value>')
def path(value):
    return f"<p>Hi this is a path value {value}</p>"

@app.route('/result/<name>/<age>')
def result(name, age):
    return render_template('result.html', name=name, age=age)
    
if __name__ == '__main__':
    app.run(debug=True)