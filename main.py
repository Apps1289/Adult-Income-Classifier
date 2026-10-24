from fastapi import FastAPI
from fastapi.responses import JSONResponse
from user_input import UserInput
from predict import make_prediction 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/health")
def health_check():
    return JSONResponse(content={
        "status": "healthy"
        }, status_code=200)
    
@app.post("/predict")
async def predict(input_data: UserInput):
    try :
        input_df = input_data.model_dump()  # Convert Pydantic model to dictionary
        prediction= make_prediction(input_df)
        
        return JSONResponse(content={"prediction": prediction}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
    