# curl -i -u refaelb:Refael316444058 https://api.github.com/refaelb/cd-ui

curl -i -H "Authorization: token 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" \
    -d '{ \
        "name": "blog", \
        "auto_init": true, \
        "private": true, \
        "gitignore_template": "nanoc" \
      }' \
    https://api.github.com/refaelb/cd-ui