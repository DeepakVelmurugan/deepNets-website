from flask import Flask, url_for, render_template, request, redirect,session
import requests

app = Flask(__name__)

@app.route('/',methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/fc',methods=["GET"])
def fc():
    return render_template('fc.html')

@app.route('/conv',methods=["GET"])
def conv():
    return render_template('conv.html')
    
@app.route('/about',methods=["GET"])
def about():
    request = requests.get(url='https://virtual-data-scientist.herokuapp.com')
    return render_template('about.html')
if __name__ == '__main__' :
    app.run(debug=True)