import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup

html = urllib.request.urlopen(' http://py4e-data.dr-chuck.net/known_by_Trudy.html').read()
soup = BeautifulSoup(html, 'html.parser')
print('Get span tags')
tags = soup('span')
sum = 0
for tag in tags:
    #print('tag.content : ', tag.contents[0]) #tag.contents returns a list of contents
    sum = sum + int(tag.contents[0])
    #print(sum)

print('final sum :', sum)