import urllib.parse, urllib.error, urllib.request
import json
import re
#url = https://api.github.com/repos/sjha3/WebAcessUsingPython/commits  #shows all commits
#url = 'https://api.github.com/users/sjha3' #gives all the details
#url = 'https://api.github.com/users/sjha3/repos' #gives all the repo
token='44fb5f549425d1c2733c6372edebdf128daf798f'
commits=[]

def get_url_fh(url):
    print('URL :', url)
    try :
        uh = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.reason)
    except urllib.error.URLError as er:
        print(er.code)
        print(er.reason)
    return uh

def get_commits(url):
    #url = url + 'access_token=' + token  # encode place here
    uh=get_url_fh(url)
    url_info = uh.info()
    print('url info  : ', url_info)
    header = uh.getheaders()
    data = uh.read().decode()
    json_data = json.loads(data)
    #print('headers :', header,' type ',type(header))
    #print("Json_output :: ", json.dumps(json_data, indent=2))
    for elem in json_data:
        if 'sha' in elem:
            commits.append(elem['sha'])


#url = 'https://api.github.com/users/sjha3' #gives all the details
#url = 'https://api.github.com/users/sjha3/repos' #gives all the repos
#get_url_data(url)
url = 'https://api.github.com/repos/sjha3/WebAcessUsingPython/commits'
get_commits(url)
print('========= Commit Hashes===========')
print(commits)
print('========= Details of Commit Hash ',commits[0])
url = url+'/'+commits[0]
fh = get_url_fh(url)
data = fh.read().decode()
json_data = json.loads(data)
print(json.dumps(json_data, indent=2))
print('files changed : ')
for file in json_data['files']:
    print(file['filename'])