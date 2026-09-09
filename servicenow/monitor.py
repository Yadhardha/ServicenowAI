import time
from kubernetes import client,config

from incident import create_incident

#connect to kubernetes


config.load_kube_config()

v1 = client.CoreV1Api() # create API object

while True:
    try:
        pods = v1.list_pod_for_all_namespaces()

        for pod in pods.items:
            if not pod.status.container_statuses:
                continue
            for container in pod.status.container_statuses:
                state = container.state

            if state.waiting:
                reason = state.waiting.reason

            elif state.terminated:
                reason = state.terminated.reason

            else:
                continue

            if reason in ["CrashLoopBackOff", "ImagePullBackOff",
                              "ErrImagePull", "OOMKilled","Error"]:
                    pod_name = pod.metadata.name
                    namespace = pod.metadata.namespace
                    container_name = container.name
                    incident_data = {
                        "short_description": (
                            f"Kubernetes Pod Issue Detected\n\n"
                            f"Pod: {pod_name}\n"
                            f"Namespace: {namespace}\n"
                            f"Container: {container_name}\n"
                            f"Issue: {reason}\n"
                    ),
                    "urgency": "2",
                    "priority": "2"
                   }
                    print("\n ISSUE DETECTED")
                    print("Pod:", pod.metadata.name)
                    print("Namespace:", pod.metadata.namespace)
                    print("Container:", container.name)
                    print("Issue:", reason)
        create_incident(incident_data)
        time.sleep(20)

    except Exception as e:
        print("❌ Monitoring error:", e)
        time.sleep(30)
