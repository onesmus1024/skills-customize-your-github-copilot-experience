# Starter code for FastAPI REST API assignment
# Install FastAPI and Uvicorn before running: pip install fastapi uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI API!"}

# Add CRUD endpoints below for your resource (e.g., items or users)
