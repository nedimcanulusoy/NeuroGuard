from fastapi import FastAPI
from pydantic import BaseModel
import torch
from ng_models.distilbert_model import dbert

app = FastAPI()
model, tokenizer = dbert()

class InputData(BaseModel):
    data: str

@app.post("/predict")
async def predict(input_data: InputData):
    data = input_data.data
    inputs = tokenizer(data, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits, dim=1).item()
    return {"prediction": prediction}