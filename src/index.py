from asyncio import sleep
from concurrent.futures import Executor
from http.client import OK, responses
from os import name
from flask import render_template
from flask import request
# from ci_cd import *
from flask import Flask
from flask import Flask, request ,Response
import flask 

from validate import *
from webhook import *
from threading import Thread
import time

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
    creaeteWebhook(namespace,host,repo,tag,reg,branch,ingress,Ruser,Rpass,Duser,Dpass,token)

    return render_template('pipline.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = (request.data) 
    print ("webhook post ")
    response = Response('hello')
    @response.call_on_close
    def on_close():
        validate(data)
    return response


if __name__ == '__main__':
    app.run(debug=True)
