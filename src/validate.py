import json

from ci_cd import *
# data = '{"zen":"Half measures are as bad as nothing at all.","hook_id":349673121,"hook":{"type":"Repository","id":349673121,"name":"web","active":true,"events":["push"],"config":{"branch":"branch","content_type":"json","Dpass":"Dpass","host":"host","ingress":"ingress","insecure_ssl":"false","namespace":"namespace","reg":"reg","repo":"repo","Rpass":"Rpass","Ruser":"refaelb","tag":"tag","url":"http://52.170.32.128:5000/webhook"},"updated_at":"2022-03-24T10:36:03Z","created_at":"2022-03-24T10:36:03Z","url":"https://api.github.com/repos/refaelb/ci-cd/hooks/349673121","test_url":"https://api.github.com/repos/refaelb/ci-cd/hooks/349673121/test","ping_url":"https://api.github.com/repos/refaelb/ci-cd/hooks/349673121/pings","deliveries_url":"https://api.github.com/repos/refaelb/ci-cd/hooks/349673121/deliveries","last_response":{"code":null,"status":"unused","message":null}},"repository":{"id":412045250,"node_id":"R_kgDOGI9Pwg","name":"ci-cd","full_name":"refaelb/ci-cd","private":false,"owner":{"login":"refaelb","id":59889842,"node_id":"MDQ6VXNlcjU5ODg5ODQy","avatar_url":"https://avatars.githubusercontent.com/u/59889842?v=4","gravatar_id":"","url":"https://api.github.com/users/refaelb","html_url":"https://github.com/refaelb","followers_url":"https://api.github.com/users/refaelb/followers","following_url":"https://api.github.com/users/refaelb/following{/other_user}","gists_url":"https://api.github.com/users/refaelb/gists{/gist_id}","starred_url":"https://api.github.com/users/refaelb/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/refaelb/subscriptions","organizations_url":"https://api.github.com/users/refaelb/orgs","repos_url":"https://api.github.com/users/refaelb/repos","events_url":"https://api.github.com/users/refaelb/events{/privacy}","received_events_url":"https://api.github.com/users/refaelb/received_events","type":"User","site_admin":false},"html_url":"https://github.com/refaelb/ci-cd","description":"ci cd","fork":false,"url":"https://api.github.com/repos/refaelb/ci-cd","forks_url":"https://api.github.com/repos/refaelb/ci-cd/forks","keys_url":"https://api.github.com/repos/refaelb/ci-cd/keys{/key_id}","collaborators_url":"https://api.github.com/repos/refaelb/ci-cd/collaborators{/collaborator}","teams_url":"https://api.github.com/repos/refaelb/ci-cd/teams","hooks_url":"https://api.github.com/repos/refaelb/ci-cd/hooks","issue_events_url":"https://api.github.com/repos/refaelb/ci-cd/issues/events{/number}","events_url":"https://api.github.com/repos/refaelb/ci-cd/events","assignees_url":"https://api.github.com/repos/refaelb/ci-cd/assignees{/user}","branches_url":"https://api.github.com/repos/refaelb/ci-cd/branches{/branch}","tags_url":"https://api.github.com/repos/refaelb/ci-cd/tags","blobs_url":"https://api.github.com/repos/refaelb/ci-cd/git/blobs{/sha}","git_tags_url":"https://api.github.com/repos/refaelb/ci-cd/git/tags{/sha}","git_refs_url":"https://api.github.com/repos/refaelb/ci-cd/git/refs{/sha}","trees_url":"https://api.github.com/repos/refaelb/ci-cd/git/trees{/sha}","statuses_url":"https://api.github.com/repos/refaelb/ci-cd/statuses/{sha}","languages_url":"https://api.github.com/repos/refaelb/ci-cd/languages","stargazers_url":"https://api.github.com/repos/refaelb/ci-cd/stargazers","contributors_url":"https://api.github.com/repos/refaelb/ci-cd/contributors","subscribers_url":"https://api.github.com/repos/refaelb/ci-cd/subscribers","subscription_url":"https://api.github.com/repos/refaelb/ci-cd/subscription","commits_url":"https://api.github.com/repos/refaelb/ci-cd/commits{/sha}","git_commits_url":"https://api.github.com/repos/refaelb/ci-cd/git/commits{/sha}","comments_url":"https://api.github.com/repos/refaelb/ci-cd/comments{/number}","issue_comment_url":"https://api.github.com/repos/refaelb/ci-cd/issues/comments{/number}","contents_url":"https://api.github.com/repos/refaelb/ci-cd/contents/{+path}","compare_url":"https://api.github.com/repos/refaelb/ci-cd/compare/{base}...{head}","merges_url":"https://api.github.com/repos/refaelb/ci-cd/merges","archive_url":"https://api.github.com/repos/refaelb/ci-cd/{archive_format}{/ref}","downloads_url":"https://api.github.com/repos/refaelb/ci-cd/downloads","issues_url":"https://api.github.com/repos/refaelb/ci-cd/issues{/number}","pulls_url":"https://api.github.com/repos/refaelb/ci-cd/pulls{/number}","milestones_url":"https://api.github.com/repos/refaelb/ci-cd/milestones{/number}","notifications_url":"https://api.github.com/repos/refaelb/ci-cd/notifications{?since,all,participating}","labels_url":"https://api.github.com/repos/refaelb/ci-cd/labels{/name}","releases_url":"https://api.github.com/repos/refaelb/ci-cd/releases{/id}","deployments_url":"https://api.github.com/repos/refaelb/ci-cd/deployments","created_at":"2021-09-30T11:54:49Z","updated_at":"2021-09-30T11:54:52Z","pushed_at":"2022-03-24T07:51:16Z","git_url":"git://github.com/refaelb/ci-cd.git","ssh_url":"git@github.com:refaelb/ci-cd.git","clone_url":"https://github.com/refaelb/ci-cd.git","svn_url":"https://github.com/refaelb/ci-cd","homepage":null,"size":44,"stargazers_count":0,"watchers_count":0,"language":null,"has_issues":true,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":0,"mirror_url":null,"archived":false,"disabled":false,"open_issues_count":1,"license":null,"allow_forking":true,"is_template":false,"topics":[],"visibility":"public","forks":0,"open_issues":1,"watchers":0,"default_branch":"main"},"sender":{"login":"refaelb","id":59889842,"node_id":"MDQ6VXNlcjU5ODg5ODQy","avatar_url":"https://avatars.githubusercontent.com/u/59889842?v=4","gravatar_id":"","url":"https://api.github.com/users/refaelb","html_url":"https://github.com/refaelb","followers_url":"https://api.github.com/users/refaelb/followers","following_url":"https://api.github.com/users/refaelb/following{/other_user}","gists_url":"https://api.github.com/users/refaelb/gists{/gist_id}","starred_url":"https://api.github.com/users/refaelb/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/refaelb/subscriptions","organizations_url":"https://api.github.com/users/refaelb/orgs","repos_url":"https://api.github.com/users/refaelb/repos","events_url":"https://api.github.com/users/refaelb/events{/privacy}","received_events_url":"https://api.github.com/users/refaelb/received_events","type":"User","site_admin":false}}'



def validate(data):
    d = json.loads(data)
    for i in d:
        if 'hook' == i:
            for x in d[i]:
                if x == 'config':
                    for y in d[i][x]:
                        print (y)
                        branch = d[i][x]['branch']
                        Dpass = d[i][x]['Dpass']
                        host = d[i][x]['host']
                        ingress = d[i][x]['ingress']
                        namespace = d [i][x]['namespace']
                        reg = d[i][x]['reg']
                        repo = d[i][x]['repo']
                        Rpass = d [i][x]['Rpass']
                        Ruser = d [i][x]['Ruser']
                        tag = d[i][x]['tag']
                        url = d[i][x]['url']
            # print(branch, Dpass)
            print (namespace, repo, tag, branch, Dpass, Ruser, Rpass, host, ingress,reg, url)
            ci_cd(namespace,host,repo,tag,reg,branch,ingress,Ruser,Rpass ,"shit",Dpass)
            break
# main()