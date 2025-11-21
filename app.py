from fastapi import FastAPI, Request, HTTPException, Body
import uvicorn
import os
from fastapi.responses import PlainTextResponse
from textSummarizer.pipeline.prediction import PredictionPipeline

app = FastAPI()

@app.get("/")
async def index():
    return "Text Summarization API is running. Send a POST request to /predict with your text to get a summary."

@app.get("/train")
async def train_model():
    try:
        os.system("python main.py")
        return "Training completed successfully"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict", response_class=PlainTextResponse)
async def predict_model(text: str = Body(..., media_type="text/plain")):
    try:
        if not text.strip():
            raise HTTPException(status_code=400, detail="Text cannot be empty")
            
        prediction_pipeline = PredictionPipeline()
        return prediction_pipeline.predict(text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)