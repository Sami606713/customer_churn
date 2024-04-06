import streamlit as st
from utils import read_data,prediction
import pandas as pd

def page_config():
    st.set_page_config(
        page_title="Customer Churn Prediction",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

def input_layout():
    # Inilize the empty dic
    dic={}
    df=read_data()
    # st.dataframe(df)
    col1,col2,col3=st.columns(3)
    with col1:
        gender = st.selectbox(
            'Selected Your Gender',
            (df['gender'].value_counts().index))
        dic['gender']=gender
    with col2:
        citizen = st.selectbox(
            'Are you SeniorCitizen are Not',
            (['No',"Yes"]))
        if(citizen=='No'):
            citizen=0
        elif(citizen=="Yes"):
            citizen=1
        dic['SeniorCitizen']=citizen

    with col3:
        dependent = st.selectbox(
            'Are you Dependent',
            (df['Dependents'].value_counts().index))
        dic['Dependents']=dependent

    col4,col5,col6=st.columns(3)
    with col4:
        m_lines = st.selectbox(
            'Select Lines',
            (df['MultipleLines'].value_counts().index))
        dic['MultipleLines']=m_lines 

    with col5:
        backup = st.selectbox(
            'Online Backup',
            (df['OnlineBackup'].value_counts().index))
        dic['OnlineBackup']=backup

    with col6:
        protection = st.selectbox(
            'Device Protection?',
            (df['DeviceProtection'].value_counts().index))
        dic['DeviceProtection']=protection

    col7,col8=st.columns(2)
    with col7:
        tech_support= st.selectbox(
            'TechSupport',
            (df['TechSupport'].value_counts().index))
        dic['TechSupport']=tech_support

    with col8:
        contract = st.selectbox(
            'Select Contract',
            (df['Contract'].value_counts().index))
        dic['Contract']=contract

    col9,col10=st.columns(2)
    with col9:
        m_charges = st.number_input('enter monthly charges',min_value=1)
        dic['MonthlyCharges']=m_charges

    with col10:
        t_charges = st.number_input('enter total charges',min_value=1)
        dic['TotalCharges']=t_charges

    if(st.button("Predict")):
        df=pd.DataFrame(dic,index=[1])
        st.dataframe(df)
        result=prediction(df)[0]
        if(result==0):
            st.error("Customer Can leave them")
        elif(result==1):
            st.success("Customer can't leave")
    
def main():
    # set the page config
    page_config()

    # set the title
    col1,col2,col3=st.columns(3)
    with col1:
        pass
    with col2:
        st.subheader("Customrer Churn Prediction", divider='rainbow')
        # st.title("Customrer Churn Prediction")
    with col3:
        pass
    
    # database_connection()
    # set the input layout
    input_layout()

if __name__=="__main__":
    main()