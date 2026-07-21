# 🚀 404 DevOps

A live DevOps portfolio project — not just an app, but a real environment demonstrating containerization, orchestration, CI/CD, monitoring, and infrastructure-as-code.

🔗 **Live demo:** _coming soon (after VM + Kubernetes deployment)_

---

## What it does

A simple Flask "infrastructure dashboard" that:

- Shows which Pod and Node handled the request, live
- Displays the deployed Git commit and version (proof of CI/CD)
- Exposes `/metrics` in Prometheus format
- Has a **"Chaos Test"** button that intentionally crashes the pod — demonstrating Kubernetes self-healing in real time

## Tech Stack

| Layer | Technology |
|---|---|
| App | Python (Flask) |
| Containerization | Docker |
| Orchestration | Kubernetes (kubeadm) |
| IaC | Terraform |
| CI/CD | GitHub Actions |
| Monitoring | Prometheus + Grafana |
| Logging | ELK Stack |
| DNS/SSL | Let's Encrypt (cert-manager) |

## API Endpoints

| Endpoint | Description |
|---|---|
| `/` | Main dashboard (HTML) |
| `/health` | Health check (for Kubernetes probes) |
| `/version` | Deployed version + Git commit |
| `/pod-info` | Pod/Node info (JSON) |
| `/metrics` | Prometheus-format metrics |
| `/chaos` | Intentionally crashes the pod (POST) |


## Roadmap

- [x] Flask dashboard app
- [x] Dockerfile
- [ ] Terraform infrastructure
- [ ] Kubernetes cluster (kubeadm)
- [ ] Deployment/Service/Ingress
- [ ] GitHub Actions CI/CD
- [ ] Domain + HTTPS
- [ ] Prometheus + Grafana
- [ ] ELK logging

## Author

**Gunay Abdullazada** · [LinkedIn](https://www.linkedin.com/in/gunay-abdullazada/)
