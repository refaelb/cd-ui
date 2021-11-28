from os import name, system
from flask import render_template
from flask import request
from ci_cd import ci_cd
from flask import Flask
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
    ci_cd(namespace,host,repo,tag,reg,branch,ingress,Ruser,Rpass,Duser,Dpass)
    return render_template('pipline.html')



