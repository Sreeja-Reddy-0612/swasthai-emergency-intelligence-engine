from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.emergency_routes import router as emergency_router
from ai_engine.ingestion.json_loader import load_medical_knowledge
from ai_engine.ingestion.chunker import chunk_text
from ai_engine.vector_store.vector_db import build_vector_store

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

data_path = os.path.join(BASE_DIR, "data", "medical_knowledge.json")

medical_data = load_medical_knowledge(data_path)

chunks=chunk_text(medical_data)

build_vector_store(chunks)

app = FastAPI(
    title="SwasthAI Emergency Intelligence Engine",
    version="0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(emergency_router, prefix="/api")


@app.get("/")
def root():
    return {
        "service": "SwasthAI Emergency Intelligence Engine",
        "status": "running"
    }