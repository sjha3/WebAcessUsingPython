import urllib.parse, urllib.error, urllib.request
import json

service = 'http://maps.googleapis.com/maps/api/geocode/json?'
while True:
    place = input("Enter place:")
    url = service+urllib.parse.urlencode({'address':place}) #encode place here
    uh=urllib.request.urlopen(url)
    #urlopen has two ways to see info as shown below
    print("url ", uh.geturl())
    print('url info', uh.info())
    data = uh.read().decode()
    header = uh.getheaders()
    json_data = json.loads(data)
    if 'status' not in json_data or json_data['status'] != 'OK':
        print('Something wrong in retrieving data for',place)
        continue
    print("Complete info of ", place, ":", json_data)
    #print("Complete info of ", place, ":",json.dumps(json_data, indent=4)) #Print in proper format with indentation of 4
    print("Value of key 'formatted_address' :",json_data['results'][0]['formatted_address'])
    print("Geometry results ",json_data['results'][0]['geometry']['location'])
    print("Header : ",header)



'''
Enter place:Raleigh
Complete info of  Raleigh : {'results': [{'address_components': [{'long_name': 'Raleigh', 'short_name': 'Raleigh', 'types': ['locality', 'political']}, {'long_name': 'Wake County', 'short_name': 'Wake County', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'North Carolina', 'short_name': 'NC', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}], 'formatted_address': 'Raleigh, NC, USA', 'geometry': {'bounds': {'northeast': {'lat': 35.97172800000001, 'lng': -78.471063}, 'southwest': {'lat': 35.7158079, 'lng': -78.8190489}}, 'location': {'lat': 35.7795897, 'lng': -78.6381787}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 35.97172800000001, 'lng': -78.471063}, 'southwest': {'lat': 35.7158079, 'lng': -78.8190489}}}, 'place_id': 'ChIJ9-BRny9arIkRrfARilK2kGc', 'types': ['locality', 'political']}], 'status': 'OK'}
Value of key 'formatted_address' : Raleigh, NC, USA
Geometry results  {'lat': 35.7795897, 'lng': -78.6381787}
Header :  [('Content-Type', 'application/json; charset=UTF-8'), ('Date', 'Thu, 01 Feb 2018 04:57:51 GMT'), ('Expires', 'Fri, 02 Feb 2018 04:57:51 GMT'), ('Cache-Control', 'public, max-age=86400'), ('Access-Control-Allow-Origin', '*'), ('Server', 'mafe'), ('X-XSS-Protection', '1; mode=block'), ('X-Frame-Options', 'SAMEORIGIN'), ('Accept-Ranges', 'none'), ('Vary', 'Accept-Language,Accept-Encoding'), ('Connection', 'close')]
Enter place:
'''