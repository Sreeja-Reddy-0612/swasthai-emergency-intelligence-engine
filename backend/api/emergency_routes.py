from fastapi import APIRouter
from pydantic import BaseModel
from ai_engine.pipeline.emergency_pipeline import run_emergency_pipeline

router = APIRouter()


class EmergencyRequest(BaseModel):
    message: str
    age: int | None = None


@router.post("/emergency/analyze")
def analyze_emergency(data: EmergencyRequest):

    result = run_emergency_pipeline(
        message=data.message,
        age=data.age
    )

    return result