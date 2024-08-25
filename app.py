from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import joblib
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestSchema(BaseModel):
    "Request Schema"
    screen_time_and_sleep_quality: int
    education_level: int
    average_daily_screen_time: int
    sleep_issues_from_screen_time: int


@app.post("/get_prediction")
def prediction(item: RequestSchema):
    screen_time_and_sleep_quality: int = item.screen_time_and_sleep_quality
    education_level: int = item.education_level
    average_daily_screen_time: int = item.average_daily_screen_time
    sleep_issues_from_screen_time: int = item.sleep_issues_from_screen_time


    response = model_prediction(
        screen_time_and_sleep_quality=screen_time_and_sleep_quality,
        education_level=education_level,
        average_daily_screen_time=average_daily_screen_time,
        sleep_issues_from_screen_time=sleep_issues_from_screen_time
    )

    return {
        "model_response": response
    }, 200


def model_prediction(
    screen_time_and_sleep_quality: int,
    education_level: int,
    average_daily_screen_time: int,
    sleep_issues_from_screen_time: int,
    model_path: str="./model.pkl"
):
    classifier = joblib.load(model_path)

    input_data = np.array([
            screen_time_and_sleep_quality,
            education_level,
            average_daily_screen_time,
            sleep_issues_from_screen_time
    ])
    response = classifier.predict(input_data.reshape(1, -1))
    return response.tolist()



