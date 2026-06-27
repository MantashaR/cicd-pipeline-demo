"""A tiny Flask web app — the thing our CI/CD pipeline ships.

Routes:
  /        -> a landing page that shows the live build number + commit
  /health  -> a JSON health check (used by Docker + uptime monitors)
"""
import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# These are injected by the CI/CD pipeline at deploy time (env vars).
BUILD_NUMBER = os.environ.get("BUILD_NUMBER", "local")
COMMIT_SHA = os.environ.get("COMMIT_SHA", "dev")


@app.route("/")
def home():
    return render_template(
        "index.html",
        build=BUILD_NUMBER,
        commit=COMMIT_SHA[:7],
    )


@app.route("/health")
def health():
    """Lightweight health check — returns 200 when the app is up."""
    return jsonify(status="ok", build=BUILD_NUMBER)


if __name__ == "__main__":
    # For local dev only. In production gunicorn runs the app (see Dockerfile).
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
