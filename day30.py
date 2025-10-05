import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#reading the data set 
data = pd.read_csv("dataset.csv")

X = data[["YearsOfExperience"]]
Y = data[["Salary"]]

model = LinearRegression()
model.fit(X , Y)

data["PredictedSalary"] = model.predict(X)

print("model coefficient/slope: ", round(float(model.coef_[0]) , 2))
print("model intercept: ", round(float(model.intercept_) , 2))

plt.scatter(X , Y , color= "red" , label="actual data")
plt.plot(X , data["PredictedSalary"] , color="blue" , label="Regression Line")
plt.xlabel("years of experience")
plt.ylabel("salary")
plt.grid(True)
plt.tight_layout()
plt.show()