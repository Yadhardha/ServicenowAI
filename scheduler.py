import time
import docker

from gemini import analyze_incident
from gemini import analyze_recovery

from service_now import update_incident
from service_now import resolve_incident

client = docker.from_env()


def scheduler(container_name, incident_number):

    while True:

        print("Checking container...")

        try:

            container = client.containers.get(container_name)

            # -----------------------
            # Container Running
            # -----------------------

            if container.status == "running":

                logs = container.logs(
                    tail=100
                ).decode("utf-8", errors="ignore")

                close_notes = analyze_recovery(
                    container_name,
                    logs
                )

                resolve_incident(
                    incident_number,
                    close_notes
                )

                print("Incident Resolved.")

                break

            # -----------------------
            # Container Still Down
            # -----------------------

            logs = container.logs(
                tail=100
            ).decode("utf-8", errors="ignore")

            inspect = client.api.inspect_container(container.id)

            work_notes = analyze_incident(

                container_name,

                container.status,

                logs,

                inspect

            )

            update_incident(

                incident_number,

                work_notes

            )

            print("Incident Updated.")

        except Exception as e:

            print(e)

        print("Waiting 2 Minutes...\n")

        time.sleep(120)