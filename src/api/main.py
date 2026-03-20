#Import FastAPI + Pipeline
from fastapi import FastAPI
from pydantic import BaseModel

from src.inference_pipeline.predict import predict

#create app
app = FastAPI()

#Define Input Schema , This ensures correct input format
class HouseData(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int
    mainroad: str
    guestroom: str
    basement: str
    hotwaterheating: str
    airconditioning: str
    parking: int
    prefarea: str
    furnishingstatus: str

#Home Endpoint
@app.get("/")
def home():
    return {"message": "House Price Prediction API"}

#Prediction Endpoint
@app.post("/predict")
def get_prediction(data: HouseData):
    input_data = data.dict()

    result = predict(input_data)

    return {"predicted_price": result}
