import requests
import json
import os 
from dotenv import load_dotenv

load_dotenv()


USERNAME = os.getenv("username")
PASSWORD = os.getenv("password")

instance = "dev381973.service-now.com"

url = f"https://{instance}/api/now/table/sys_choice"

params = {
    "sysparm_query": "name=incident^element=close_code",
    "sysparm_fields": "label,value"
}

response = requests.get(
    url,
    auth=(USERNAME, PASSWORD),
    params=params,
    headers={"Accept": "application/json"}
)

print(json.dumps(response.json(), indent=2))
