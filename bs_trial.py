import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
url = input('Enter:')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
print('Get a tags')
tags = soup('a')
for tag in tags:
    print('tag : ', tag)
    print('tag.content : ', tag.contents[0]) #tag.contents returns a list of contents
    print(tag.get('href',None))

print('Get Headers Now')
tags = soup('h1')
for tag in tags:
    print(tag) #the whole tag
    print(tag.contents) # tag content
    print(tag.attrs) #tag attribute
'''
====== Page format ============
<h1>The First Page</h1>
<p>
If you like, you can switch to the 
<a href="http://www.dr-chuck.com/page2.htm">
Second Page</a>.
</p>

========  Output : ============
Enter:http://www.dr-chuck.com/page1.htm  
Get a tags
tag :  <a href="http://www.dr-chuck.com/page2.htm">
Second Page</a>
tag.content :  
Second Page
http://www.dr-chuck.com/page2.htm
Get Headers Now
<h1>The First Page</h1>
['The First Page']
[]
'''