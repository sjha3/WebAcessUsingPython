import urllib.parse, urllib.error, urllib.request
import json
#Note : Get token from https://developers.facebook.com/tools/explorer/
#options to url are passed using '?'
#multiple fields can be passed with '&' separation : https://graph.facebook.com/v2.12/me?fields=id,photos&access_token=#
token='#'
def get_url_data(url):
    url = url + 'access_token=' + token  # encode place here
    print('URL :', url)
    uh = urllib.request.urlopen(url)
    header = uh.getheaders()
    data = uh.read().decode()
    json_data = json.loads(data)
    print('headers :',header)
    print("Json_output :: ", json.dumps(json_data,indent=2))


print('============ Just me===========')
url = 'https://graph.facebook.com/v2.12/me?'
get_url_data(url)

print('============Me with friends===========')
url_with_friends= 'https://graph.facebook.com/v2.12/me/friends?'
get_url_data(url_with_friends)

print('============My photos===========')
url_with_photos= 'https://graph.facebook.com/v2.12/me?fields=id,photos&'
get_url_data(url_with_photos)

print('=============albums======')
url_with_photos= 'https://graph.facebook.com/v2.12/me?fields=albums.limit(5),posts.limit(5)&'
get_url_data(url_with_photos)
