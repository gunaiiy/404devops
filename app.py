import os
import socket
import time
from datetime import datetime

from flask import Flask, render_template, jsonify

app = Flask(__name__)

START_TIME = time.time()

# --- CI/CD-dən gələcək məlumatlar (env dəyişənləri kimi) ---
GIT_COMMIT = os.environ.get("GIT_COMMIT", "local-dev")
APP_VERSION = os.environ.get("APP_VERSION", "v0.1.0")
ENVIRONMENT = os.environ.get("ENVIRONMENT", "local")

# Sadə in-memory sayğac (hər sorğuda artır)
request_count = 0


def get_uptime():
    seconds = int(time.time() - START_TIME)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours}h {minutes}m {seconds}s"


@app.route("/")
def home():
    global request_count
    request_count += 1
    data = {
        "pod_name": socket.gethostname(),
        "node_name": os.environ.get("NODE_NAME", "unknown-node"),
        "git_commit": GIT_COMMIT,
        "app_version": APP_VERSION,
        "environment": ENVIRONMENT,
        "uptime": get_uptime(),
        "request_count": request_count,
        "deployed_at": os.environ.get("DEPLOYED_AT", "unknown"),
    }
    return render_template("index.html", **data)


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


@app.route("/version")
def version():
    return jsonify(
        version=APP_VERSION,
        git_commit=GIT_COMMIT,
        environment=ENVIRONMENT,
    )


@app.route("/pod-info")
def pod_info():
    return jsonify(
        pod_name=socket.gethostname(),
        node_name=os.environ.get("NODE_NAME", "unknown-node"),
        pod_ip=os.environ.get("POD_IP", "unknown"),
    )


@app.route("/metrics")
def metrics():
    # Sadə Prometheus formatında metrics (real layihədə prometheus_client
    # kitabxanası istifadə oluna bilər, bura sadə nümunədir)
    uptime_seconds = int(time.time() - START_TIME)
    output = (
        f"# HELP app_request_count Total number of requests\n"
        f"# TYPE app_request_count counter\n"
        f"app_request_count {request_count}\n"
        f"# HELP app_uptime_seconds Application uptime in seconds\n"
        f"# TYPE app_uptime_seconds gauge\n"
        f"app_uptime_seconds {uptime_seconds}\n"
    )
    return output, 200, {"Content-Type": "text/plain; charset=utf-8"}


@app.route("/chaos", methods=["POST"])
def chaos():
    """Qəsdən pod-u çökdürür ki, Kubernetes-in onu necə
    avtomatik yenidən başlatdığını canlı göstərsin."""
    app.logger.warning("Chaos endpoint çağırıldı — proses qəsdən dayandırılır!")
    os._exit(1)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)