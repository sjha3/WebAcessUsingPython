import xml.etree.ElementTree as ET
data = '''<person>
<name>LAKHAN</name>
<password hide="yes"/>
</person>'''

data1 = '''<person>
<users>
    <user x="2">
        <id>001</id>
        <name>ram</name>
    </user>
    <user x="4">
        <id>002</id>
        <name>lakhan</name>
    </user>
</users>
</person>'''



tree = ET.fromstring(data)
print(ET)
print(type(ET))
print('Name',tree.find('name').text)
print('Password attribute',tree.find('password').get('hide'))
print('Name',tree.find('name'))
print("=======================")
tree1 = ET.fromstring(data1)
items= tree1.findall('users/user')
print("Num items :", len(items))
for item in items:
    print('Name : ', item.find('name').text, "\tId : ",item.find('id').text)

'''
Output
<module 'xml.etree.ElementTree' from 'C:\\Users\\sumit\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\xml\\etree\\ElementTree.py'>
<class 'module'>
Name LAKHAN
Password attribute yes
Name <Element 'name' at 0x034D88D0>
=======================
Num items : 2
Name :  ram 	Id :  001
Name :  lakhan 	Id :  002
'''