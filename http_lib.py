import urllib.parse, urllib.request, urllib.error
counts = dict()
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#fhand = urllib.request.urlopen('http://www.google.com')
for lines in fhand:
    #print (lines.decode().strip())
    line = lines.decode()#.strip()
    words = line.split()
    #print (words)
    for word in words:
        counts[word] = counts.get(word, 0) + 1;

print (counts)