import pandas as pd
import pickle as pkl
def read_data():
    df=pd.read_csv('Data/clean.csv')
    return df

def prediction(data):
    try:
        with open("churn_pred.pkl",'rb') as f:
            model=pkl.load(f)
            pred=model.predict(data)
            return pred
            
    except FileNotFoundError as e:
        return e
