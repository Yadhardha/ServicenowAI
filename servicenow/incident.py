import requests
from requests.auth import HTTPBasicAuth


URL = "https://dev381973.service-now.com/"
USERNAME = "admin"
PASSWORD = "%Ti^D9WlWzu4"

INCIDENT_URL = f"{URL}/api/now/table/incident"
def create_incident(incident_data):

    headers = {
        "Content-type":"application/json",
        "Accept":"application/json"
    }

    response = requests.post(INCIDENT_URL,auth= HTTPBasicAuth(USERNAME,PASSWORD),json=incident_data,headers=headers)
    print(response.status_code)
    if response.status_code!=200:
        print("Failed to create incident")
        print(response.text)
    result = response.json()["result"]

    incident_number = result["number"]
    print("Incident created :",incident_number)


    n8n_data = {
        "number":incident_number,
        "short_description":incident_data["short_description"],
        "urgency": incident_data["urgency"],
        "priority": incident_data["priority"]

    }

    n8n_url = "https://yadhardha45.app.n8n.cloud/webhook-test/Incident_created"

    n8n_response = requests.post(n8n_url,json= n8n_data,headers={"Content-type":"application/json"})


    print(n8n_response.status_code)
    print(n8n_response.text)
