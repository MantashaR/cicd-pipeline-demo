# Production image: Python + Flask served by gunicorn.
FROM python:3.12-slim

WORKDIR /app

# Install dependencies first (better layer caching).
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code.
COPY app.py .
COPY templates/ templates/
COPY static/ static/

EXPOSE 5000

# Basic container healthcheck — hits the /health endpoint.
HEALTHCHECK --interval=30s --timeout=3s \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

# gunicorn is a production-grade WSGI server (don't use Flask's dev server in prod).
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
