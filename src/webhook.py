import requests
import json
import index
from common import *
def creaeteWebhook(namespace,host,repo,tag,reg,branch,ingress,Ruser,Rpass,Duser,Dpass,imageName,token):
    url = "https://api.github.com/repos/{}/{}/hooks".format(Ruser,imageName)
    payload = json.dumps({
    "type": "Repository",
    "id": 12345678,
    "name": "web",
    "active": True,
    "events": [
        "push"
    ],
    "config": {
        "content_type": "json",
        "insecure_ssl": "false",
        "url": "http://52.170.32.128:5000/webhook",
        "namespace": f"{namespace}",
        "tag": f"{tag}",
        "repo": f"{repo}",
        "Ruser": f"{Ruser}",
        "Rpass": f"{Rpass}",
        "ingress": f"{ingress}",
        "branch": f"{branch}",
        "host": f"{host}",
        "reg": f"{reg}",
        "Dpass": f"{Duser}",
        "Dpass": f"{Dpass}"
    }
    })
    headers = {
    'Authorization': 'Bearer '+ token + '',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    ci_cd(namespace,host,repo,tag,reg,branch,ingress,Ruser,Rpass,Duser,Dpass,token)


# creaeteWebhook("namespace","host","repo","tag","reg","branch","ingress","refaelb","Rpass","Duser","Dpass","ci-cd","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") 