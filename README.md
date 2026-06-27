# 🚀 CI/CD Pipeline Demo (Python + Flask)

![CI/CD Pipeline](https://github.com/MantashaR/cicd-pipeline-demo/actions/workflows/ci-cd.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-python--slim-blue?logo=docker)
![Deployed on Render](https://img.shields.io/badge/Deployed-Render-46E3B7?logo=render)

An end-to-end **CI/CD pipeline** that takes a **Python Flask** web app from
`git push` all the way to a live, deployed URL — fully automated, with zero
manual steps.

> **Live demo:** _add your Render URL here after deploy_

---

## 🔧 What it does

The same pipeline is implemented in **two CI/CD engines** — GitHub Actions
(`.github/workflows/ci-cd.yml`) and Jenkins (`Jenkinsfile`). Every push to
`main` triggers:

```
git push
  │
  ▼
┌──────────────┐   ┌──────────────┐   ┌─────────────────┐   ┌──────────────┐   ┌────────────┐
│ 1. Lint+Test │ → │ 2. Build     │ → │ 3. Push image   │ → │ 4. Deploy    │ → │ 5. Notify  │
│  htmlhint +  │   │   Docker     │   │   to Docker Hub │   │   to Render  │   │   Slack    │
│  smoke tests │   │   image      │   │                 │   │              │   │            │
└──────────────┘   └──────────────┘   └─────────────────┘   └──────────────┘   └────────────┘
```

If any test fails, the build stops — nothing broken ever reaches production.

## 🛠️ Tech Stack

| Concern            | Tool                          |
|--------------------|-------------------------------|
| CI/CD engine       | GitHub Actions **and** Jenkins|
| Web app            | Python + Flask + gunicorn     |
| Containerization   | Docker (python:3.12-slim)     |
| Image registry     | Docker Hub                    |
| Hosting / deploy   | Render (push-to-deploy)       |
| Quality gate       | flake8 (lint) + pytest (tests)|
| Notifications      | Slack webhook (optional)      |

## ▶️ Run locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the tests + lint
flake8 app.py tests/ --max-line-length=100
pytest -v

# Run the app directly
python app.py
# open http://localhost:5000

# ...or build and run the container
docker build -t cicd-demo .
docker run -p 5000:5000 cicd-demo
```

## ⚙️ Setup (to make the pipeline live)

1. Push this repo to GitHub.
2. In **Settings → Secrets and variables → Actions**, add:
   - `DOCKERHUB_USERNAME` — your Docker Hub username
   - `DOCKERHUB_TOKEN` — a Docker Hub access token
   - `RENDER_DEPLOY_HOOK` — the deploy hook URL from your Render service
   - `SLACK_WEBHOOK` — (optional) an incoming-webhook URL
3. Create a Render web service from this repo (it reads `render.yaml`).
4. Push a commit → watch the Actions tab run all 5 stages. ✅

## 🧱 Jenkins version

A self-hosted equivalent of the pipeline lives in the `Jenkinsfile`. To run it
locally with a containerized Jenkins server, see [`jenkins/README.md`](jenkins/README.md).

## 📚 What I learned

- Writing multi-stage GitHub Actions workflows with job dependencies (`needs`)
- Containerizing apps and publishing versioned images to a registry
- Secure credential handling with GitHub Secrets (no hardcoded keys)
- Automated quality gates that block bad code from deploying
- Push-to-deploy continuous delivery to a cloud host
- Implementing the same pipeline in both **GitHub Actions** and **Jenkins**
  (declarative pipeline, credentials binding, stage view)
