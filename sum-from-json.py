import urllib.parse, urllib.error, urllib.request
import json

url = 'http://py4e-data.dr-chuck.net/comments_72035.json'
uh=urllib.request.urlopen(url)
data = uh.read().decode()
json_data = json.loads(data)
comments = json_data['comments']
sum = 0
for comment in comments:
    sum = sum+int(comment['count'])

print("Final Sum : ",sum)