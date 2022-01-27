#!/bin/bash
# curl -u 'refaelb:Refael316444058' \
#   -X POST \
#   -H "Accept: application/vnd.github.v3+json" \
#   -d '{"name":"re"}' \
#   'https://api.github.com/refaelb/cd-ui/settings/hooks/'
curl -u 'refaelb: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' \
  -X POST \
  -H "Accept: application/vnd.github.v3+json" \
  -d '{
    "type": "Repository",
    "id": 12345678,
    "namespace": "shitt",
    "name": "web",
    "active": true,
    "events": [
      "push"
    ],
    "config": {
      "content_type": "text",
      "insecure_ssl": "false",
      "url": "http://52.170.32.128:5000/webhook"
    },
    "last_response": {
      "code": null,
      "status": "unused",
      "namespace": "shit",
      "message": {
        "namespace": "shitt"
      }
    }
  }' \
 'https://api.github.com/repos/refaelb/cd-ui/hooks' 
