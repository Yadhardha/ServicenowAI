import requests

from dotenv import load_dotenv
import os
from requests.auth import HTTPBasicAuth

load_dotenv()

URL = "https://dev381973.service-now.com/"

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


CHANGE_TASK = f"{URL}/api/now/table/change_task"

task_data = {
    "description": "test data",
    "short_description":"normal test data",
    "impact":"3"
}

headers = {
    "Content-type":"application/json",
    "Accept":"application/json"
}
response = requests.get(CHANGE_TASK,auth = HTTPBasicAuth(USERNAME,PASSWORD),json = task_data,headers= headers)

print(response.status_code)
print(response.json())