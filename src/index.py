from os import name, system
from flask import render_template
from flask import request
from ci_cd import ci_cd
from flask import Flask
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
    ci_cd(namespace,host,repo,tag,reg,branch,ingress,Ruser,Rpass,Duser,Dpass)
    return render_template('pipline.html')



@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        a = request.json
        b = json.dumps(a)
        storedata = json.loads(b)
        li=[]
        for val in storedata:
            v = storedata[val]
            li.append(v)
        namespace = li[0]
        host = li[1]
        repo = li[2]
        tag = li[3]
        reg = li[4]
        branch = li[5]
        ingress = li[6]
        Ruser = li[7]
        Rpass = li[8]
        Duser = li[9]
        Dpass = li[10]
        ci_cd(namespace,host,repo,tag,reg,branch,ingress,Ruser,Rpass,Duser,Dpass)

        return 'success', 200
    else:
        return('err')

if __name__ == '__main__':
    app.run(debug=True)
