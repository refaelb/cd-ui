from os import name, system
from urllib import response
from flask import jsonify, render_template
from flask import request
from common import ci_cd
from flask import Flask
import yaml
import json
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
    ci_cd(namespace,host,repo,tag,reg,branch,ingress,Ruser,Rpass,Duser,Dpass,token)
    return render_template('pipline.html')



@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json    
    print(data)
    with open('test.txt','w+')as till:
        yaml.dump(request.json,till)
        a = request.json
        b = json.dumps(a)
    # return jsonify(data)
    return('okk')

if __name__ == '__main__':
    app.run(debug=True)
