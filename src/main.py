from fastapi import FastAPI
import os
import json

app = FastAPI()

@app.get("/")
def read_root():
    file_path = os.path.join(os.getcwd(), 'src','transcript_summary.json')
    f = open(file_path)
    data = json.load(f)
    return data

@app.get("/hits")
def read_root():
    return {"Number of hits:"}