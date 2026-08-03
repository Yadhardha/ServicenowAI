import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()


INSTANCE = "https://dev381973.service-now.com"
BASE_URL = f"{INSTANCE}/api/now/table/incident"

USERNAME = os.getenv("username")
PASSWORD = os.getenv("password")

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}



def get_sys_id(incident_number):

    query_url = f"{BASE_URL}?sysparm_query=number={incident_number}"

    response = requests.get(
        query_url,
        auth=(USERNAME, PASSWORD),
        headers=HEADERS
    )

    if response.status_code != 200:
        return None

    result = response.json()["result"]

    if len(result) == 0:
        return None

    return result[0]["sys_id"]




def create_incident(
        short_description,
        description,
        category="software",
        impact="2",
        urgency="2"
):

    payload = {
        "short_description": short_description,
        "description": description,
        "category": category,
        "impact": impact,
        "urgency": urgency
    }

    try:

        response = requests.post(
            BASE_URL,
            auth=(USERNAME, PASSWORD),
            headers=HEADERS,
            json=payload,
            timeout=30
        )

        if response.status_code == 201:

            result = response.json()["result"]

            print("\nIncident Created Successfully")
            print("Incident Number :", result["number"])
            print("Sys ID :", result["sys_id"])

            return result["number"], result["sys_id"]

        else:

            print("Failed to Create Incident")
            print(response.status_code)
            print(response.text)

            return None, None

    except Exception as e:

        print("Error:", e)

        return None, None


def update_incident(incident_number, work_notes):

    sys_id = get_sys_id(incident_number)

    if not sys_id:
        print("Incident not found")
        return

    payload = {
        "work_notes": work_notes
    }

    update_url = f"{BASE_URL}/{sys_id}"

    response = requests.patch(
        update_url,
        auth=(USERNAME, PASSWORD),
        headers=HEADERS,
        json=payload
    )

    if response.status_code == 200:

        print("Incident Updated Successfully")

    else:

        print("Update Failed")
        print(response.text)



def resolve_incident(incident_number, close_notes):

    sys_id = get_sys_id(incident_number)

    if not sys_id:
        print("Incident not found")
        return

    payload = {
        "state": "6",
        "incident_state": "6",

        "close_code": "Solution provided",

        "close_notes": "Docker container flask-app was restored and validated successfully."

    }
    update_url = f"{BASE_URL}/{sys_id}"

    response = requests.patch(
        update_url,
        auth=(USERNAME, PASSWORD),
        headers=HEADERS,
        json=payload
    )

    if response.status_code == 200:

        print("Incident Resolved Successfully")

    else:

        print("Resolve Failed")
        print(response.text)
    print(json.dumps(response.json(),indent=2))


def get_incident(incident_number):

    query_url = f"{BASE_URL}?sysparm_query=number={incident_number}"

    response = requests.get(
        query_url,
        auth=(USERNAME, PASSWORD),
        headers=HEADERS
    )

    if response.status_code == 200:

        result = response.json()["result"]

        if len(result) > 0:

            return result[0]

    return None



def get_open_incidents():
    query = (
        "state!=6",
        "^sys_created_on=>javascript:gs.minutesAgoStart(30)"
    )

    q_url = f"{BASE_URL}?sysparm_query={query}"


    response = requests.get(
        q_url,
        auth=(USERNAME, PASSWORD),
        headers=HEADERS
    )

    if response.status_code == 200:

        return response.json()["result"]

    return []