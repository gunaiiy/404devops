# 404 DevOps

A DevOps portfolio project — not just an app, but a full environment covering
containerization, orchestration, CI/CD, monitoring, and infrastructure-as-code.

Live demo: coming soon, after the VM + Kubernetes deployment is up.

## What it does

A simple Flask "infrastructure dashboard" that shows which pod and node
handled the request, live. It also displays the deployed Git commit and
version as proof the CI/CD pipeline actually ran, exposes `/metrics` in
Prometheus format, and has a "Chaos Test" button that crashes the pod on
purpose — a quick way to watch Kubernetes self-healing in real time.

Built with Flask, Docker, Kubernetes (kubeadm), Terraform, GitHub Actions,
Prometheus + Grafana, the ELK stack, and Let's Encrypt/cert-manager for
HTTPS.

## Endpoints

`/` is the main dashboard. `/health` is what Kubernetes probes check.
`/version` shows the deployed version and Git commit. `/pod-info` returns
pod/node info as JSON. `/metrics` exposes Prometheus-format metrics, and
`/chaos` (POST) intentionally crashes the pod.

## What's next

Flask app and Dockerfile are done. Still to come: Terraform for the
infrastructure, a real kubeadm cluster, Deployment/Service/Ingress,
GitHub Actions CI/CD, a domain with HTTPS, Prometheus + Grafana, and
ELK for logging.
