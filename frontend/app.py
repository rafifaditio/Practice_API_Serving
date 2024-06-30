import streamlit as st
import requests
import pickle

st.title("Credit Risk Prediction")

st.write('Insert feature to predict')

# user input
person_age= st.number_input(label='Age', value=20)
person_income=st.number_input(label="person_income", value= 64900)
person_home_ownership=st.selectbox(label="person_home_ownership",options=['RENT','OWN','MORTGAGE','OTHER' ])
person_emp_length=st.number_input(label="person_emp_length",value=4.0)
loan_intent=st.selectbox(label="loan_intent",options=['PERSONAL','EDUCATION','MEDICAL',
                                                      'VENTURE','HOMEIMPROVEMENT','DEBTCONSOLIDATION'])
loan_grade=st.selectbox(label="loan_grade",options=['D','B','C','A','E','F','G'])
loan_amnt=st.number_input(label="loan_amnt",value=13625)
loan_int_rate=st.number_input(label="loan_int_rate",value=10)
loan_percent_income=st.number_input(label="loan_percent_income",value=0.21)
cb_person_default_on_file = st.selectbox(label="cb_person_default_on_file",options=['Y','N'])
cb_person_cred_hist_length=st.number_input(label="cb_person_cred_hist_length",value= 3)

# convert into dataframe
# data = pd.DataFrame({"person_age": [person_age],
# "person_income": [person_income],
# "person_home_ownership": [person_home_ownership],
# "person_emp_length": [person_emp_length],
# "loan_intent": [loan_intent],
# "loan_grade": [loan_grade],
# "loan_amnt": [loan_amnt],
# "loan_int_rate": [loan_int_rate],
# "loan_percent_income": [loan_percent_income],
# "cb_person_default_on_file": [cb_person_default_on_file],
# "cb_person_cred_hist_length":[cb_person_cred_hist_length]})

URL = "http://backend:8000/predict"
param = {"person_age": person_age,
"person_income": person_income,
"person_home_ownership": person_home_ownership,
"person_emp_length": person_emp_length,
"loan_intent": loan_intent,
"loan_grade": loan_grade,
"loan_amnt": loan_amnt,
"loan_int_rate": loan_int_rate,
"loan_percent_income": loan_percent_income,
"cb_person_default_on_file": cb_person_default_on_file,
"cb_person_cred_hist_length":cb_person_cred_hist_length}
r = requests.post(URL, json=param)

if st.button('Predict'):
    if r.status_code == 200:
        res = r.json()
        st.write(res['prediction'])
    else:
        st.write("Unexpected Error")

