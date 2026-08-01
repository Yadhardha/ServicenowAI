import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")



def analyze_incident(container_name,
                     status,
                     logs,
                     inspect_data):

    prompt = f"""
You are a Senior Cloud DevOps Engineer.

Analyze the Docker incident.

Container Name:
{container_name}

Container Status:
{status}

Docker Inspect:
{inspect_data}

Docker Logs:
{logs}

Generate professional ServiceNow Work Notes.

Include:

simple explain the issue
with
Cause :
how to resolve : 
wrote simply in common language
Return only plain text.
"""

    response = model.generate_content(prompt)

    return response.text
def analyze_recovery(container_name,
                     logs):

    prompt = f"""
You are a Senior DevOps Engineer.

The Docker container has recovered.

Container Name:
{container_name}

Latest Logs:
{logs}

Generate professional ServiceNow Close Notes.

Include:

1. Recovery Summary
2. Health Status
3. Resolution
4. Recommendation

Return only plain text.
"""
    try:
        response = model.generate_content(prompt)

        return response.text
    except Exception as e:
        return f"Gemini Error : {e}"
    
