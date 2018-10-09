import requests
import json

data = {
    "username": "",
    "password": ""
}
url = "http://127.0.0.1:8000/api-token-auth/"
response = requests.post(url, data=data)
token = json.loads(response.text).get('token')
#print(token)
if token:
    headers={}
    headers['Authorization']= 'Token ' + token
    print(headers)
    response = requests.get("http://127.0.0.1:8000/api/entity/", headers=headers)
    print(response.text)
else:
    print('No Key')