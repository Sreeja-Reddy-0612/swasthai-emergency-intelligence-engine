from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.emergency_routes import router as emergency_router

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