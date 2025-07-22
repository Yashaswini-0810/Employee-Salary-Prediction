import streamlit as streamlit
import joblib
import numpy

st.title("Salary Prediction")

st.divider()

st.write("With this app, you can get estimations for the salaries of the company employees ")

years=st.number_input(value=1,step=1,min_value=0)

model=joblib.load("linearmodel.pkl")
jobrate=st.number_input(value=3.5,step=0.5,min_value=0.0)

X=[years,jobrate]

st.divider()

predict=st.button("Press the bitton for salary prediction")
st.divider()

if predict:
  st.balloons()
  X1=np.array([X])

  prediction=model.predict(X1)

  st.write("Salary prediction is{prediction}")

  st.divider()







