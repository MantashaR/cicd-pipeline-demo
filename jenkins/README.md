# Running the Jenkins Pipeline

This project ships **two** CI/CD implementations of the same pipeline:

- `.github/workflows/ci-cd.yml` — GitHub Actions (cloud, zero setup)
- `Jenkinsfile` — Jenkins (self-hosted CI server)

Talking about both in an interview shows you understand CI/CD as a *concept*,
not just one vendor's tool.

## 1. Start Jenkins locally

```bash
cd jenkins
docker compose up -d
```

Open <http://localhost:8080>. Get the first-run admin password with:

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Install the **suggested plugins** when prompted, then create your admin user.

## 2. Install required tools/plugins

- Plugins: **Docker Pipeline**, **Git**, **Credentials Binding** (most are in
  the "suggested" set).
- Node.js is invoked via `npx` in the agent — install the **NodeJS** plugin, or
  use a Jenkins agent image that already has Node.

## 3. Add credentials

**Manage Jenkins → Credentials → System → Global → Add Credentials:**

| ID                  | Kind                | Value                          |
|---------------------|---------------------|--------------------------------|
| `dockerhub-creds`   | Username & password | Docker Hub user + access token |
| `render-deploy-hook`| Secret text         | Render deploy hook URL         |
| `slack-webhook`     | Secret text         | (optional) Slack webhook URL   |

## 4. Create the pipeline job

1. **New Item → Pipeline** → name it `cicd-pipeline-demo`.
2. Under **Pipeline**, choose **Pipeline script from SCM**.
3. SCM: **Git**, Repository URL: your GitHub repo URL.
4. Script Path: `Jenkinsfile` (the default).
5. Save → **Build Now**.

Watch the stages run in the **Stage View**: Checkout → Lint & Test →
Build & Push → Deploy → (post) Notify. Screenshot this for your portfolio.

## 5. (Optional) Auto-trigger on push

Add a GitHub webhook pointing to `http://<your-jenkins>/github-webhook/`, or
enable **Poll SCM** / **GitHub hook trigger** in the job config so every push
kicks off a build automatically.
