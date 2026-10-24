import pickle
import pandas as pd
from user_input import UserInput
import __main__
from Feature_engineering import FeatureEngineering

__main__.FeatureEngineering = FeatureEngineering

with open("adult_income.pkl", "rb") as f:
    model = pickle.load(f) 
    
def make_prediction(input_data):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    return prediction[0].item()