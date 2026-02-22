from fastapi import FastAPI
import requests
import pandas as pd

app = FastAPI(title="Sample FastAPI Project")

# Home route
@app.get("/")
def home():
    return {"message": "FastAPI + requests + pandas example"}

# Fetch sample JSON and return summary using pandas
@app.get("/posts-summary")
def posts_summary():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame(data)

    summary = {
        "total_posts": len(df),
        "unique_users": df["userId"].nunique(),
        "columns": list(df.columns)
    }

    return summary

# Simple health check
@app.get("/health")
def health():
    return {"status": "ok"}
