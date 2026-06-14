from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output,model,MODEL_VERSION
from schema.prediction_response import PredictionResponse
from fastapi import HTTPException

app = FastAPI()

#human readable
@app.get('/')
def home():
   return {'message': 'Insurance Premium Prediction API'}

#machine readable
@app.get('/health')
def health_check():
   return {
      'status': 'OK',
      'version': MODEL_VERSION,
      'model_loaded': model is not None
   }

@app.post('/predict',response_model= PredictionResponse)
def predict_premium(data: UserInput):
   
   user_input = {
      'age': data.age,
        'smoker': data.smoker,
        'region': data.region,
        'children': data.children,
        'sex': data.sex,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'bmi': data.bmi
   }

   user_input["age_squared"] = user_input["age"] ** 2
   user_input["bmi_age"] = user_input["bmi"] * user_input["age"]

   try:

     prediction = predict_output(user_input)

     return JSONResponse(status_code=200, content={'response':prediction})
  
   except Exception as e:
    raise HTTPException(
        status_code=500,
        detail=str(e)
    )


#These are the improvements we've done in this API:
#add routes like health check.
#try catch.
#Add confidence score.
#response model.
