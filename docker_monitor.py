import docker
from service_now import create_incident

client = docker.from_env()


def container_moniter(container_name):

    try:

        container = client.containers.get(container_name)

        print(f"Container Name : {container.name}")
        print(f"Container Status : {container.status}")

        if container.status == "running":
            print(f"{container.name} is running")
            return None

        logs = container.logs(tail=100).decode("utf-8", errors="ignore")

        inspect = client.api.inspect_container(container.id)

        description = f"""
Container Name : {container.name}

Status : {container.status}

Exit Code : {inspect['State']['ExitCode']}

Restart Count : {inspect['RestartCount']}

Started At : {inspect['State']['StartedAt']}

Finished At : {inspect['State']['FinishedAt']}

Docker Logs:

{logs}
"""

        incident_number, sys_id = create_incident(

            short_description=f"Docker Container {container.name} Stopped",

            description=description,

            category="software",

            impact="2",

            urgency="2"

        )

        print(f"Incident Created : {incident_number}")

        return incident_number

    except Exception as e:

        print("Docker Monitor Error:", e)

        return None