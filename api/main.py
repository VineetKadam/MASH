from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator.orchestrator import run_diagnosis
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Medical Diagnosis System")

class PatientInput(BaseModel):
    symptoms: str


@app.get("/")
def home():
    return {"message": "AI Medical Diagnosis API Running"}


@app.post("/diagnose")
def diagnose(patient: PatientInput):

    result = run_diagnosis(patient.symptoms)

    return {
        "symptoms": patient.symptoms,
        "diagnosis_summary": result
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)