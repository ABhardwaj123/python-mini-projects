import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st

#reading the data set 
data = pd.read_csv("dataset.csv")

X = data[["YearsOfExperience"]]
Y = data[["Salary"]]

model = LinearRegression()
model.fit(X , Y)

st.title("Salary predictor")
st.write("enter your years of experience for salary prediction: ")
input = st.number_input("Years of experience: " , min_value=0.0 , max_value=50.0 , step=0.1)

if input:
    print(input)

    prediction = model.predict([[input]])[0]
    st.success(f"estimated salary: {prediction}")


fig , ax = plt.subplots()
ax.scatter(X , Y , color= "red" , label="actual data")
ax.plot(X , model.predict(X) , color="blue" , label="Regression Line")
ax.set_xlabel("years of experience")
ax.set_ylabel("salary")
ax.legend()
st.pyplot(fig)