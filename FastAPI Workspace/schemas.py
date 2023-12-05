from pydantic import BaseModel


class PersonalInfo(BaseModel):
    age: int
    gender: int
    sports: int
    sleep: int


class EductionalInfo(BaseModel):
    degree_level: int
    year: int
    cgpa: float
    workload: int
    mistreat: int
    academic_pressure: int
    campus_networking: int
    residential_status: int
    field_satisfaction: int


class StressInfo(BaseModel):
    anxiety: int
    isolation: int
    future_insecurity: int
    financial_pressure: int
    stress_score: int
