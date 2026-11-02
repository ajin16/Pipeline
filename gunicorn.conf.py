"""
gunicorn.conf.py
----------------
Configuration for Gunicorn running on Render or other cloud PaaS.
Automatically binds to 0.0.0.0:$PORT and uses UvicornWorker for FastAPI.
"""

import os

port = os.getenv("PORT", "8000")
bind = f"0.0.0.0:{port}"
workers = int(os.getenv("WEB_CONCURRENCY", "1"))
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 120
keepalive = 5
