import re

print (re.search('^a\S+b$','acccb'))
k = (re.search('^From\s+H', 'From Here to Eternity'))
print(k)
print(type(k))
print(re.search('[k\s+}$]', '{block }'))
x = "My name is lakhan 1 2 ka 14"
y=re.findall('[0-9]',x)
print (y)
print(type(y))
print (y[0])

print (re.findall('\d+', '8837 a difficult data analysis problem to having fun to helping 128'))

y = re.findall('\S+k\S+', x)
print (y)

print (re.findall('\S+?@\S+', 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'))

print(re.findall('href="(.+)"','<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'))