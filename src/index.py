from os import name
from flask import render_template
from flask import request
from common import *
from flask import Flask
from flask import Flask, request
import yaml
import json
from validate import validate
from webhook import *


app = Flask(__name__)

@app.route('/' , methods=['GET','POST'])
def home():
    return render_template('home.html')


@app.route('/pipline', methods=['GET', 'POST'])
def pipline():
    namespace = request.form['namespace']
    Duser = request.form['docker-username']
    Dpass = request.form['docker-password']
    Ruser = request.form['repo-username']
    Rpass = request.form['repo-username']
    host = request.form['host']
    repo = request.form['repo']
    tag = request.form['tag']
    reg = request.form['reg']
    branch = request.form['branch']
    ingress = request.form['ingress']
    token = request.form['token']
    # ci_cd(namespace,host,repo,tag,reg,branch,ingress,Ruser,Rpass,Duser,Dpass,token)
    creaeteWebhook(namespace,host,repo,tag,reg,branch,ingress,Ruser,Rpass,Duser,Dpass,token)

    return render_template('pipline.html')



@app.route('/webhook', methods=['POST'])
def webhook():
    data = (request.data) 
    print(data)
    print ("its work")
    validate(data)

    return('ok')

if __name__ == '__main__':
    app.run(debug=True)
