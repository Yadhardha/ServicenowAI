import requests

from requests.auth import HTTPBasicAuth

URL ="https://dev381973.service-now.com/"
USERNAME="admin"
PASSWORD="%Ti^D9WlWzu4"

CHANGE_URL = f"{URL}/api/now/table/change_request"

change_data ={
    "short_description": "Firmware update is there for recent version of 10",
    "description": "Version update from version 9 to version 10",
    "impact":"2",
    "risk": "moderate",
    "type":"normal"
}

headers = {
    "Content-type":"application/json",
    "Accept":"application/json"
}


response = requests.post(
    CHANGE_URL,auth = HTTPBasicAuth(USERNAME,PASSWORD),json = change_data,headers = headers
)

print(response.status_code)
print(response.json())