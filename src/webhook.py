# import requests
# import json
# def creaeteWebhook(namespace,host,repo,tag,reg,branch,ingress,Ruser,Rpass,Duser,Dpass,imageName,token):
    

#     url = "https://api.github.com/repos/{}/{}/hooks".format(Ruser,imageName)

#     payload = json.dumps({
#     "type": "Repository",
#     "id": 12345678,
#     "name": "web",
#     "active": "True",
#     "events": "push",
#     "config": {
#         "content_type": "text",
#         "insecure_ssl": "false",
#         "url": "http://52.170.32.128:5000/webhook",
#         "namespace": f"{namespace}",
#         "tag": f"{tag}",
#         "repo": f"{repo}",
#         "Ruser": f"{Ruser}",
#         "Rpass": f"{Rpass}",
#         "ingress": f"{ingress}",
#         "branch": f"{branch}",
#         "host": f"{host}",
#         "reg": f"{reg}",
#         "pass": f"{Duser}",
#         "pass": f"{Dpass}"
#         }
#     })
#     headers = {
#     'Authorization': 'Bearer '+ token + '',
#     'Content-Type': 'application/json'
#     }

#     response = requests.request("POST", url, headers=headers, data=payload)

#     print(response.text)
# token = ('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')
# creaeteWebhook("namespace","host","cd-ui","tag","reg","branch","ingress","refaelb","Rpass","Duser","Dpass","cd-ui",token)
import requests
import json

url = "https://api.github.com/repos/refaelb/cd-ui/hooks"

payload = json.dumps({
  "type": "Repository",
  "id": 12345678,
  "name": "web",
  "active": True,
  "events": [
    "push"
  ],
  "config": {
    "content_type": "text",
    "insecure_ssl": "false",
    "url": "http://52.170.32.128:5000/webhook",
    "namespace": "shit",
    "tag": "tag",
    "repo": "repo",
    "username": "username"
  }
})
headers = {
  'Authorization': 'Bearer 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',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)