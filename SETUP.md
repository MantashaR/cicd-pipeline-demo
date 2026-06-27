# 🪜 Setup Checklist — Go Live in ~20 Minutes

Follow these steps **in order**. No coding — just clicking buttons and copying
2 values into GitHub. At the end, your pipeline will be fully green ✅ and you'll
have a **live website URL** for your resume.

Your repo: <https://github.com/MantashaR/cicd-pipeline-demo>

---

## ✅ Step 1 — Create a Docker Hub account + token (5 min)

Docker Hub is the "warehouse" where your app's container image is stored.

1. Go to <https://hub.docker.com/signup> and sign up (free). Remember your
   **username**.
2. After logging in, click your **avatar (top-right) → Account settings**.
3. In the left menu click **Personal access tokens** → **Generate new token**.
4. Description: `github-actions`. Permissions: **Read & Write**. Click
   **Generate**.
5. **Copy the token now** — it's shown only once. Paste it somewhere temporary.

You now have two values: your **username** and a **token**.

---

## ✅ Step 2 — Add those secrets to GitHub (3 min)

This gives the pipeline the "warehouse key" — securely, never in your code.

1. Open <https://github.com/MantashaR/cicd-pipeline-demo/settings/secrets/actions>
2. Click **New repository secret**. Add the first one:
   - **Name:** `DOCKERHUB_USERNAME`
   - **Secret:** your Docker Hub username
   - Click **Add secret**.
3. Click **New repository secret** again. Add the second:
   - **Name:** `DOCKERHUB_TOKEN`
   - **Secret:** the token you copied in Step 1
   - Click **Add secret**.

You should now see 2 secrets listed.

---

## ✅ Step 3 — Create the Render web service (5 min)

Render is the "live server" that hosts your app on the internet for free.

1. Go to <https://render.com> → **Get Started** → sign in **with GitHub**
   (easiest — it links your repos automatically).
2. On the dashboard click **New +** → **Web Service**.
3. Find **cicd-pipeline-demo** in the list → click **Connect**.
4. Render auto-detects the `render.yaml` / Dockerfile. Confirm these:
   - **Language / Runtime:** Docker
   - **Instance type:** **Free**
   - **Branch:** main
5. Click **Create Web Service**. Render builds the image and deploys it
   (takes 2–4 min the first time).
6. When done, you'll see a URL like
   `https://cicd-pipeline-demo.onrender.com` — **open it. That's your live app!** 🎉

---

## ✅ Step 4 — Connect the Render deploy hook to GitHub (3 min)

This makes Render redeploy automatically every time the pipeline runs.

1. In your Render service, go to **Settings** (left menu).
2. Scroll to **Deploy Hook** → click **Copy** (it's a long URL).
3. Back on GitHub:
   <https://github.com/MantashaR/cicd-pipeline-demo/settings/secrets/actions>
   → **New repository secret**:
   - **Name:** `RENDER_DEPLOY_HOOK`
   - **Secret:** the deploy hook URL you copied
   - **Add secret**.

*(Optional: for Slack alerts, add a `SLACK_WEBHOOK` secret the same way. Skip if
you don't want it — the pipeline works fine without it.)*

---

## ✅ Step 5 — Trigger the full pipeline + verify (2 min)

Make any tiny change so a fresh pipeline runs with all the keys in place.

Easiest way (right on GitHub, no terminal):
1. Open `README.md` in your repo → click the **pencil (Edit)** icon.
2. Add a space anywhere → **Commit changes**.
3. Go to the **Actions** tab → watch the run. All stages should go green:
   ```
   ✓ Lint & Test
   ✓ Build & Push Image
   ✓ Deploy to Render
   ✓ Notify
   ```

Or from your terminal:
```bash
cd C:/Users/Lenovo/cicd-pipeline-demo
git commit --allow-empty -m "Trigger full pipeline"
git push
```

---

## 🎯 You're done — for your resume

1. Take a **screenshot** of the green Actions run.
2. Edit `README.md` and replace the "Live demo" line with your Render URL.
3. Add this to your resume:

> Built an end-to-end CI/CD pipeline (GitHub Actions + Jenkins) for a Python
> Flask app: automated pytest testing and flake8 linting, Docker
> containerization, image publishing to Docker Hub, and auto-deployment to a
> live Render URL on every push — with secure secrets management.

Live URL: `__paste your Render link here__`
Repo: <https://github.com/MantashaR/cicd-pipeline-demo>
