import os
import uvicorn
from fastapi import FastAPI, BackgroundTasks
from app.services.verifier import run_full_verification

app = FastAPI()

@app.get("/")
async def health_check():
    # Railway needs this to confirm the service is "Alive"
    return {"status": "Online", "engine": "Veritas"}

@app.post("/analyze")
async def analyze_url(url: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(run_full_verification, url)
    return {"status": "Processing", "url": url}

# This part is CRITICAL for Railway
if __name__ == "__main__":
    # Get the port assigned by Railway, or default to 8000 locally
    port = int(os.environ.get("PORT", 8000))
    # Bind to 0.0.0.0 so the internet can reach the container
    uvicorn.run(app, host="0.0.0.0", port=port)