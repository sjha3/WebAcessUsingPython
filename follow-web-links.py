import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
count = int(input('Enter Count:'))
position = int(input('Enter Position:'))
url = ' http://py4e-data.dr-chuck.net/known_by_Trudy.html'
i = 0
while i < count:
    j=1
    html = urllib.request.urlopen(url).read()
    #print('url : ', url, 'i :',i)
    soup = BeautifulSoup(html, 'html.parser')
    print('Get a tags')
    tags = soup('a')
    for tag in tags:
        print('tag : ',tag.get('href',None))
        if j < position:
            j=j+1
            continue
        else:
            if(i == count-1):
                print('Finally reached my destination with content:', tag.contents)
                break
            url = tag.get('href', None)
            break
    if(i == count-1):
        print('Found the URL')
        break
    i = i+1

'''
Following Links in Python

In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

    Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
    Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
    Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
    Last name in sequence: Anayah
    Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Trudy.html
    Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
    Hint: The first character of the name of the last page that you will load is: D

Strategy

The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.

Sample execution

Here is a sample execution of a solution:

$ python3 solution.py
Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Enter count: 4
Enter position: 3
Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html

'''