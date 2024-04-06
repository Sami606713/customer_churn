import pandas as pd
import streamlit as st
import pickle as pkl
import pymysql
import os
from dotenv import load_dotenv
load_dotenv()
host=os.getenv("host")
user_name=os.getenv("user_name")
password=os.getenv('password')

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

# def database_connection():
#     try:
#         connection = pymysql.connect(
#             host=host,
#             user=user_name,
#             password=password
#         )
#         st.write("Connected to the database successfully!")
#         create_db(connection)
#         return connection
#     except pymysql.Error as e:
#         print("Error connecting to the database:", e)
#         return None

# def create_db(conn):
    with conn.cursor() as cursor:
        cursor.execute("""create database if not exists Churn_pred""")