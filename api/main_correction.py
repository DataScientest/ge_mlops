from fastapi import FastAPI
from pydantic import BaseModel
from models import model


class SentenceBody(BaseModel):
    sentence: str


class Response(BaseModel):
    sentence: str
    score: float
    prediction: int


api = FastAPI()


@api.get("/", tags=["root"])
def get_index():
    return {
        "status": 1
    }


@api.post(
    "/predict",
    tags=["prediction"],
    responses={
        "200": {
            "description": "Ok !",
            "model": Response
        },
        "422": {
            "description": "Wrong data"
        }
    })
def predict(data: SentenceBody):
    prediction = model(data.sentence)
    response = Response(
        sentence=data.sentence,
        score=model(data.sentence),
        prediction=1 if prediction > 0 else 0
    )

    return response
