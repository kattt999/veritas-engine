from fastapi import FastAPI, BackgroundTasks
from app.services.verifier import run_full_verification

app = FastAPI()

@app.post("/analyze")
async def analyze_url(url: str, background_tasks: BackgroundTasks):
    # 1. Start the long-running AI in the background
    background_tasks.add_task(run_full_verification, url)
    
    # 2. Return immediately so the UI doesn't freeze
    return {"status": "Processing", "url": url}