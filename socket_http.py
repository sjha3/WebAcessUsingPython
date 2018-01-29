import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'
#NOTE : encode() basically converts Unicode to UTF-8 format here
#We can also give UTF-8 as input to encode(encoding = 'UTF-8) but it's the default value
print('cmd data type before encode: ',type(cmd))
cmd=cmd.encode()
print('cmd data type after encode: ',type(cmd))
mysock.send(cmd)
#print ("Get cmd : ", cmd)

while True:
    data = mysock.recv(1024)
    if (len(data) < 1):
        break
    print('data type before decode : ',type(data))
    print(data.decode(),end='')
    print('data type after decode :', type(data.decode()))
    #decode() converts UTF-8 to Unicode format

mysock.close()

'''
==== Output =====
cmd data type before encode:  <class 'str'>
cmd data type after encode:  <class 'bytes'>
data type before decode :  <class 'bytes'>
HTTP/1.1 200 OK
Date: Mon, 29 Jan 2018 15:23:24 GMT
Server: Apache/2.4.7 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "a7-54f6609245537"
Accept-Ranges: bytes
Content-Length: 167
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain

But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
data type after decode : <class 'str'>
'''
