from flask import Flask
from docker_monitor import container_moniter
from scheduler import scheduler
import threading
import webbrowser

app = Flask(__name__)

@app.route("/")
def home():
    return "AI DevOps Incident Automation Running"

@app.route("/monitor")
def monitor():

    incident = container_moniter("flask-app")

    if incident:

        thread = threading.Thread(
            target=scheduler,
            args=("flask-app", incident),
            daemon=True
        )

        thread.start()

        return f"Incident Created : {incident}"

    return "Container is Healthy"

if __name__ == "__main__":
    app.run(debug=True)