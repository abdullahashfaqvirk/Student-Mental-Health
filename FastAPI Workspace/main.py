from fastapi import FastAPI
from utils import get_input_features
from model.model import model1, model2
from model.model import __version__ as model_version
from schemas import PersonalInfo, EductionalInfo, StressInfo


app = FastAPI()


@app.get("/")
async def index():
    return {
        "health_check": "ok",
        "version": model_version
    }


@app.post("/mental-health")
async def prediction(
    personal: PersonalInfo,
    educational: EductionalInfo,
    stress: StressInfo
):
    features = get_input_features(personal, educational, stress)

    prediction1 = int(model1.predict(features))
    prediction2 = int(model2.predict(features))

    return {
        "stress_level": prediction1,
        "depression": prediction2
    }
