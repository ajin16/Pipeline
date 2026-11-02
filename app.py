"""
app.py
------
Application entrypoint alias for Render default deployments.
Re-exports the FastAPI application instance from main.py so commands like:
  - gunicorn app:app
  - uvicorn app:app
work seamlessly out of the box.
"""

from main import app

if __name__ == "__main__":
    import uvicorn
    from config import settings

    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=False)
