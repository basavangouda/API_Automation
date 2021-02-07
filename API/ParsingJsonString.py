import json

#section 1
#dictionary
from API.payload import addpayload

'''course = '{"name":"Basavanagouda","languages":["python","Java"]}'

#loads method parse json string and it returns dictionary
dict_course = json.loads(course)

print(dict_course)
print(type(dict_course))
print(dict_course['languages'])
print(dict_course['name'])
print(dict_course['languages'][0])

#Another way of parsing content in json file into dictionary
with open("C:\\Users\\Lenovo\\Desktop\\PythonPractice\\Final_Automation_Practice\\API\\Jsonfile.json") as f:

    data=json.load(f)
    print(type(data))
    print(data)
    print(data['data'][2])
    print(data['data'][2]['last_name'])

#parsing complex json with nested structure
    for data1 in data['data']:
        print(data1)
        if data1['id'] == 12:
            print(data1['email'])
            assert data1['email']=="rachel.howell@reqres.in"

# Comparison of 2 json files

with open("C:\\Users\\Lenovo\\Desktop\\PythonPractice\\Final_Automation_Practice\\API\\jsonfile1.json") as f1:
    data2=json.load(f1)
    print(data2)

    assert data == data2'''

#section2  with request Module
'''import requests

response = requests.get("https://reqres.in/api/users",params={'name':'basavanagouda'},)
print(response.text)
print(type(response.text))
dict_response=json.loads(response.text)
print(dict_response)
print(dict_response['data'][0]['id'])
print(response.status_code)'''

#we can do all these above things in one shot
'''json_repose=response.json()
print(json_repose)
print(type(json_repose))

#validation of status code and header
assert response.status_code == 200
print(response.headers)
print(type(response.headers))
assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

for actual_data in json_repose['data']:
    #print(type(data))
    if actual_data['id'] == 5:
        print(actual_data)
        break #***** very very imported if you dont put it will give assertion error

expected_data ={'id': 5, 'email': 'charles.morris@reqres.in', 'first_name': 'Charles', 'last_name': 'Morris', 'avatar': 'https://reqres.in/img/faces/5-image.jpg'}

assert actual_data == expected_data'''

#using post method
'''import requests

adding_user=requests.post("https://reqres.in/api/users",json=addpayload("basavanagouda"),headers={"Content-Type":"application/json"},)

print(adding_user.json())
response_json=adding_user.json()
print(type(response_json))

user_id=response_json['id']

print(user_id)

#delete
delete_user=requests.delete("https://reqres.in/api/users",json={'id':user_id},headers={"Content-Type":"application/json"},)
print(delete_user.status_code)
print(type(delete_user))
#response_delet=delete_user.json()
#print(response_delet)
assert delete_user.status_code==204'''


#section 5 setting up global configuration using congig object
import requests
import configparser

config=configparser.ConfigParser()
config.read('C:/Users/Lenovo/Desktop/PythonPractice/Final_Automation_Practice/API/utilities/properties.ini')

adding_user=requests.post(config['API']['endpoint']+'/api/users',json=addpayload("basavanagouda"),headers={"Content-Type":"application/json"},)

print(adding_user.json())
response_json=adding_user.json()
print(response_json['name'])
user_id=response_json['id']
print(user_id)
'''
#delete
delete_user=requests.delete("https://reqres.in/api/users",json={'id':user_id},headers={"Content-Type":"application/json"},)
print(delete_user.status_code)
assert delete_user.status_code==204'''


# Now i want to drive config from configration file
'''import requests
from API.utilities.configurations import *
from API.utilities.Resources import *
from payload import *

url=getconfig()['API']['endpoint']+Apiresources.add_user
query='select * from user1'
adding_user=requests.post(url,json=buildpayload(query),headers={"Content-Type":"application/json"},)

print(adding_user.json())
response_json=adding_user.json()
print(type(response_json))
user_id=response_json['id']
print(user_id)

#delete
url=getconfig()['API']['endpoint']+Apiresources.delete_user
delete_user=requests.delete(url,json={'id':user_id},headers={"Content-Type":"application/json"},)
print(delete_user.status_code)
assert delete_user.status_code==204'''
'''
auth=('basavangouda','abc9741090584@J')
r=requests.get('https://api.github.com/user',verify=False,auth=auth)
print(r.status_code)

se=requests.session()
se.auth=auth=('basavangouda','abc9741090584@J')
url2='https://api.github.com/user/repos'
res=se.get(url2)
print(res.status_code)
'''

#cookies passing
import requests
'''se=requests.session()
se.cookies.update({'visit-month':'January'})
response=se.get("https://httpbin.org/cookies", allow_redirects=False, cookies={'visit-year':'2021'},timeout=1)
print(response.history)
print(response.text)'''

#Attahemnt sending
'''url3="https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open('C:\\Users\\Lenovo\\Desktop\\Perents.jpg', 'rb')}
responce1=requests.post(url3,files=files)
print(responce1.status_code)
print(responce1.text)
'''