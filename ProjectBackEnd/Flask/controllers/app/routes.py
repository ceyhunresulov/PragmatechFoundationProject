from run import app 
from flask import render_template,redirect,request

# app index route

@app.route('/', methods=['GET','POST'])
def app_index():
    return render_template('app/index.html')