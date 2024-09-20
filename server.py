from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/status")
def get_status():
    return {"status": "running"}

@app.get("/jsonfile")
def get_json_file():
    file_path = "data.json"
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type='application/json', filename="data.json")
    else:
        return {"error": "File not found"}
