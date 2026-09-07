import requests
from requests.auth import HTTPBasicAuth


URL = "https://dev381973.service-now.com/"
USERNAME = "admin"
PASSWORD = "%Ti^D9WlWzu4"

INCIDENT_URL = f"{URL}/api/now/table/incident"


incident_data = {
    "short_description":"Pod is down",
    "description": "kind pod is not running",
    "urgency":"1",
    "impact":"1"
}

headers = {
    "Content-type":"application/json",
    "Accept":"application/json"
}

response = requests.post(INCIDENT_URL,auth= HTTPBasicAuth(USERNAME,PASSWORD),json=incident_data,headers=headers)
print(response.status_code)
result = response.json()["result"]

incident_number = result["number"]
print("Incident created :",incident_number)

n8n_data = {
    "number":incident_number,
    "short_description":incident_data["short_description"],
    "description":incident_data["description"]
}

n8n_url = "https://yadhardha.app.n8n.cloud/webhook-test/incident-created"

n8n_response = requests.post(n8n_url,json= n8n_data,headers={"Content-type":"application/json"})


print(n8n_response.status_code)
print(n8n_response.text)