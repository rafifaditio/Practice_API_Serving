from fastapi import FastAPI, Request, Response, status
import pandas as pd
import numpy as np
import pickle
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    result = {
        "status": 200,
        "message": "Hello World" 
    }
    return result

# check model loading
@app.get('/check-model')
def check_model():
    try:
        # try to load model
        with open('backend/model_final.pkl', 'rb') as file:
            model = pickle.load(file)
        result = {
            "status": 200,
            "message": "Model loaded successfully"
        }
        return result
    except Exception as e:
        result = {
            "status": 500,
            "message": "Model loading failed",
            "error": str(e)
        }
        return result

# Predict
@app.post('/predict')
async def predict(request: Request):
    # get data from request
    data = await request.json()
    
    replacement = {'person_age':'age', 'person_income': 'income',
                'person_home_ownership':'home_ownership',
                'loan_status':'loan_default',
                'cb_person_default_on_file':'hist_default',
                'cb_person_cred_hist_length':'cred_hist_length'}

    for k, v in list(data.items()):
        data[replacement.get(k, k)] = data.pop(k)
    
    # load model
    with open('backend/model_final.pkl', 'rb') as file:
        model = pickle.load(file)
        
    # label 
    label = ['Good', 'Bad']
    
    # prediction
    try:
        prediction = model.predict(pd.DataFrame(data,index=[0]))
        result = {
            "status": 200,
            "message": "Prediction success",
            "prediction": label[prediction[0]]
        }
        return result
    except Exception as e:
        result = {
            "status": 500,
            "message": "Prediction failed",
            "error": str(e)
        }
        return result
    
# Run API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)


