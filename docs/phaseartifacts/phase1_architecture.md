# Phase 1 Architecture

Frontend (React)
↓
API Request
↓
FastAPI Backend
↓
Emergency Pipeline

Modules

input_processing/context_extractor.py
triage/triage_engine.py
pipeline/emergency_pipeline.py

Response

{
 triage,
 instructions,
 confidence,
 agent_trace
}