import requests
import json
webhook_url = 'http://127.0.0.1:5000//webhook'
data = { 'namespace': 'fre',
        'host': 'test',
        'repo': 'https://github.com/refaelb/image_project.git',
        'tag': 'v0.0.1',
        'reg': 'refael058325',
        'branch': 'dev',
        'ingress': 'ew',
        'Ruser': 'refael058325',
        'Rpass': 'Rootroot316444058',
        'Duser': 'refaelb',
        'Dpass': 'Refael'}
requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})