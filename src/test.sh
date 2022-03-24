curl -X POST \
  https://api.github.com/repos/refaelb/ci-cd/hooks \
  -H 'authorization: token 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' \
  -H 'cache-control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{ 
  "config": { 
    "url": "http://52.170.32.128:5000/webhook" ,
    "name": "webhook11122",
    "content_type": "json"
  }, 
  "events": [ 
    "push"
  ]
}'